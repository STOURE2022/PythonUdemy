from pathlib import Path

path_file = Path.home() / "Downloads" / "note.txt"
path_file.touch(exist_ok=True)
print(path_file)

path_file_no_dir = r"C:\Users\Soumailou\Downloads\hello.pdf"

path_file.write_text("Bonjour les amis.")

# Gestion des erreurs quand le user met un faux chemin
try:
    with open(path_file_false, "r") as f:
        print(f.read())
except NameError as e:
    print("Erreur :", e)

# Gestion des erreurs lorsque le fichier est introuvable ou ne peut pas être ouvert
try:
    with open(path_file_no_dir, "r") as f:
        print(f.read())
except UnicodeDecodeError as e:
    print("Impossible d'ouvrir le fichier :", e)



