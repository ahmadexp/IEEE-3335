# Builds main.pdf from paper.md (pandoc -> IEEEtran LaTeX -> latexmk).

PANDOC   ?= pandoc
LATEXMK  ?= latexmk
BUILDDIR := build
FIGURE_BUILDDIR := $(BUILDDIR)/figures
FIGURE_TEX := figures/architecture-context.tex
FIGURE_PDF := figures/architecture-context.pdf

SOURCES := paper.md references.bib $(FIGURE_TEX) $(FIGURE_PDF)

.PHONY: all pdf tex watch clean distclean

all: main.pdf

pdf: main.pdf

main.pdf: $(BUILDDIR)/main.pdf
	cp $< $@

$(BUILDDIR)/main.pdf: $(BUILDDIR)/main.tex references.bib $(FIGURE_PDF)
	cd $(BUILDDIR) && TEXINPUTS=..: BIBINPUTS=..: $(LATEXMK) -pdf -interaction=nonstopmode main.tex

$(FIGURE_PDF): $(FIGURE_TEX)
	mkdir -p $(FIGURE_BUILDDIR)
	$(LATEXMK) -pdf -interaction=nonstopmode -halt-on-error \
		-outdir=$(FIGURE_BUILDDIR) $(FIGURE_TEX)
	cp $(FIGURE_BUILDDIR)/architecture-context.pdf $(FIGURE_PDF)

$(BUILDDIR)/main.tex: paper.md
	mkdir -p $(BUILDDIR)
	$(PANDOC) paper.md --standalone --natbib -V 'natbiboptions=numbers,sort&compress' -o $@

# Generated LaTeX only, for inspection or journal submission.
tex: $(BUILDDIR)/main.tex

# Rebuild automatically on source changes (requires fswatch: brew install fswatch).
watch: main.pdf
	fswatch -o $(SOURCES) | while read _; do $(MAKE) main.pdf; done

clean:
	rm -rf $(BUILDDIR)
	rm -f main.aux main.bbl main.blg main.log main.out main.fls main.fdb_latexmk

distclean: clean
	rm -f main.pdf
