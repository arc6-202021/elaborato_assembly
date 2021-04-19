# TESTS

Contiene i file di test del progetto.

* **SPELLING**: la cartella **hunspell** contiene i file dizionario con le parole accettate da hunspell,
  usato per assicurarsi che non ci siano errori di spelling.
    > Questi file vengono usati da hunspell quando vengono eseguiti i comandi:
    >
    >     make spellcheck     # Linux/Mac OS
    >     ./spellcheck.sh     # Linux/Mac OS
    >
    >     make spellcheck_win # Windows
    >
    > NOTA: i comandi devono essere eseguiti dalla root del repository

L'ideale sarebbe aggiungere programmi di test in C per testare il codice assembly e C.
