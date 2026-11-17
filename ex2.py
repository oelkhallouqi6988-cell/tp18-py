
from datetime import datetime
from contextlib import ExitStack


# ==========================================
# Partie 1 : Classe ConnectionManager
# ==========================================

class ConnectionManager:

    def __init__(self, service_name):
        self.service_name = service_name

    def __enter__(self):
        print(
            f"[{datetime.now()}] "
            f"Connexion à {self.service_name} établie."
        )
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(
            f"[{datetime.now()}] "
            f"Déconnexion de {self.service_name}."
        )

        if exc_type:
            print(
                f"Erreur détectée : "
                f"{exc_type.__name__} — {exc_value}"
            )

        return False


# ==========================================
# Partie 2 : ExitStack et fichier de logs
# ==========================================

print("========== PARTIE 2 ==========")

with ExitStack() as stack:

    log = stack.enter_context(open("log.txt", "a"))

    conn = stack.enter_context(
        ConnectionManager("Serveur X")
    )

    log.write(
        f"[{datetime.now()}] "
        f"Tâche effectuée sur {conn.service_name}\n"
    )

    print("Tâche effectuée avec succès.")


# ==========================================
# Partie 3 : Simulation d'une erreur
# ==========================================

print("\n========== PARTIE 3 ==========")

try:

    with ExitStack() as stack:

        log = stack.enter_context(open("log.txt", "a"))

        conn = stack.enter_context(
            ConnectionManager("Base Y")
        )

        log.write(
            f"[{datetime.now()}] "
            f"Traitement sur {conn.service_name}\n"
        )

        print("Début du traitement...")

        # Simulation d'une erreur
        raise RuntimeError("Erreur de traitement")

except RuntimeError as e:
    print(f"Exception récupérée : {e}")


# ==========================================
# Fin du programme
# ==========================================

print("\n========== FIN DU PROGRAMME ==========")
print("Toutes les ressources ont été fermées.")
print("Consultez le fichier log.txt pour voir les logs.")
