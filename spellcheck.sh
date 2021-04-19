#!/bin/bash

#
# SPELLCHECK: controlla se sono presenti errori
#             di scrittura nel README e nei file tex
#
# lo script usa hunspell con il dizionario inglese,
# italiano e un dizionario personalizzato per assicurarsi
# che le parole siano valide e esistenti
#
# Autore: Zenaro Stefano
# Versione: 01_03 2020-05-15
#

# esci al primo errore e con il codice di uscita dell'ultimo comando
set -e
set -o pipefail

# percorso di questo script
SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
# percorso del file readme
READMEPATH="${SCRIPTPATH}/README.md"
# percorso della cartella da analizzare
CODEPATH="${SCRIPTPATH}/docs"

# vai nella cartella con i dizionari di hunspell
cd "${SCRIPTPATH}/tests/hunspell"

# togli duplicati dalla wordlist e riordinala. Scrivi il risultato in file temporaneo
sort -u custom_dict-wordlist.txt | sort > custom_dict-wordlist.temp
# sovrascrivi la wordlist rinominando il file temporaneo
mv custom_dict-wordlist.temp custom_dict-wordlist.txt

# sovrascrivi il file dizionario con il numero di parole nella wordlist
wc -l custom_dict-wordlist.txt > custom_dict.dic
# riordina le parole nella word list, togli duplicati e aggiungile a fine dizionario
sort custom_dict-wordlist.txt | uniq >> custom_dict.dic

# memorizza output
output=$(hunspell -d en-GB,it_IT,custom_dict -l < "${READMEPATH}" -u)

echo -e "\n=========================================================\n\n   README SPELLCHECKING"
echo -e "\n=========================================================\n"

# visualizza output
printf "$output"

# se l'output e' vuoto, visualizza "nessun errore trovato"
if [ -z "$output" ] ; then
    echo "Nessun errore di spelling trovato nel file REAMDE.md"
fi

echo -e "\n\n=========================================================\n\n   TEX SPELLCHECKING"
echo -e "\n=========================================================\n"

printf "" > "${SCRIPTPATH}/spellcheck.temp"

# trova in code, file di tipo "file", nome qualsiasi ("*") che finisce con estensione ".tex":
# per ogni file aggiungi il suo percorso al file temporaneo, usa hunspell per trovare gli errori di spelling e inserisci l'output nel file temporaneo
find "$CODEPATH" -type f -iname "*.tex" -exec echo '{}' >> "${SCRIPTPATH}/spellcheck.temp" \; -exec hunspell -d en-GB,it_IT,custom_dict -l -u '{}' >> "${SCRIPTPATH}/spellcheck.temp" \;

# se rimane 0, il file temporaneo contiene solo i percorsi degli script
# altrimenti sono presenti anche errori di spelling
check=0

# per ogni riga nel file temporaneo ("${SCRIPTPATH}/spellcheck.temp")
while IFS="" read -r p || [ -n "$p" ]
do
    # se la riga contiene il percorso ad un file esistente, non e' un errore di spelling
    if ! test -f "$p"; then
        # visualizza la riga con l'errore di spelling
        printf '%s\n' "$p"
        check=1
    fi

done < "${SCRIPTPATH}/spellcheck.temp"

# se il file non conteneva errori di spelling, visualizza il messaggio e cancella il file temporaneo
if [ "$check" -eq "0" ] ; then
    echo "Nessun errore di spelling trovato nei file tex"
    rm "${SCRIPTPATH}/spellcheck.temp"
fi

# controlla se il file contiene errori di spelling:
# se il controllo e' falso (check != 0), lo script terminera' con status code 1
[ "$check" -eq "0" ]

# verifica se l'output e' vuoto (0 = vuoto, 1 = non vuoto):
# se il controllo e' 1, lo script terminera' con status code 1
[ -z "$output" ]
