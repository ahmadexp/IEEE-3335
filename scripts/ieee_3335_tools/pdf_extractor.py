"""PDF extraction and conversion utilities."""

from pathlib import Path
from typing import Optional
from rich.console import Console
from rich.progress import Progress, TextColumn, BarColumn, TaskProgressColumn

console = Console()


def extract_text_from_pdf_simple(pdf_path: Path) -> str:
    """Extract raw text from PDF using pypdfium2."""
    import pypdfium2
    
    pdf = pypdfium2.PdfDocument(str(pdf_path))
    text = ""
    total_pages = len(pdf)
    
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=None),
        TaskProgressColumn(),
        TextColumn("•"),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%", style="progress.percentage"),
        console=console,
        transient=True
    ) as progress:
        task = progress.add_task("Extracting pages...", total=total_pages)
        for page_num in range(total_pages):
            progress.update(task, description=f"Extracting page {page_num + 1}/{total_pages}")
            page = pdf[page_num]
            text += f"--- Page {page_num + 1} ---\n"
            textpage = page.get_textpage()
            text_content = textpage.get_text_bounded()
            text += text_content + "\n\n"
            # Clean up resources
            textpage.close()
            page.close()
            progress.update(task, advance=1)
    return text


def extract_pdf_to_markdown(
    pdf_path: Path, 
    output_path: Optional[Path] = None,
    extract_images: bool = True
) -> Path:
    """
    Extract PDF to markdown using marker-pdf.
    
    Args:
        pdf_path: Path to input PDF file
        output_path: Optional output path (default: {input_name}.md)
        extract_images: Whether to extract and save images
        
    Returns:
        Path to the created markdown file
    """
    try:
        from marker.converters.pdf import PdfConverter
        from marker.models import create_model_dict
        from marker.output import text_from_rendered
        from marker.config.parser import ConfigParser
    except ImportError as e:
        raise ImportError(
            f"marker-pdf is not installed correctly: {e}\nPlease install it with: uv add marker-pdf"
        )
    
    if output_path is None:
        output_path = pdf_path.with_suffix('.md')
    
    console.print(f"[bold]Converting PDF to Markdown:[/bold] {pdf_path}")
    if not extract_images:
        console.print("[dim]Text-only mode: Images will not be extracted[/dim]")
    console.print("[dim]Loading marker-pdf models (this may take a moment on first run)...[/dim]")
    
    # Configure converter
    config = {
        "disable_image_extraction": not extract_images
    }
    config_parser = ConfigParser(config)
    
    # Create converter with models
    converter = PdfConverter(
        config=config_parser.generate_config_dict(),
        artifact_dict=create_model_dict(),
        renderer=config_parser.get_renderer()
    )
    
    # Convert PDF
    rendered = converter(str(pdf_path))
    
    # Extract text and images
    text, _, images = text_from_rendered(rendered)
    
    # Write output
    output_path.write_text(text, encoding='utf-8')
    
    # Save images if extracted
    if extract_images and images:
        images_dir = output_path.parent / f"{output_path.stem}_images"
        images_dir.mkdir(exist_ok=True)
        
        image_count = 0
        for filename, image_data in images.items():
            image_path = images_dir / filename
            image_path.write_bytes(image_data)
            image_count += 1
        
        console.print(f"[green]✓ Successfully converted to markdown:[/green] {output_path}")
        console.print(f"[green]✓ Extracted {image_count} image(s) to:[/green] {images_dir}")
    else:
        console.print(f"[green]✓ Successfully converted to markdown:[/green] {output_path}")
    
    return output_path
