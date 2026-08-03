OUTPUT = IEEE3335.pdf
METADATA = metadata.yaml
LINE_NUMBER_HEADER = latex/review-line-numbers.tex
FOOTER_HEADER = latex/review-footer.tex
LAYOUT_HEADER = latex/standards-layout.tex
TABLE_FILTER = scripts/ieee_table_layout.lua
LATEX_SCRATCH = *.aux *.log *.out *.toc
FIGURE_CONVERTER ?= $(shell command -v magick 2>/dev/null || command -v convert 2>/dev/null || true)
FIGURE_DENSITY ?= 72
FIGURE_SVGS := $(wildcard figures/*.svg)
FIGURE_PDFS := $(patsubst figures/%.svg,figures/rendered/%.pdf,$(FIGURE_SVGS))

# Try to find xelatex in PATH, then in the default macOS MacTeX install location, fallback to pdflatex
PDF_ENGINE ?= $(shell command -v xelatex 2>/dev/null || (test -x /Library/TeX/texbin/xelatex && echo "/Library/TeX/texbin/xelatex") || echo "pdflatex")

.PHONY: all check clean requirements $(OUTPUT)

all: $(OUTPUT)

requirements:
	python3 scripts/requirements_index.py

check:
	python3 scripts/check_draft.py
	python3 scripts/requirements_index.py --check
	python3 -m py_compile scripts/ieee_3335_tools/*.py scripts/check_python.py scripts/check_torch.py scripts/check_draft.py scripts/requirements_index.py

figures/rendered/%.pdf: figures/%.svg
	@if [ -z "$(FIGURE_CONVERTER)" ]; then \
		echo "No SVG-to-PDF converter found. Install ImageMagick or commit rendered figure PDFs."; \
		exit 1; \
	fi
	@mkdir -p figures/rendered
	@$(FIGURE_CONVERTER) -density $(FIGURE_DENSITY) "$<" "$@"

$(OUTPUT): $(METADATA) $(LINE_NUMBER_HEADER) $(FOOTER_HEADER) $(LAYOUT_HEADER) $(TABLE_FILTER) $(FIGURE_PDFS)
	@echo "Gathering chapter files to build $(OUTPUT)..."
	@bash -c ' \
		FILES=() ; \
		while IFS= read -r line; do \
			FILES+=("$$line") ; \
		done < <(find . -maxdepth 2 -name "README.md" | grep -E "^\./([0-9]{2}|Annex)" | LC_ALL=C sort) ; \
		echo "Found files:" ; \
		for file in "$${FILES[@]}"; do echo "  $$file"; done ; \
		echo "Using PDF Engine: $(PDF_ENGINE)" ; \
		pandoc "$${FILES[@]}" -o $(OUTPUT) \
			--toc \
			--toc-depth=3 \
			--metadata-file=$(METADATA) \
			--lua-filter=$(TABLE_FILTER) \
			--include-in-header=$(LAYOUT_HEADER) \
			--include-in-header=$(FOOTER_HEADER) \
			--include-in-header=$(LINE_NUMBER_HEADER) \
			--pdf-engine=$(PDF_ENGINE) \
			-V geometry:margin=1in ; \
		rm -f $(LATEX_SCRATCH) \
	'

clean:
	rm -f $(OUTPUT) $(LATEX_SCRATCH)
