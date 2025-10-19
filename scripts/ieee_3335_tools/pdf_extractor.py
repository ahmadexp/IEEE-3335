"""PDF extraction and conversion utilities."""

import io
from pathlib import Path
from typing import Optional

from PIL import Image

# Import shared console from package
from . import console

# Global variable to cache models
_models_cache = None

def _get_models():
    """Get or load marker-pdf models, caching them globally."""
    global _models_cache
    if _models_cache is None:
        console.print("[dim]Loading marker-pdf models (this may take a moment on first run)...[/dim]")
        from marker.models import create_model_dict
        _models_cache = create_model_dict()
        console.print("[green]✅ Models loaded and cached[/green]")
    return _models_cache


def extract_text_from_pdf_simple(pdf_path: Path) -> str:
    """Extract raw text from PDF using pypdfium2."""
    import pypdfium2
    
    pdf = pypdfium2.PdfDocument(str(pdf_path))
    text = ""
    total_pages = len(pdf)
    
    # Simple progress indication without progress bar to avoid interference
    for page_num in range(total_pages):
        if page_num % 10 == 0:  # Show progress every 10 pages
            console.print(f"[dim]Processing page {page_num + 1}/{total_pages}...[/dim]")
        
        page = pdf[page_num]
        text += f"--- Page {page_num + 1} ---\n"
        textpage = page.get_textpage()
        text_content = textpage.get_text_bounded()
        text += text_content + "\n\n"
        # Clean up resources
        textpage.close()
        page.close()
    
    return text


def extract_pdf_to_markdown(
    pdf_path: Path, 
    output_path: Optional[Path] = None,
    extract_images: bool = True,
    quiet: bool = False
) -> Path:
    """
    Extract PDF to markdown using marker-pdf.
    
    Args:
        pdf_path: Path to input PDF file
        output_path: Optional output path (default: {input_name}.md)
        extract_images: Whether to extract and save images
        quiet: Whether to suppress individual file output messages
        
    Returns:
        Path to the created markdown file
    """
    try:
        from marker.config.parser import ConfigParser
        from marker.converters.pdf import PdfConverter
        from marker.output import text_from_rendered
    except ImportError as e:
        raise ImportError(
            f"marker-pdf is not installed correctly: {e}\nPlease install it with: uv add marker-pdf"
        )
    
    if output_path is None:
        output_path = pdf_path.with_suffix('.md')
    
    if not quiet:
        console.print(f"[bold]Converting PDF to Markdown:[/bold] {pdf_path}")
        if not extract_images:
            console.print("[dim]Text-only mode: Images will not be extracted[/dim]")
    
    # Get cached models (loads only once globally per process)
    models = _get_models()
    
    # Configure converter
    config = {
        "disable_image_extraction": not extract_images,
        "output_format": "markdown"  # Explicitly set output format
    }
    config_parser = ConfigParser(config)
    
    # Create converter with cached models
    converter = PdfConverter(
        config=config_parser.generate_config_dict(),
        artifact_dict=models,
        renderer=config_parser.get_renderer()
    )
    
    # Convert PDF
    rendered = converter(str(pdf_path))
    
    # Extract text and images
    text, _, images = text_from_rendered(rendered)
    
    # Write output
    output_path.write_text(text, encoding='utf-8')
    if not quiet:
        console.print(f"[green]✅ Successfully converted to markdown:[/green] {output_path}")
    
    # Save images if extracted
    if extract_images and images:
        images_dir = output_path.parent / f"{output_path.stem}_images"
        images_dir.mkdir(exist_ok=True)
        
        image_count = 0
        failed_images = []
        
        for filename, image_data in images.items():
            try:
                image_path = images_dir / filename
                
                # Handle both PIL Images and bytes
                if isinstance(image_data, Image.Image):
                    # Convert PIL Image to bytes
                    buffer = io.BytesIO()
                    # Determine format from filename extension
                    image_format = image_path.suffix[1:].upper()
                    if image_format == 'JPG':
                        image_format = 'JPEG'
                    image_data.save(buffer, format=image_format)
                    image_bytes = buffer.getvalue()
                    image_path.write_bytes(image_bytes)
                else:
                    # Assume it's already bytes
                    image_path.write_bytes(image_data)
                
                image_count += 1
            except Exception as e:
                failed_images.append((filename, str(e)))
                if not quiet:
                    console.print(f"[yellow]⚠️  Failed to save image {filename}: {e}[/yellow]")
        
        if not quiet:
            if image_count > 0:
                console.print(f"[green]✅ Extracted {image_count} image(s) to:[/green] {images_dir}")
            if failed_images:
                console.print(f"[yellow]⚠️  Failed to extract {len(failed_images)} image(s)[/yellow]")
    
    return output_path
