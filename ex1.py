
from pathlib import Path
from contextlib import contextmanager, ExitStack


# ============================================================
# Partie 1 : Gestion manuelle avec __enter__ et __exit__
# ============================================================

class TempFileWriter:

    def __enter__(self):
        self.filepath = Path("temp.txt")
        self.f = self.filepath.open("w")
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()

        if self.filepath.exists():
            self.filepath.unlink()

        print("Fichier temporaire fermé et supprimé.")


print("=== Partie 1 ===")

with TempFileWriter() as f:
    f.write("Contenu temporaire\n")

print("Partie 1 terminée.")


# ============================================================
# Partie 2 : Utilisation de contextlib.contextmanager
# ============================================================

@contextmanager
def temp_file():

    path = Path("temp.txt")
    f = path.open("w")

    try:
        yield f

    finally:
        f.close()

        if path.exists():
            path.unlink()

        print("Fichier temporaire fermé et supprimé.")


print("\n=== Partie 2 ===")

with temp_file() as f:
    f.write("Autre test\n")

print("Partie 2 terminée.")


# ============================================================
# Partie 3 : Utilisation de ExitStack
# ============================================================

print("\n=== Partie 3 ===")

paths = ["a.txt", "b.txt", "c.txt"]

with ExitStack() as stack:

    files = [
        stack.enter_context(open(p, "w"))
        for p in paths
    ]

    for f in files:
        f.write("test\n")

print("Tous les fichiers ont été fermés automatiquement.")
print("Partie 3 terminée.")
