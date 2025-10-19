# IEEE-3335 Tools

Command-line tools for working with IEEE-3335 documents. Extract and convert PDF, DOCX, and PPTX files to markdown with ease.

## Features

- **PDF to Markdown**: Uses `marker-pdf` for high-quality PDF extraction with preserved formatting, tables, equations, and images
- **DOCX to Markdown**: Uses `python-docx` to convert Word documents while preserving headings, formatting, and tables
- **PPTX to Markdown**: Uses `python-pptx` to extract slide content, notes, and images from presentations
- **Image Extraction**: Automatically extracts and saves images to a separate folder (optional)
- **Text-Only Mode**: Skip image extraction with `--text-only` or `--no-media` for faster processing and smaller output
- **Automatic Detection**: Automatically detects file type and uses the appropriate converter
- **Batch Processing**: Process entire directories recursively with file type filtering
- **Rich CLI**: Beautiful command-line interface with progress indicators

## Requirements

- Python >=3.10
- ~2GB disk space for ML models (downloaded automatically on first PDF conversion)
- GPU recommended but not required (CPU and Apple MPS also supported)

## Installation

### Development Mode

Install the package in editable mode for development:

```bash
# From the scripts directory
cd scripts
uv sync
```

### User Installation

Install it to your user site-packages:

```bash
cd scripts
uv tool install .
```

## Usage

You can use either `ieee-3335-tools` or the shorter alias `p3335`.

**For development mode** (recommended), prefix commands with `uv run`:

```bash
# From the scripts directory
uv run p3335 extract ../document.pdf
```

**For user installation**, use directly:

```bash
ieee-3335-tools extract document.pdf
# or
p3335 extract document.pdf
```

### Extract Command

The `extract` command can process individual files or entire directories (recursively). It automatically detects file types and converts them to markdown.

#### Extract Single File

##### PDF Files

```bash
# Basic usage - creates document.md in the same directory as the PDF
uv run p3335 extract ../document.pdf

# With custom output file
uv run p3335 extract ../document.pdf --output output.md

# Using short flag
uv run p3335 extract ../document.pdf -o output.md
```

**⏱️ Expected Behavior - First Run:**

When you run PDF extraction for the first time, you'll see:

1. **Model Download Phase** (~2-5 minutes depending on connection):
   ```
   Converting PDF to Markdown: document.pdf
   Loading marker-pdf models (this may take a moment on first run)...
   Downloading model.safetensors: 0%|          | 0/1.35G [00:00<?, ?B/s]
   ```
   The tool downloads several ML models totaling ~1-1.5GB. This happens only once.

2. **Conversion Phase** (varies by document size):
   - The tool will process each page
   - You'll see progress indicators
   - Typical speed: 1-3 pages/second on CPU, faster on GPU

**⚡ Expected Behavior - Subsequent Runs:**

After models are cached, conversions start immediately with no download phase.

##### DOCX Files

```bash
# Basic usage - creates document.md
uv run p3335 extract ../document.docx

# With custom output file
uv run p3335 extract ../document.docx -o output.md
```

**⏱️ Expected Behavior:**

DOCX conversion is fast and doesn't require any model downloads:
- Starts immediately
- Completes in seconds for most documents
- Preserves headings, bold/italic formatting, and tables

##### PPTX Files

```bash
# Basic usage - creates presentation.md
uv run p3335 extract ../presentation.pptx

# With custom output file
uv run p3335 extract ../presentation.pptx -o output.md
```

**⏱️ Expected Behavior:**

PPTX conversion is fast and extracts slide-by-slide:
- Starts immediately
- Completes in seconds for most presentations
- Extracts slide titles, content, and images
- Images saved to `{filename}_images/` directory
- Each slide becomes a markdown section

#### Text-Only Mode

Use `--text-only` or `--no-media` to skip image extraction for faster processing:

```bash
# PDF without images (much faster)
uv run p3335 extract document.pdf --text-only

# PPTX without images
uv run p3335 extract presentation.pptx --no-media

# Batch processing without images
uv run p3335 extract ./documents/ -r --text-only
```

**Benefits of Text-Only Mode:**
- **⚡ Faster processing**: Skip image extraction and encoding
- **💾 Smaller output**: No image files or directories created
- **📄 Pure text**: Focus on textual content only
- **🔄 Batch friendly**: Process large directories more quickly

#### Extract Directory (Batch Processing)

Process multiple files at once by pointing to a directory:

```bash
# Process all files in current directory (non-recursive)
uv run p3335 extract ./documents/

# Process all files recursively
uv run p3335 extract ./documents/ --recursive

# Short form
uv run p3335 extract ./documents/ -r
```

