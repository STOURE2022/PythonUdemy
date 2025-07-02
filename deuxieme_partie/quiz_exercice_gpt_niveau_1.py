import json
# Exo 1.1
"""
chaine.json = '{"fruit": "pomme", "quantité": 10}'

# 1. Convertir cette chaîne JSON en dictionnaire python

conversion_dictionnaire = json.loads(chaine.json)
print(conversion_dictionnaire)

# 2. Convertis le dictionnaire en chaîne JSON avec indentation

conversion_chaine = json.dumps(conversion_dictionnaire, indent=4)
print(conversion_chaine)
"""

# Exo 1.1
# Convertis ce dictionnaire en une chaîne JSON bien formatée (indentée) et affiche-la.

livre = {
    "titre": "Python pour débutants",
    "auteur": "Jean Dupont",
    "pages": 250,
    "disponible": True
}

conversion_chaine = json.dumps(livre, indent=4)
print(conversion_chaine)


# Exo 1.2
# Convertis cette chaîne JSON en dictionnaire Python, puis affiche tous les prénoms de la liste.

json_str = '''
{
  "nom": ["Alice", "BOB", "Charlie"]
}
'''
conversion_dictionnaire = json.loads(json_str)
print(conversion_dictionnaire)
for element in conversion_dictionnaire["nom"]:
    print(f"{element}")


# Exo 1.3
# Voici une chaîne JSON plus détaillée. Accède aux informations demandées.

chaine = '''
{
  "personne": {
    "nom": "Alice",
    "age": 30,
    "adresses": [
      {"ville": "Paris", "code": 75000},
      {"ville": "Lyon", "code": 69000}
    ]
  }
}
'''

conversion_dict = json.loads(chaine)
print(conversion_dict)

print(conversion_dict["personne"]["nom"])

print(conversion_dict["personne"]["adresses"][1]["code"])