OUTPUT = IEEE3335.pdf

# Try to find xelatex in PATH, then in the default macOS MacTeX install location, fallback to pdflatex
PDF_ENGINE ?= $(shell command -v xelatex 2>/dev/null || (test -x /Library/TeX/texbin/xelatex && echo "/Library/TeX/texbin/xelatex") || echo "pdflatex")

.PHONY: all clean $(OUTPUT)

all: $(OUTPUT)

$(OUTPUT):
	@echo "Gathering chapter files to build $(OUTPUT)..."
	@bash -c ' \
		FILES=() ; \
		while IFS= read -r line; do \
			FILES+=("$$line") ; \
		done < <(find . -maxdepth 2 -name "README.md" | grep -E "^\./([0-9]{2}|Annex)" | sort) ; \
		echo "Found files:" ; \
		for file in "$${FILES[@]}"; do echo "  $$file"; done ; \
		echo "Using PDF Engine: $(PDF_ENGINE)" ; \
		pandoc "$${FILES[@]}" -o $(OUTPUT) \
			--toc \
			--pdf-engine=$(PDF_ENGINE) \
			-V geometry:margin=1in \
			-V title="IEEE P3335 Standard" \
			-V author="IEEE-3335 Working Group" \
	'

clean:
	rm -f $(OUTPUT)



