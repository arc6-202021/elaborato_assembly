# CODICE

Questa cartella contiene il codice del progetto.

* La cartella **python** contiene i prototipi, pdf con status del progetto e altri file per descrivere gli algoritmi da riprodurre in assembly

* La cartella assembly contiene il progetto finito: contiene il file main.c e poi tutti i file assembly per far funzionare il programma

<details><summary>IDEA INIZIALE SUL WORKFLOW (clicca per visualizzare)</summary>

Ecco la mia idea su come organizzare il progetto...
> NOTA: il codice che ho indicato e' pseudo-codice utile solo a indicare il concetto.
> Dovrebbe essere verosimile ma non e' detto.

<br>

Creiamo 3 cartelle, una per ogni fase di lavoro:

* fase 1: "```C```": contiene il progetto finito scritto solo in linguaggio C suddiviso in piu' file (uno per funzione per facilitare la conversione in assembly)
    > Questo ci permette di avere una base solida (magari testata da test automatici) da cui partire

    Esempio: funzione generica in un file chiamato ```nomefunzione_c.c``` (richiamato in qualche modo dal main o da un'altra funzione)
    ```c
    int nomefunzione_c(param1, param2) {
        istruzione_1;
        istruzione_2;
        istruzione_3;
        istruzione_4;
        istruzione_5;
    }
    ```

* fase 2: "```C_assembly```" o "```assembly_C```": all'inizio conterra' gli stessi file della cartella ```C```, poi man mano andremo a sostituire le singole istruzioni con istruzioni assembly.

    L'idea e' avere un main che richiama le sottofunzioni C che passano semplicemente i parametri alle funzioni assembly.

    Questo ci permette di utilizzare gli stessi test scritti nella fase 1 per garantire il
    funzionamento del codice con i test automatici.

    Primi passi (proseguo con l'esempio di sopra):
    ```c
    int nomefunzione_c(param1, param2) {
        __asm__(
            "istruzioni",
            "per",
            "fare",
            "cio' che fa",
            "l'istruzione 1 in C"
        );

        istruzione_2;
        istruzione_3;
        istruzione_4;
        istruzione_5;
    }
    ```

    Alla fine dovremmo avere:
    ```c
    extern nomefunzione_assembly(param1, param2);

    int nomefunzione_c(param1, param2) {
        /*
            Tutto cio' che fa nomefunzione_c e' richiamare la funzione assembly
            nel file nomefunzione_assembly.s
            > NOTA: io non farei una distinzione cosi' evidente con "_c" o "_assembly".
            > forse ha senso solo per "_c" ma non per i nomi dei file (e delle funzioni) che andremo a consegnare.
        */
        nomefunzione_assembly(param1, param2);
    }
    ```

* fase 3: "```assembly```": all'inizio conterra' solo il file C con il main, poi conterra' i singoli
file delle funzioni assembly (suddivise una per ogni file) copiate da quelle nella cartella della fase 2.

    Un ultimo test automatico verifichera' che i file rimarranno allineati tra la fase 2 e la fase 3.

    Esempio:

    prendiamo il file ```nomefunzione_assembly.s``` (con la funzione ```nomefunzione_assembly```)
    e tutti gli altri file e infine richiamiamo dal main le sottofunzioni assembly:
    ```c
    extern aggregatore_sottofunzioni_assembly(int param);

    int main() {
        /*
            Adesso che tutto e' organizzato in file scritti
            solo in assembly l'unica cosa da fare e' richiamare
            la funzione che aggrega tutto il codice assembly.
        */
        aggregatore_sottofunzioni_assembly(param);
    }
    ```

---

<br>


Per suddividere il lavoro direi che i passi sono questi:

*  decidiamo insieme quanti sottoprogrammi creare e come chiamarli
    > Solo fase 1, dopo manteniamo i nomi uguali

* suddividiamo in parti uguali il numero di sottoprogrammi da creare
    > Ogni persona sara' "specializzata" in ```<X>``` sottoprogrammi

* uniamo insieme i "pezzi del puzzle" (sottofunzioni / codice)
    > Nella prima fase il codice sara' in C e nella terza (quasi tutto) sara' scritto in assembly, nella seconda fase avremo un mix tra assembly e C)

* Creiamo (e ampliamo) i test.
    > solo nella fase 1, poi i test rimangono uguali nella seconda fase


</details>

