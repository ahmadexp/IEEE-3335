"""CLI interface for IEEE-3335 tools."""

import typer
from pathlib import Path
from typing import Optional, List
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn

from .pdf_extractor import extract_pdf_to_markdown
from .docx_extractor import extract_docx_to_markdown
from .pptx_extractor import extract_pptx_to_markdown

# Configure console with better width for help text
import shutil
terminal_width = shutil.get_terminal_size().columns
console = Console(width=max(terminal_width, 100))  # Responsive width, min 100

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
    extract_images: bool = True
) -> bool:
    """
    Extract a single file to markdown.
    
    Args:
        input_file: Path to input file
        output_file: Optional output path
        extract_images: Whether to extract images
        
    Returns:
        True if successful, False otherwise
    """
    try:
        suffix = input_file.suffix.lower()
        
        if suffix == '.pdf':
            extract_pdf_to_markdown(input_file, output_file, extract_images)
        elif suffix in ['.docx', '.doc']:
            if suffix == '.doc':
                console.print("[yellow]Warning: .doc files may not be fully supported.[/yellow]")
            extract_docx_to_markdown(input_file, output_file, extract_images)
        elif suffix in ['.pptx', '.ppt']:
            if suffix == '.ppt':
                console.print("[yellow]Warning: .ppt files may not be fully supported. Consider converting to .pptx first.[/yellow]")
            extract_pptx_to_markdown(input_file, output_file, extract_images)
        else:
            return False
        
        return True
        
    except Exception as e:
        error_type = type(e).__name__
        console.print(f"[red]Error processing {input_file.name} ({error_type}):[/red] {str(e)}")
        return False


def _collect_files(
    directory: Path, 
    recursive: bool, 
    file_type: str
) -> List[Path]:
    """
    Collect files from directory based on criteria.
    
    Args:
        directory: Directory to search
        recursive: Whether to search recursively
        file_type: Filter by type ('all', 'pdf', 'docx', 'pptx')
        
    Returns:
        List of matching file paths
    """
    files = []
    
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
        for ext in extensions:
            files.extend(directory.rglob(f'*{ext}'))
    else:
        for ext in extensions:
            files.extend(directory.glob(f'*{ext}'))
    
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
            
            success = _extract_single_file(input_path, output_file, extract_images)
            if success:
                console.print("[green]✓ Extraction complete![/green]")
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
            console.print()
            
            # Process files with progress tracking
            successful = 0
            failed = 0
            skipped = 0
            
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.completed}/{task.total}"),
                console=console,
            ) as progress:
                task = progress.add_task("Processing files...", total=len(files))
                
                for file_path in files:
                    progress.update(task, description=f"Processing {file_path.name}")
                    
                    success = _extract_single_file(file_path, None, extract_images)
                    if success:
                        successful += 1
                    else:
                        failed += 1
                    
                    progress.update(task, advance=1)
            
            # Summary
            console.print()
            console.print("[bold]Summary:[/bold]")
            console.print(f"  [green]✓ Successful:[/green] {successful}")
            if failed > 0:
                console.print(f"  [red]✗ Failed:[/red] {failed}")
            if skipped > 0:
                console.print(f"  [yellow]⊘ Skipped:[/yellow] {skipped}")
            
            if failed == 0:
                console.print()
                console.print("[green]✓ All files processed successfully![/green]")
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
