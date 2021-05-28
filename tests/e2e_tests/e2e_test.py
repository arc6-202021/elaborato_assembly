import os
import sys
import subprocess

boold = False
exit_code = 0

current_path = os.path.dirname(os.path.abspath(__file__))
postfix_folder_path = os.path.join("..", "..", "code", "assembly")
postfix_path = os.path.join(postfix_folder_path, "bin", "postfix")
postfix_path = os.path.abspath(postfix_path)
temp_fout = os.path.join(current_path, "tempout.txt")

if __name__ == "__main__":

    try:
        # vai nella cartella con il makefile e eseguilo, poi torna nella cartella corrente
        os.chdir(postfix_folder_path)
        if boold:
            print("[DEBUG] cartella postfix: ", postfix_folder_path)
            print("[DEBUG] cartella script python: ", current_path)
        subprocess.call(["make"], shell=True)
        os.chdir(current_path)

        # trova i file da dare in input a postfix
        for fin_path in os.listdir("inputs"):
            # prepara i percorsi del file in input, del file in output e del file output atteso
            full_fin_path = os.path.abspath(os.path.join("inputs", fin_path))
            fexpout_file_name = os.path.basename(full_fin_path)
            full_fexpout_path = os.path.abspath(os.path.join("expected_output", fexpout_file_name))

            if boold:
                print("[DEBUG] percorso input:", full_fin_path)
                print("[DEBUG] percorso output atteso:", full_fexpout_path)
                print("[DEBUG] percorso output postfix:", temp_fout)
                print("[DEBUG] eseguo postfix: ", postfix_path, full_fin_path, temp_fout)

            # richiama il programma per ottenere l'output nel file temporaneo
            subprocess.call(postfix_path + " " + full_fin_path + " " + temp_fout, shell=True)

            # leggi l'output del programma
            with open(temp_fout, "r") as fout:
                output = fout.read()

            # leggi output atteso
            with open(full_fexpout_path, "r") as fexpout:
                expected_output = fexpout.read()

            # confronta output e output atteso
            if output != expected_output:
                print(output, "!=", expected_output, ": i contenuti dei file {} non corrispondono".format(fexpout_file_name))
                exit_code = 1
            elif boold:
                print("[DEBUG]", output, "==", expected_output)

    except Exception as e:
        print("\n ERRORE PYTHON: qualcosa e' andato storto:")
        print(e, "file {}".format(fexpout_file_name))
        exit_code = 2

    if exit_code != 0:
        print("\n ERRORE: Almeno un output e' errato (o Python ha avuto errori di esecuzione)")
    else:
        print("\n SUCCESSO: tutti gli output corrispondono")

    sys.exit(exit_code)