**🔍 Gitignore Awareness:** The tool automatically respects `.gitignore` files found in the search directory and its parent directories. Files and directories matching gitignore patterns will be excluded from processing.

##### Filter by File Type

Use the `--file-type` (or `-t`) flag to process only specific file types:

```bash
# Process only PDF files recursively
uv run p3335 extract ./documents/ -r --file-type pdf

# Process only DOCX files recursively
uv run p3335 extract ./documents/ -r -t docx

# Process only PPTX files recursively
uv run p3335 extract ./documents/ -r -t pptx

# Process all supported files (default)
uv run p3335 extract ./documents/ -r -t all

# Combine with text-only mode
uv run p3335 extract ./documents/ -r -t pptx --text-only
```

**⏱️ Expected Behavior - Batch Processing:**

When processing directories:
1. **Scanning Phase**: Lists all matching files
2. **Processing Phase**: Shows progress bar with current file
3. **Summary**: Reports successful, failed, and skipped files

Example output:
```
Scanning directory: ./documents/
Searching recursively...
Found 15 file(s) to process

⠋ Processing report.pdf ━━━━━━━━━━━━━━━━━━ 8/15

Summary:
  ✓ Successful: 14
  ✗ Failed: 1

```

**Notes on Batch Processing:**
- Output files are created in the same directory as source files
- Failed files don't stop the entire batch
- Use `--file-type` to avoid processing unnecessary files
- Progress bar shows current file being processed

## Project Structure

```
scripts/
├── ieee_3335_tools/          # Main package
│   ├── __init__.py          # Package initialization
│   ├── cli.py               # CLI interface with batch processing
│   ├── pdf_extractor.py     # PDF extraction logic (marker-pdf)
│   ├── docx_extractor.py    # DOCX extraction logic (python-docx)
│   └── pptx_extractor.py    # PPTX extraction logic (python-pptx)
├── pyproject.toml           # Project configuration and dependencies
├── uv.lock                  # Locked dependencies
└── README.md                # This file
```

## Troubleshooting

### "Missing dependency: marker-pdf is not installed"

If you see this error but `marker-pdf` is installed, the API may have changed. Ensure you're using marker-pdf 1.10.1+ with the correct imports:

```bash
# Check version
uv pip list | grep marker-pdf

# Should show: marker-pdf  1.10.1 or higher
```

### First PDF conversion is slow

This is expected! The first conversion downloads ~1-1.5GB of ML models. Subsequent conversions will be much faster.

### Out of memory errors

For very large PDFs on systems with limited RAM:
- Close other applications
- Process smaller page ranges if needed
- Consider using a system with more RAM or a GPU

## Technical Details

The project uses:
- **marker-pdf (1.10.1+)**: ML-based PDF to markdown with OCR, layout detection, and table extraction
- **python-docx**: DOCX parsing and structure extraction
- **python-pptx**: PPTX parsing and slide content extraction
- **Pillow**: Image handling and manipulation
- **typer**: Modern CLI interface with type hints
- **rich**: Beautiful terminal output with progress bars
- **pypdfium2**: Low-level PDF operations

### ML Models Used by marker-pdf

On first PDF conversion, marker-pdf downloads several specialized models:
- Layout detection model
- OCR model (Surya)
- Table detection model
- Equation recognition model

These are cached in `~/.cache/huggingface/` and reused for all future conversions.

## Notes

- **🕐 First PDF conversion**: Expect 2-5 minute delay for model downloads (~1-1.5GB). This only happens once.
- **💾 Subsequent conversions**: Start immediately using cached models.
- **⚡ DOCX/PPTX conversion**: Fast, no model download required.
- **📄 .doc files**: Limited support. Convert to .docx first for best results.
- **📄 .ppt files**: Limited support. Convert to .pptx first for best results.
- **🖼️ Image extraction**: Images saved to `{filename}_images/` directory by default.
- **📝 Text-only mode**: Use `--text-only` or `--no-media` to skip images for faster processing.
- **📁 Output location**: Defaults to same directory and name as input with .md extension.
- **🖥️ GPU acceleration**: Automatically detected and used if available (CUDA, MPS).
- **📂 Batch processing**: Process entire directories recursively with `--recursive` flag.
- **🔍 File filtering**: Use `--file-type` to process only PDFs, DOCX, or PPTX files.
- **🔍 Gitignore awareness**: Automatically respects `.gitignore` files in search paths - ignored files are excluded from processing.
