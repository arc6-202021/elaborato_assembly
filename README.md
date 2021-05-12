# ELABORATO ASSEMBLY 2020/2021

Questo repository contiene i file relativi
all'elaborato assembly per architettura degli elaboratori (anno 2020/2021).

<br>

---

## Test Github Actions

|Badge|Descrizione|
|-----|-----------|
|[![Spellcheck](https://github.com/arc6-202021/elaborato_assembly/actions/workflows/spellcheck.yml/badge.svg)](https://github.com/arc6-202021/elaborato_assembly/actions/workflows/spellcheck.yml)|Verifica che lo spelling sia corretto sia nel README.md sia nella documentazione (verifica errori di battitura)|
|[![Relazione](https://github.com/arc6-202021/elaborato_assembly/actions/workflows/relazione.yml/badge.svg)](https://github.com/arc6-202021/elaborato_assembly/actions/workflows/relazione.yml)|Verifica che la build della documentazione sia andata a buon fine (artifact scaricabile da gh actions)|
|[![Unit tests](https://github.com/arc6-202021/elaborato_assembly/actions/workflows/unittests.yml/badge.svg)](https://github.com/arc6-202021/elaborato_assembly/actions/workflows/unittests.yml)|Si assicura che le singole funzioni assembly restituiscano il risultato atteso|

---

<br>

## Contenuto repository

I file presenti in questo repository sono:

* **.editorconfig**: dice agli editor che supportano questo file di configurazione
    come devono essere strutturati i file:
    > NOTA: per certi editor, come vscode, e' necessario scaricare un'estensione per attuare le configurazioni

    La configurazione impone:
    * End Of Line Linux (\n e non \r\n come vorrebbe Windows)
    * Tutti i file terminano con una riga vuota
    * Tutti gli spazi a fine riga vengono automaticamente rimossi
    * Tutte le spaziature nel file ```Makefile``` verranno convertite in tab
    * Tutte le altre spaziature nei file markdown, json, assembly, C, C header, ... Verranno convertite in spazi (un'indentazione sono 4 spazi)
    * Il set di caratteri dei file elencati qui sopra sono UTF-8

* **.gitattributes**: dice a git di forzare il EOF Linux (\n e non \r\n come vorrebbe Windows) per i file di testo

* **.gitignore**: dice a git di non tracciare alcuni file
    > Vengono ignorati:
    > * i file post-build della relazione/documentazione
    > * il file spellcheck.tmp, creato da ```spellcheck.sh``` quando ci sono errori di spelling nella documentazione
    >   (contiene questi errori di spelling)

* **Makefile**: file eseguito da ```make```, utility che esegue comandi che eseguono le build delle varie componenti del progetto
    > Per utilizzare il file eseguire il comando ```make``` seguito da uno dei seguenti parametri:
    >
    > * **make help**: visualizza questa lista dei possibili parametri
    >
    > COMPATIBILI SOLO CON LINUX/MAC OS:
    > * **make Relazione.pdf**: esegue la build della documentazione con pdflatex
    > * **make watch_relazione**: esegue la build della documentazione automaticamente dopo ogni modifica ai file .tex
    >
    >       NOTA: e' necessario installare when-changed con pip:
    >       pip install https://github.com/joh/when-changed/archive/master.zip
    >
    > * **make spellcheck**: controlla se ci sono errori di spelling nella documentazione
    >
    >       NOTA: e' necessario installare hunspell
    > * **make clean**: cancella la cartella build della documentazione
    >
    >  COMPATIBILI SOLO CON WINDOWS:
    > * **make relazione_win**: esegue la build della documentazione con pdflatex
    > * **make watch_relazione_win**: esegue la build della documentazione automaticamente dopo ogni modifica al file Relazione.tex
    >
    >       NOTA: e' necessario installare when-changed con pip:
    >       pip install https://github.com/joh/when-changed/archive/master.zip
    >
    >       NOTA 2: la flag ricorsiva sembra avere un bug e
    >       quindi le modifiche vengono riconosciute solo per il file principale
    >
    >       NOTA 3: anche un Ctrl+S viene considerato "file modificato"
    >
    > * **make spellcheck**: controlla se ci sono errori di spelling nella documentazione
    >
    >       NOTA: e' necessario installare hunspell (per Windows esiste la versione "ezwinports")
    >
    > * **make clean_win**: cancella la cartella build della documentazione

* **README.md**: questo file...

* **spellcheck.sh**: script bash che usa hunspell per verificare se ci sono errori di spelling nei file della documentazione
    > E' possibile eseguirlo eseguendo il comando ```./spellcheck.sh``` oppure ```make spellcheck```.
    >
    > NOTA: lo script puo' funzionare su Windows grazie a MINGW64...
    > E' pero' consigliabile installare hunspell versione "ezwinports"
    > e poi eseguire il comando ```make spellcheck_win```

Le cartelle presenti in questo repository sono:

* **.vscode**: contiene il file ```settings.json``` che dice alla estensione "latex-workshop" per Visual Studio Code di non creare automaticamente il PDF ogni volta che si salvano file .tex
    > Questo perche' il ```Makefile``` si occupera' di questo compito

* **docs**: contiene i sorgenti della documentazione scritta in LaTeX
    > Per eseguire la build della documentazione eseguire il comando ```make Relazione.pdf``` su Linux/Mac OS
    > oppure ```make relazione_win``` su Windows. La relazione compilata apparira' nella cartella ```docs_build``` nella root del repository.
    >
    > NOTA: e' necessario aver installato LaTeX sul computer (il comando ```pdflatex``` deve essere richiamabile da ```make```)
    >
    > NOTA 2: Gli autori vengono recuperati da 3 variabili d'ambiente (```asm_rel_author1```, ```asm_rel_author2``` e ```asm_rel_author3```).
    >Se una/piu' di queste variabili non vengono impostate, "valgono" come una stringa vuota.
    >
    > Esempio:
    > * se non vengono impostate, l'autore non e' specificato
    > * se viene specificato solo che ```asm_rel_author1``` e' "Mario Rossi (matricola 123)"
    > allora lui e' l'unico autore (apparira' nella prima pagina con il titolo)
    > * con due autori vengono visualizzati entrambe su due righe diverse
    > * stessa cosa vale per tutti e 3 gli autori specificati

    * la cartella **sections** contiene le sezioni della documentazione (nel corso del progetto tutto verra' scritto su questi file)

    * il file **Relazione.tex** e' un file di "configurazione" per la documentazione: imposta
    la lingua italiana, richiama le estensioni necessarie, definisce la pagina con il titolo e importa i file delle sezioni.

* **tests** contiene i file di test
    * la cartella **hunspell** contiene i dizionari necessari per verificare se ci sono errori di spelling
        > Questi file vengono usati da hunspell quando vengono eseguiti i comandi "```make spellcheck```", "```make spellcheck_win```" e "```./spellcheck.sh```"
