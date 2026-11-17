
import csv
from datetime import datetime


# Classe BatchProcessor
class BatchProcessor:

    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.csv = None
        self.journal = None

    # Ouverture des fichiers
    def __enter__(self):
        try:
            self.csv = open(
                self.csv_file, "r", encoding="utf-8"
            )

            self.journal = open(
                "journal.log", "a", encoding="utf-8"
            )

            print("Fichiers ouverts avec succès.")

            self.journal.write(
                f"[{datetime.now()}] Début du traitement.\n"
            )

            return self

        except (OSError, UnicodeError) as e:
            print(f"Erreur d'ouverture : {e}")

            if self.csv is not None:
                self.csv.close()

            if self.journal is not None:
                self.journal.close()

            raise

    # Traitement des opérations
    def traiter(self):
        try:
            reader = csv.reader(self.csv)

            for ligne in reader:
                if not ligne:
                    continue

                operation = ligne[0]

                print(f"Traitement de l'opération : {operation}")

                self.journal.write(
                    f"[{datetime.now()}] "
                    f"Opération traitée : {operation}\n"
                )

        except (OSError, csv.Error) as e:
            print(f"Erreur de traitement : {e}")
            raise

    # Fermeture des fichiers
    def __exit__(self, exc_type, exc_value, traceback):

        try:
            if self.journal is not None:
                if exc_type:
                    self.journal.write(
                        f"[{datetime.now()}] "
                        f"Erreur : {exc_value}\n"
                    )

                self.journal.write(
                    f"[{datetime.now()}] Fin du traitement.\n"
                )
                self.journal.close()

        except OSError as e:
            print(f"Erreur d'écriture du journal : {e}")

        finally:
            if self.csv is not None and not self.csv.closed:
                self.csv.close()

            print("Fichiers fermés correctement.")

        return False


# Programme principal
try:
    with BatchProcessor("operations.csv") as processor:
        processor.traiter()

except (OSError, csv.Error) as e:
    print(f"Erreur détectée : {e}")

print("Programme terminé.")
