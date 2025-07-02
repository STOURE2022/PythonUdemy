import json

chaine_json = '''
{
  "groupe": "Développeurs Python",
  "membres": [
    {
      "nom": "Alice",
      "email": "alice@example.com",
      "skills": {
        "python": "avancé",
        "machine_learning": "intermédiaire"
      },
      "projets": [
        {"nom": "Analyse de données", "actif": true},
        {"nom": "Dashboard", "actif": false}
      ]
    },
    {
      "nom": "Bob",
      "email": "bob@example.com",
      "skills": {
        "python": "débutant",
        "machine_learning": "débutant"
      },
      "projets": [
        {"nom": "Scraping Web", "actif": true}
      ]
    }
  ]
}
'''

# Convertir la chaîne JSON en dictionnaire Python

conver_object = json.loads(chaine_json)
print(conver_object)

# Afficher le nom du groupe
print(conver_object["groupe"])

# Pour chaque membre, afficher : son nom, son niveau en Python, ses projets actifs (filtrer sur "actif": true)
for element in conver_object["membres"]:
    if element['projets'][0]['actif']:
        print(
            f"nom : {element['nom']}, niveau python : {element['skills']['python']}, projets : {element['projets'][0]['actif']}")

# Afficher uniquement les membres ayant un niveau "avancé" en Python
for element in conver_object['membres']:
    if element['skills']['python'] == 'avancé':
        print(f"Membre ayant un niveau pyhon avancé est : {element['nom']}")