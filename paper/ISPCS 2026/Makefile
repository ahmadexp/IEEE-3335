# Builds main.pdf from paper.md (pandoc -> IEEEtran LaTeX -> latexmk).

PANDOC   ?= pandoc
LATEXMK  ?= latexmk
BUILDDIR := build

SOURCES := paper.md references.bib figures/architecture-context.pdf

.PHONY: all pdf tex watch clean distclean

all: main.pdf

pdf: main.pdf

main.pdf: $(BUILDDIR)/main.pdf
	cp $< $@

$(BUILDDIR)/main.pdf: $(BUILDDIR)/main.tex references.bib
	cd $(BUILDDIR) && TEXINPUTS=..: BIBINPUTS=..: $(LATEXMK) -pdf -interaction=nonstopmode main.tex

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
