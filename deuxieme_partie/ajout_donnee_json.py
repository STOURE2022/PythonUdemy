import json

chemin = r"C:\Users\Soumailou\Desktop\pythonProject\FormationUdemuPython\base_tests/data.json"

# lire ce qui est à l'intérieur du fichier et le récupérer
with open(chemin, "r", encoding='utf-8') as f:
    donnees = json.load(f)

print(donnees)
donnees.append(4)

with open(chemin, "w", encoding='utf-8') as f:
    json.dump(donnees, f, indent=4)

print(donnees)




