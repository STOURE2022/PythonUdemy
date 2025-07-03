import json

chemin = r"C:\Users\Soumailou\Desktop\pythonProject\FormationUdemuPython\PythonUdemy\base_tests\groupe_modifie.json"

# affichage
with open(chemin, "r", encoding="utf-8") as f:
    contenu = json.load(f)
    print(contenu)

# Ajouter un nouveau projet actif à Alice

for element in contenu["membres"]:
    if element['nom'] == "Alice":
        nom_projet = [projet["nom"] for projet in element["projets"]]
        if "Projet IA Générative" not in nom_projet:
            element["projets"].append({
                "nom": "Projet IA Générative",
                "actif": True})
            print(f"Nouveau projet ajouter avec succès pour {element['nom']}.")
        else:
            print(f"Le projet existe déjà pour {element['nom']}")
print("nouveau ajout :", contenu)

# Changer le niveau de Bob en Python à "intermédiaire"
for element in contenu["membres"]:
    if element["nom"] == "Bob":
        if element["skills"]["python"] == "débutant":
            element["skills"]["python"] = "intermédiaire"
        else:
            print("Bob est déjà au nivau intermédiaire.")
print("changement niveau bob", contenu)

# Sauvegarder le résultat dans un nouveau fichier : groupe_modifie.json avec accents lisibles

with open(chemin, "w", encoding="utf-8") as f:
    try:
        if json.dump(contenu, f, ensure_ascii=False, indent=4):
            print("Sauvegarder dans le fichier avec succès.")
    except json.JSONDecodeError as e:
        print("Error: lors du sauvegarde du fichier : ", e)
