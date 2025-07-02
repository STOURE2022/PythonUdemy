import json

data = r"C:\Users\Soumailou\Desktop\pythonProject\FormationUdemuPython\base_tests/personne.json"
data_info = r"C:\Users\Soumailou\Desktop\pythonProject\FormationUdemuPython\base_tests/infos.json"


# Lecture d'un JSON
with open(data, "r") as f:
    contenu = json.load(f)
print(contenu)

# Ecriture dans un fichier json
with open(data_info, "w") as f:
    json.dump(contenu, f, indent=4)
