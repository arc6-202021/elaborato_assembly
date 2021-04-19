# TEST SPELLING

Questa cartella contiene i file di hunspell
per il controllo dello spelling nei file della documentazione.

## Dizionario italiano
I file ```it_IT.aff``` e ```it_IT.dic``` contengono le parole italiane.


Questo dizionario viene usato sia su Windows (comando ```make spellcheck_win```),
sia su Linux/Mac OS (```make spellcheck``` o ```./spellcheck.sh```).

README originale per la licenza:
```
Versione 2.2 (21/05/2005) (dd/mm/yyyy)

For English Readers: please see the text at the end of this document
----------------------------------

**********************************
***********  Italiano  ***********
**********************************

Questo dizionario è rilasciato sotto licenza GPL versione 2.0 o superiore.
Puoi trovare il testo della licenza qui: http://www.gnu.org/ (http://www.gnu.org/licenses/gpl.txt)

Con questo file (README.txt) sono inclusi anche i seguenti:
* it_IT.dic il file del dizionario (radici + regole per l'espansione)
* it_IT.aff il file delle affix (le regole)
* GPL.txt (la licenza GPL)
* license.txt (il copyright e la licenza usata per questo lavoro)
* README_it_IT.txt (una piccola documentazione)
* statistiche.sxc (un file di calc con le statistiche tra le varie versioni del dizionario)
* history.txt (file contenente la storia del dizionario)
* thanks.txt (file contenente i nomi dei volontari)
* notes.txt (file contenente note varie relative alla versione attuale del dizionario)

Puoi trovare le nuove versioni del dizionario qui:
 http://sourceforge.net/projects/linguistico/

Puoi trovare alcune delle vecchie versioni del dizionario qui:
- http://sourceforge.net/projects/ooodocs/
- http://xoomer.virgilio.it/alessandro.prina/

Ulteriori informazioni circa questo dizionario, gli autori e chi ha contribuito, possono essere reperite visitando la pagina:
 http://it.openoffice.org/contribuire/spellcheck.html

Per contattare gli autori è possibile scrivere a:
* DavidePrina(chiocciola)yahoo(punto)com

**********************************
***********  English  ************
**********************************

This dictionary is released under GPL license version 2.0 or above.
You can find the text of the license on http://www.gnu.org/ (http://www.gnu.org/licenses/gpl.txt)

With this file (README.txt) you must find:
* it_IT.dic the dictionary file (words with rules)
* it_IT.aff the affix file (rules)
* GPL.txt (the GPL license)
* license.txt (the copyright and license used for this work)
* README_it_IT.txt (a small documentation)
* statistiche.sxc (a calc file with statistics on our works)
* history.txt (file with the history of the Italian dictionary)
* thanks.txt (file with volunteer names)
* notes.txt (file with additional notes about acutual dictionary version)

You can find new Italian dictionary versions here:
 http://sourceforge.net/projects/linguistico/

You can find some old Italian dictionary versions here:
- http://sourceforge.net/projects/ooodocs/
- http://xoomer.virgilio.it/alessandro.prina/

For further information about this dictionary, the authors or how to contribute to it, please visit http://it.openoffice.org/contribuire/spellcheck.html

You can contact authours writing to:
* DavidePrina(at)yahoo(dot)com
```

## Dizionario inglese
I file ```en-GB.aff``` e ```en-GB.dic``` contengono le parole inglesi.

Questo dizionario viene usato sia su Windows (comando ```make spellcheck_win```),
sia su Linux/Mac OS (```make spellcheck``` o ```./spellcheck.sh```).

README per la licenza ```README_en_GB.txt```.

## Dizionario custom (Linux/Mac OS)
I file ```custom_dict.aff```, ```custom_dict.dic``` e ```custom_dict-wordlist.txt``` contengono le parole che vengono considerate errate perche' "termini tecnici" o keyword di linguaggi di programmazione.

Questo dizionario viene usato SOLO su Linux/Mac OS (```make spellcheck``` o ```./spellcheck.sh```).

Se e' necessario aggiunge parole modificare il file ```custom_dict-wordlist.txt```
lasciando l'ultima riga vuota.
> Lo script aggiornera' automaticamente il file ```custom_dict.dic```.

## Dizionario custom (Windows)
I file ```custom_dict_win.aff```, ```custom_dict_win.dic``` e ```custom_dict_win-wordlist.txt``` contengono le parole che vengono considerate errate perche' "termini tecnici" o keyword di linguaggi di programmazione.

Questo dizionario viene usato SOLO su Windows (```make spellcheck_win```).

Se e' necessario aggiunge parole modificare i seguenti file lasciando l'ultima riga vuota:
* ```custom_dict_win-wordlist.txt```: aggiungere la parola in basso
* ```custom_dict_win.dic```: aggiungere la parola in basso e incrementare di uno il numero
a inizio file (indica quante sono le parole contenute nel dizionario)
