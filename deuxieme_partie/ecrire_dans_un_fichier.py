chemin = r"C:\Users\Soumailou\Desktop\pythonProject\FormationUdemuPython\base_tests/fichier.txt"

#ajouter dans écraser ce qui existe déjà
with open(chemin, "a") as f:
    f.write("\nCool")

#ajouter avec écrasement de ce qui existe déjà
with open(chemin, "w") as f:
    f.write("\nCool")

