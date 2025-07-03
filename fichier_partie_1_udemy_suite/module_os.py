"""
import os

chemin = "C:\\Users\\Soumailou\\Desktop\\pythonProject\\FormationUdemuPython"
dossier = os.path.join(chemin, "dossier")
if not os.path.exists(dossier):
    os.makedirs(dossier)
    print("Le fichier a été crée !")

"""
import os

chemin = "C:\\Users\\Soumailou\\Desktop\\pythonProject\\FormationUdemuPython"
dossier = os.path.join(chemin, "dossier")

os.removedirs(dossier) 