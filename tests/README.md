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

* **UNIT TEST**: la cartella **unit_tests** contiene i file per i test delle singole funzioni assembly (eseguire ```make``` per creare i test nella cartella ```bin```)

* **END TO END TEST**: la cartella **e2e_tests** contiene i file per i test lato end user (viene testato l'eseguibile compilato dal makefile nella cartella ```code/assembly```)
