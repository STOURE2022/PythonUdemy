from pathlib import Path

"""
p  = Path.home()
print(p)

p1 = p / "Documents"
print(p1)

p3 = p / "Documents" / "Films"
print(p3)
"""

"""
# Pour afficher notre repertoire courant
p = Path.home()
print(p)
# On fait la concaténation du dossier qu'on souhaite créer
chemin_dossier = p / "Pathlib"
chemin_dossier.mkdir(exist_ok=True)
print(chemin_dossier)
# On va créer le fichier grace à touch dans notre dossier chemin_dossier
chemin_fichier = chemin_dossier / "readme.txt"
chemin_fichier.touch()
print(chemin_fichier)
# On va maintenant écrire dans le fichier
chemin_fichier.write_text("Bonjour les amis.")
print(chemin_fichier)
# On peut lire aussi le contenu de notre fichier
chemin_fichier.read_text()
print(chemin_fichier)
"""
"""
# Scanner l'intérieur de notre disque dur
a = Path.home().iterdir()
for i in a:
    print(i.name)
"""
# Ajouter un suffixe à un non de fichier
"""
rep_dossier = Path.home() / "image.png"
print(rep_dossier)
C:\\Users\Soumailou\image.png

# On va essayer de récupérer le dossier parent C:\\Users\Soumailou
rep_parent_image = rep_dossier.parent / rep_dossier.stem
print(rep_parent_image)
# On va ajouter le siffixe maintenant
fichier_finale = rep_dossier.parent / (rep_dossier.stem + "-lowers" + rep_dossier.suffix)
print(fichier_finale)
fichier_finale.touch()
"""

# On peut trier les fichiers en fonction de leur extension
"""
dirs = {
    ".png": "Images",
    ".jpeg": "Images",
    ".jpg": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".zip": "Archives",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".json": "Documents",
    ".mp3": "Musiques",
    ".wav": "Musiques",
}

tri_dir = Path.home() / "Downloads" / "Tri"
files = [f for f in tri_dir.iterdir() if f.is_file()]
for f in files:
    output_dir = tri_dir / dirs.get(f.suffix, "Autres")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)
"""

















