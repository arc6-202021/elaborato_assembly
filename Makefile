#
# MAKEFILE
# --------
#
# Eseguendo il comando make in questa directory
# vengono visualizzati i parametri accettati.
#
# PARAMETRI:
# * make help: visualizza questa lista dei possibili parametri
#
#  COMPATIBILI SOLO CON LINUX/MAC OS:
# * make Relazione.pdf: esegue la build della documentazione con pdflatex
# * make watch_relazione: esegue la build della documentazione automaticamente dopo ogni modifica ai file .tex
#        NOTA: e' necessario installare when-changed con pip: pip install https://github.com/joh/when-changed/archive/master.zip
# * make spellcheck: controlla se ci sono errori di spelling nella documentazione
#        NOTA: e' necessario installare hunspell
# * make clean: cancella la cartella build della documentazione
#
#  COMPATIBILI SOLO CON WINDOWS:
# * make relazione_win: esegue la build della documentazione con pdflatex
# * make watch_relazione_win: esegue la build della documentazione automaticamente dopo ogni modifica al file Relazione.tex
#        NOTA: e' necessario installare when-changed con pip: pip install https://github.com/joh/when-changed/archive/master.zip
#        NOTA 2: la flag ricorsiva sembra avere un bug e quindi le modifiche vengono riconosciute solo per il file principale
#        NOTA 3: anche un Ctrl+S viene considerato "file modificato"
# * make spellcheck: controlla se ci sono errori di spelling nella documentazione
#        NOTA: e' necessario installare hunspell (per Windows esiste la versione "ezwinports")
# * make clean_win: cancella la cartella build della documentazione

# crea in questa cartella una cartella "docs_build" con la documentazione in formato PDF
build_docs_cmd = pdflatex -interaction=nonstopmode --output-dir=../docs_build --shell-escape Relazione.tex


.PHONY: help
help:
	@echo "MAKEFILE"
	@echo "--------"
	@echo "Eseguire make con i seguenti parametri:"
	@echo "* make help: visualizza questa lista dei possibili parametri"
	@echo "COMPATIBILI SOLO CON LINUX/MAC OS:"
	@echo "* make Relazione.pdf: esegue la build della documentazione con pdflatex (Linux/Mac OS)"
	@echo "* make watch_relazione: esegue la build della documentazione automaticamente dopo ogni modifica ai file .tex"
	@echo "       NOTA: e' necessario installare when-changed con pip: pip install https://github.com/joh/when-changed/archive/master.zip"
	@echo "* make spellcheck: controlla se ci sono errori di spelling nella documentazione"
	@echo "       NOTA: e' necessario installare hunspell"
	@echo "* make clean: cancella la cartella build della documentazione (Linux/Mac OS)"
	@echo "COMPATIBILI SOLO CON WINDOWS:"
	@echo "* make relazione_win: esegue la build della documentazione con pdflatex (Windows)"
	@echo "* make clean_win: cancella la cartella build della documentazione (Windows)"


# -- LINUX / MAC OS

Relazione.pdf:
	# crea la cartella per la build della documentazione
	mkdir -p docs_build

	# Crea la TOC
	cd docs && $(build_docs_cmd)
	# Crea la relazione con la TOC
	cd docs && $(build_docs_cmd)

	# tenta di avviare il browser preferito con il pdf aperto
	sensible-browser file://$(shell pwd)/docs_build/Relazione.pdf || echo ""

.PHONY: watch_relazione
watch_relazione:
	# crea la cartella per la build della documentazione
	mkdir -p docs_build

	# assicurati che almeno una build e' gia' stata effettuata
	cd docs && $(build_docs_cmd) && $(build_docs_cmd)

	# tenta di avviare il browser preferito con il pdf aperto
	sensible-browser file://$(shell pwd)/docs_build/Relazione.pdf || echo ""

	# crea la cartella per la build della documentazione
	mkdir -p docs_build

	# controlla se i file nella cartella docs vengono modificati:
	# se vengono modificati esegui la build della documentazione 2 volte (una per la TOC e una per il PDF)
	cd docs && when-changed -r . "$(build_docs_cmd) && $(build_docs_cmd)"

.PHONY: spellcheck
spellcheck:
	./spellcheck.sh

.PHONY: clean
clean:
	rm -r docs_build


# -- WINDOWS

.PHONY: relazione_win
relazione_win:
	@: # crea cartella build
	if not exist "docs_build" mkdir docs_build

	@: # esegui la build
	cd docs && $(build_docs_cmd) && $(build_docs_cmd)

	@: # tenta di avviare il browser preferito con il pdf aperto
	explorer "file:///%CD%\docs_build\Relazione.pdf" || echo ""

.PHONY: watch_relazione_win
watch_relazione_win:
	@: # crea cartella build della documentazione
	if not exist "docs_build" mkdir docs_build

	@: # assicurati che almeno una build e' gia' stata effettuata
	cd docs && $(build_docs_cmd) && $(build_docs_cmd)

	@: # tenta di avviare il browser preferito con il pdf aperto
	explorer "file:///%CD%\docs_build\Relazione.pdf" || echo ""

	@: # controlla se il file Relazione.tex viene modificato:
	@: # se viene modificato esegui la build della documentazione 2 volte (una per la TOC e una per il PDF)
	cd docs && when-changed Relazione.tex pdflatex --output-dir=../docs_build --shell-escape Relazione.tex

.PHONY: spellcheck_win
spellcheck_win:
	forfiles /S /M "*.tex" /C "cmd /C echo @PATH && hunspell -l -u -d %CD%\tests\hunspell\en-GB,%CD%\tests\hunspell\it_IT,%CD%\tests\hunspell\custom_dict,%CD%\tests\hunspell\custom_dict_win @PATH"
	@echo "NOTA: SE VENGONO VISUALIZZATI SOLO I PERCORSI TUTTO E' CORRETTO"

.PHONY: clean_win
clean_win:
	@: # elimina cartella build della documentazione
	if exist "docs_build" RMDIR /S /Q docs_build
