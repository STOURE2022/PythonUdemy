chemin = r"C:\Users\Soumailou\Desktop\pythonProject\FormationUdemuPython\base_tests/fichier.txt"

with open(chemin, "r") as f:
    contenu = f.read().splitlines()
    #new = contenu.splitlines()
    print(contenu)
    #print(new)