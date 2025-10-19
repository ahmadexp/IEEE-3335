"""CLI interface for IEEE-3335 tools."""

import os
import typer
from pathlib import Path
from typing import Optional, List, Tuple
from concurrent.futures import ProcessPoolExecutor, as_completed
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn

from .pdf_extractor import extract_pdf_to_markdown
from .docx_extractor import extract_docx_to_markdown
from .pptx_extractor import extract_pptx_to_markdown

# Import shared console from package
from . import console

app = typer.Typer(
    help="IEEE-3335 Tools",
    add_completion=False,
    no_args_is_help=True,
    rich_markup_mode="rich",  # Enable Rich markup
)


@app.callback()
def callback():
    """
    IEEE-3335 Tools - Utilities for working with IEEE-3335 documents.
    """
    pass


def _extract_single_file(
    input_file: Path, 
    output_file: Optional[Path] = None,
    extract_images: bool = True,
    quiet: bool = False
) -> Tuple[bool, str]:
    """
    Extract a single file to markdown.

    Args:
        input_file: Path to input file
        output_file: Optional output path
        extract_images: Whether to extract images
        quiet: Whether to suppress individual file output messages
        
    Returns:
        Tuple of (success: bool, error_message: str)
    """
    try:
        suffix = input_file.suffix.lower()
        
        if suffix == '.pdf':
            extract_pdf_to_markdown(input_file, output_file, extract_images, quiet)
        elif suffix in ['.docx', '.doc']:
            if suffix == '.doc':
                if not quiet:
                    console.print("[yellow]Warning: .doc files may not be fully supported.[/yellow]")
            extract_docx_to_markdown(input_file, output_file, extract_images)
        elif suffix in ['.pptx', '.ppt']:
            if suffix == '.ppt':
                if not quiet:
                    console.print("[yellow]Warning: .ppt files may not be fully supported. Consider converting to .pptx first.[/yellow]")
            extract_pptx_to_markdown(input_file, output_file, extract_images)
        else:
            return False, f"Unsupported file type: {suffix}"
        
        return True, ""
        
    except Exception as e:
        error_type = type(e).__name__
        error_msg = f"{error_type}: {str(e)}"
        if not quiet:
            console.print(f"[red]Error processing {input_file.name}:[/red] {error_msg}")
        return False, error_msg


