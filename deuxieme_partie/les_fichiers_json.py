import json

chemin = r"C:\Users\Soumailou\Desktop\pythonProject\FormationUdemuPython\base_tests/fichier.json"

#with open(chemin, "w") as f:
    #json.dump("Bonjour", f)
    #json.dump(list(range(20)), f, indent=4)

with open(chemin, "r") as f:
    liste = json.load(f)
    print(type(liste))
