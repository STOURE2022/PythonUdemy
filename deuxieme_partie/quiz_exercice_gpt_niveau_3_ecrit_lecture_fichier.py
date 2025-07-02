import json

chemin = r"C:\Users\Soumailou\Desktop\pythonProject\FormationUdemuPython\base_tests/chaine.json"

# Lire le fichier JSON
with open(chemin, "r", encoding="utf-8") as f:
    contenu = json.load(f)
    print(contenu)
# Afficher le nom du projet
print(contenu["nom"])

# Pour chaque auteur, afficher : nom, niveau en python
for element in contenu["auteurs"]:
    print(f"nom : {element['nom']} skill : {element['skills']['python']}")

# Afficher uniquement les noms des auteurs ayant un niveau avancé en JSON
for element in contenu["auteurs"]:
    if element['skills']['json'] == "avancé":
        print(f"{element['nom']} a un niveau avancé en JSON.")

