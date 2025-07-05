
"""
from pathlib import Path
# importer et créer un chemin
# chemin vers un fichier spécifique
chemin_dossier = Path.home() / "Download"
# creation d'un dossier
chemin_dossier.mkdir(exist_ok=True)
# creation d'un fichier
chemin_fichier = chemin_dossier / "fichier.txt"
chemin_fichier.touch(exist_ok=True)

# lister tous les fichiers d'un dossier
# for f in chemin_dossier.iterdir():
#     print(f)

# filtrer sur .txt par exemple
for f in chemin_dossier.glob("*.txt"):
    print(f)

# vérifier l'existence, le type etc
print(chemin_dossier.is_dir())
print(chemin_fichier.is_file())
print(chemin_dossier.exists())

# Écrire du texte
chemin.write_text("Bonjour Soumailou !", encoding="utf-8")

# Lire le contenu
contenu = chemin.read_text(encoding="utf-8")
print(contenu)

# Manipuler les parties du chemin
print(chemin_fichier.name) # fichier.txt
print(chemin_fichier.stem) # fichier
print(chemin_fichier.suffix)  # .txt
print(chemin_fichier.parent) # Download
"""
"""
from pathlib import Path

# création d'un dossier
path_dir = Path.home() / "notes"
path_dir.mkdir(exist_ok=True)
# Création d'un fichier notes/plan.txt
path_file = path_dir / "plan.txt"
path_file.touch(exist_ok=True)
# Ecrire dans le fichier
path_file.write_text("Voici mon plan de travail avec pathlib d'été.")
# lire s'il existe, puis l'affiche
if path_file.exists():
    contenu = path_file.read_text()
    print(contenu)
"""

"""
from pathlib import Path

user_dir = input("Donnez un nom de dossier : ").capitalize()

path_dir = Path.home() / user_dir
path_dir.mkdir(exist_ok=True)
print(path_dir)

user_file = input("Donnez un nom à votre fichier : ").capitalize()
if path_dir.exists():
    path_file = path_dir / user_file
    path_file.touch()
    print(path_file)
else:
    print("Le dossier n'existe pas.")

if path_file.exists():
    user_texte = input("Donne le texte qui sera écrit dans le fichier :\n").capitalize()
    path_file.write_text(user_texte, encoding="utf-8")

containt_file = path_file.read_text(encoding="utf-8")
print(containt_file)
"""

# 🧹 2. Supprimer un dossier vide ; Supprimer un dossier avec son contenu

from pathlib import Path
import shutil

suppression = ["delete_dir_empty", "delete_dir_no_empty_with_containt", "to_leave"]
user_choix = 0

while int(user_choix) != 3:
    user_dir = input("Donnez un nom de dossier : ").capitalize()

    path_dir = Path.home() / user_dir
    path_dir.mkdir(exist_ok=True)
    print(path_dir)

    user_file = input("Donnez un nom à votre fichier : ").capitalize()
    if path_dir.exists():
        path_file = path_dir / user_file
        path_file.touch()
        print(path_file)
    else:
        print("Le dossier n'existe pas.")

    if path_file.exists():
        user_texte = input("Donne le texte qui sera écrit dans le fichier :\n").capitalize()
        path_file.write_text(user_texte, encoding="utf-8")

    containt_file = path_file.read_text(encoding="utf-8")
    print(containt_file)

    user_texte_delete = input(f"Voulez vous supprimer votre fichier 📄 {user_file} ('OUI' ou 'NON') ? ").lower()
    if user_texte_delete == "oui":
        if path_file.exists() and path_file.is_file():
            path_file.unlink()
            print(f"Votre fichier 📄 {user_file} a été supprimé avec succès✅.")
            print(f"Voici le contenu du dossier : {path_dir}")
        else:
            print("❌ le fichier n'existe pas pour suppression.")
    elif user_texte_delete == "non":
        print("📄 fichier concernvé.")

    if path_dir.exists() and path_dir.is_dir():
        print("\n Gestion de suppression des dossiers")
        for num, choix in enumerate(suppression, 1):
            print(f"{num}. {choix}")
        while True:
            try:
                user_choix = input("Entrez votre choix de (1 à 3) : ")
                if int(user_choix) in range(1, 4):
                    break
            except ValueError:
                print("choix inconnu")
                continue
        if int(user_choix) == 1:
            path_dir.rmdir()
            print("📁 Dossier supprimé.")
            continue
        elif int(user_choix) == 2:
            shutil.rmtree(path_dir)
            continue