def _load_gitignore_patterns(directory: Path) -> List[str]:
    """
    Load .gitignore patterns from the given directory and its parents.
    
    Args:
        directory: Directory to start searching for .gitignore files
        
    Returns:
        List of gitignore patterns (compiled for efficiency)
    """
    patterns = []
    current_dir = directory
    
    # Walk up the directory tree looking for .gitignore files
    while True:
        gitignore_path = current_dir / '.gitignore'
        if gitignore_path.exists():
            try:
                with open(gitignore_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        # Skip empty lines and comments
                        if line and not line.startswith('#'):
                            patterns.append(line)
            except (IOError, OSError):
                # If we can't read the file, just continue
                pass
        
        # Move to parent directory
        parent = current_dir.parent
        if parent == current_dir:
            # Reached root directory
            break
        current_dir = parent
    
    return patterns


def _should_ignore_file(file_path: Path, gitignore_patterns: List[str], base_directory: Path) -> bool:
    """
    Check if a file should be ignored based on gitignore patterns.
    
    Args:
        file_path: Path to check
        gitignore_patterns: List of gitignore patterns
        base_directory: Base directory for relative path calculations
        
    Returns:
        True if file should be ignored, False otherwise
    """
    import fnmatch
    
    # Get relative path from the base directory
    try:
        relative_path = file_path.relative_to(base_directory)
        path_str = str(relative_path).replace('\\', '/')
    except ValueError:
        # If we can't make it relative, use the full path
        path_str = str(file_path).replace('\\', '/')
    
    for pattern in gitignore_patterns:
        pattern = pattern.strip()
        if not pattern:
            continue
            
        # Handle directory patterns (ending with /)
        if pattern.endswith('/'):
            dir_pattern = pattern[:-1]
            # Check if this file is in an ignored directory
            if path_str.startswith(dir_pattern + '/'):
                return True
        else:
            # Simple filename pattern matching
            if fnmatch.fnmatch(path_str, pattern):
                return True
            # Also check just the filename
            if fnmatch.fnmatch(file_path.name, pattern):
                return True
    
    return False


def _collect_files(
    directory: Path, 
    recursive: bool, 
    file_type: str
) -> List[Path]:
    """
    Collect files from directory based on criteria, respecting .gitignore.
    
    Args:
        directory: Directory to search
        recursive: Whether to search recursively
        file_type: Filter by type ('all', 'pdf', 'docx', 'pptx')
        
    Returns:
        List of matching file paths (filtered by gitignore)
    """
    files = []
    
    # Load gitignore patterns from this directory and parents
    gitignore_patterns = _load_gitignore_patterns(directory)
    
    # Define extensions to search for
    if file_type == 'pdf':
        extensions = {'.pdf'}
    elif file_type == 'docx':
        extensions = {'.docx', '.doc'}
    elif file_type == 'pptx':
        extensions = {'.pptx', '.ppt'}
    else:  # 'all'
        extensions = {'.pdf', '.docx', '.doc', '.pptx', '.ppt'}
    
    # Collect files
    if recursive:
        # For recursive search, we need to check each file against gitignore
        for root, dirs, filenames in os.walk(directory):
            root_path = Path(root)
            
            # Filter directories based on gitignore patterns
            dirs_to_remove = []
            for d in dirs:
                dir_path = root_path / d
                if _should_ignore_file(dir_path, gitignore_patterns, directory):
                    dirs_to_remove.append(d)
            
            # Remove ignored directories
            for d in dirs_to_remove:
                dirs.remove(d)
            
            # Check files in this directory
            for filename in filenames:
                file_path = root_path / filename
                
                # Skip if file matches gitignore patterns
                if _should_ignore_file(file_path, gitignore_patterns, directory):
                    continue
                
                # Check if file has desired extension
                if file_path.suffix.lower() in extensions:
                    files.append(file_path)
    else:
        # Non-recursive search
        for ext in extensions:
            for file_path in directory.glob(f'*{ext}'):
                # Skip if file matches gitignore patterns
                if _should_ignore_file(file_path, gitignore_patterns, directory):
                    continue
                files.append(file_path)
    
    return sorted(files)


@app.command("extract")
def extract(
    input_path: Path = typer.Argument(
        ..., 
        help="Path to input file or directory",
        exists=True,
    ),
    output_file: Optional[Path] = typer.Option(
        None,
        "--output", "-o",
        help="Path to output markdown file (only for single file mode)",
    ),
    recursive: bool = typer.Option(
        False,
        "--recursive", "-r",
        help="Recursively process all files in directory and subdirectories",
    ),
    file_type: str = typer.Option(
        "all",
        "--file-type", "-t",
        help="Filter by file type: 'all', 'pdf', 'docx', or 'pptx'",
    ),
    text_only: bool = typer.Option(
        False,
        "--text-only", "--no-media",
        help="Extract text only, skip image extraction for faster/smaller output",
    ),
    workers: int = typer.Option(
        1,
        "--workers", "-w",
        help="Number of parallel workers for processing multiple files (default: 1, sequential)",
        min=1,
    ),
    quiet: bool = typer.Option(
        False,
        "--quiet", "-q",
        help="Suppress output messages",
    ),
):
    """
    [bold]Extract content from PDF, DOCX, or PPTX files and convert to markdown.[/bold]

    Can process a single file or an entire directory (with --recursive flag).

    The tool automatically detects file types and uses appropriate methods:
    • PDF files: Uses marker-pdf for high-quality markdown conversion
    • DOCX files: Uses python-docx to preserve formatting
    • PPTX files: Uses python-pptx to extract slides and content

    [bold]Examples:[/bold]
        [dim]# Single file[/dim]
        p3335 extract document.pdf
        p3335 extract presentation.pptx -o output.md

        [dim]# Text only (no images, faster)[/dim]
        p3335 extract document.pdf --text-only
        p3335 extract document.pdf --no-media

        [dim]# Directory (non-recursive)[/dim]
        p3335 extract ./documents/

        [dim]# Directory (recursive, all files)[/dim]
        p3335 extract ./documents/ --recursive

        [dim]# Directory (recursive, PDFs only)[/dim]
        p3335 extract ./documents/ -r --file-type pdf

        [dim]# Directory (recursive, PPTX only, text-only mode)[/dim]
        p3335 extract ./documents/ -r -t pptx --text-only

        [dim]# Parallel processing with 4 workers[/dim]
        p3335 extract ./documents/ -r --workers 4
        p3335 extract ./documents/ -r -w 4
    """
    try:
        # Validate file_type option
        if file_type not in ['all', 'pdf', 'docx', 'pptx']:
            console.print(f"[red]Error: Invalid file type '{file_type}'[/red]")
            console.print("[yellow]Valid options: all, pdf, docx, pptx[/yellow]")
            raise typer.Exit(code=1)
        
        # Determine extract_images based on text_only flag
        extract_images = not text_only
        
        if text_only:
            console.print("[dim]Text-only mode enabled: Images will not be extracted[/dim]")
        
        # Check if input is file or directory
        if input_path.is_file():
            # Single file mode
            if recursive:
                console.print("[yellow]Warning: --recursive flag ignored for single file[/yellow]")
            if file_type != 'all':
                console.print("[yellow]Warning: --file-type flag ignored for single file[/yellow]")
            
            if not input_path.exists():
                console.print(f"[red]Error: File '{input_path}' not found[/red]")
                raise typer.Exit(code=1)
            
            suffix = input_path.suffix.lower()
            if suffix not in ['.pdf', '.docx', '.doc', '.pptx', '.ppt']:
                console.print(f"[red]Error: Unsupported file type '{suffix}'[/red]")
                console.print("[yellow]Supported types: .pdf, .docx, .pptx[/yellow]")
                raise typer.Exit(code=1)
            
            success = _extract_single_file(input_path, output_file, extract_images, quiet)
            if success:
                console.print("[green]✅ Extraction complete![/green]")
            else:
                raise typer.Exit(code=1)
                
        elif input_path.is_dir():
            # Directory mode
            if output_file is not None:
                console.print("[yellow]Warning: --output flag ignored in directory mode[/yellow]")
            
            console.print(f"[bold]Scanning directory:[/bold] {input_path}")
            if recursive:
                console.print("[dim]Searching recursively...[/dim]")
            
            # Collect files
            files = _collect_files(input_path, recursive, file_type)
            
            if not files:
                console.print(f"[yellow]No matching files found ({file_type})[/yellow]")
                raise typer.Exit(code=0)
            
            console.print(f"[bold]Found {len(files)} file(s) to process[/bold]")
            if workers > 1:
                console.print(f"[dim]Using {workers} parallel workers[/dim]")
            console.print()
            
            # Process files with progress tracking
            successful = 0
            failed = 0
            skipped = 0
            failed_files = []  # Track failed files with their error messages
            
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.completed}/{task.total}"),
                console=console,
                transient=True,  # Clear progress bar after completion
            ) as progress:
                task = progress.add_task("Processing files...", total=len(files))
                
                if workers == 1:
                    # Sequential processing (original behavior)
                    for file_path in files:
                        progress.update(task, description=f"Processing {file_path.name}")
                        
                        success, error_msg = _extract_single_file(file_path, None, extract_images, quiet)
                        if success:
                            successful += 1
                        else:
                            failed += 1
                            failed_files.append((file_path, error_msg))
                        
                        progress.update(task, advance=1)
                else:
                    # Parallel processing
                    with ProcessPoolExecutor(max_workers=workers) as executor:
                        # Submit all tasks
                        future_to_file = {
                            executor.submit(
                                _extract_single_file, 
                                file_path, 
                                None, 
                                extract_images, 
                                True  # Force quiet mode for parallel to avoid output collisions
                            ): file_path
                            for file_path in files
                        }
                        
                        # Process completed tasks
                        for future in as_completed(future_to_file):
                            file_path = future_to_file[future]
                            try:
                                success, error_msg = future.result()
                                if success:
                                    successful += 1
                                else:
                                    failed += 1
                                    failed_files.append((file_path, error_msg))
                            except Exception as e:
                                failed += 1
                                error_msg = f"{type(e).__name__}: {str(e)}"
                                failed_files.append((file_path, error_msg))
                            
                            progress.update(task, advance=1)
            
            # Summary
            console.print()
            console.print("[bold]Summary:[/bold]")
            console.print(f"[green]✅ Successful:[/green] {successful}")
            if failed > 0:
                console.print(f"[red]❌ Failed:[/red] {failed}")
                if failed_files:
                    console.print()
                    console.print("[red][bold]❌ Failed files:[/bold][/red]")
                    for file_path, error_msg in failed_files:
                        console.print(f"  [red]• {file_path.name}:[/red] {error_msg}")
            if skipped > 0:
                console.print(f"  [yellow]⏭️ Skipped:[/yellow] {skipped}")
            
            if failed == 0:
                console.print()
                console.print("[green]✅ All files processed successfully![/green]")
            else:
                raise typer.Exit(code=1)
        else:
            console.print(f"[red]Error: '{input_path}' is neither a file nor directory[/red]")
            raise typer.Exit(code=1)
        
    except ImportError as e:
        console.print(f"[red]Missing dependency:[/red] {str(e)}")
        raise typer.Exit(code=1)
    except typer.Exit:
        raise
    except Exception as e:
        error_type = type(e).__name__
        console.print(f"[red]Error ({error_type}):[/red] {str(e)}")
        raise typer.Exit(code=1)


def main():
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
