# ELABORATO ASSEMBLY 2020/2021

Questo repository contiene i file relativi
all'elaborato assembly per architettura degli elaboratori (anno 2020/2021).

<br>

---

## Test Github Actions

|Badge|Descrizione|
|-----|-----------|
|[![Unit tests](https://github.com/arc6-202021/elaborato_assembly/actions/workflows/unittests.yml/badge.svg)](https://github.com/arc6-202021/elaborato_assembly/actions/workflows/unittests.yml)|Si assicura che le singole funzioni assembly restituiscano il risultato atteso|
|[![Prototype test](https://github.com/arc6-202021/elaborato_assembly/actions/workflows/prototype_test.yml/badge.svg)](https://github.com/arc6-202021/elaborato_assembly/actions/workflows/prototype_test.yml)|Verifica il funzionamento dei prototipi scritti in Python|
|[![E2E tests](https://github.com/arc6-202021/elaborato_assembly/actions/workflows/e2e_tests.yml/badge.svg)](https://github.com/arc6-202021/elaborato_assembly/actions/workflows/e2e_tests.yml)|Si assicura che l'eseguibile postfix restituisca il risultato atteso lato end user|

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

* **.gitattributes**: dice a git di forzare il EOL Linux (\n e non \r\n come vorrebbe Windows) per i file di testo

* **.gitignore**: dice a git di non tracciare alcuni file
    > Vengono ignorati i file oggetto e binari ottenuti da codice C + assembly

* **LICENSE.txt**: file della licenza MIT

* **README.md**: questo file...

Le cartelle presenti in questo repository sono:

* **.github**: contiene file di configurazione per dependabot (verifica che le dipendenze dei software siano aggiornate) e per Github actions (nella cartella workflows sono presenti le varie configurazioni dei test descritti nella sezione "Test Github Actions")

* **code**: contiene tutto il codice del progetto (sia prototipi in Python sia il progetto finito in C+assembly)

* **docs**: contiene la documentazione

* **tests** contiene i file di test
    * la cartella **unit_test** contiene i sorgenti C necessari per compilare le singole funzioni assembly che compongono il progetto
    per poterle testare
    * la cartella **e2e_tests** contiene i file di input e di output atteso dell'intero programma. Sono i test finale che "simulano" l'uso da parte dell'utente
