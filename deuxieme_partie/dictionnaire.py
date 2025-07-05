"""
films = {
    "Le Seigneur des Anneaux": 12,
    "Harry Potter": 9,
    "Blade Runner": 7.5
}
nbre = len(films)
prix = 0

for film in films.values():
    prix += float(film)
print(f"Le prix des {nbre} DVD est : {prix}€")
"""

data = [
    {
        "nom": "Toure",
        "prenom": "Soumailou",
        "fonction": "Developpeur"
    },
    {
        "nom": "Traore",
        "prenom": "Moussa",
        "fonction": "Agronome"
    }
]

# afficher le dictionnaire
# for element in data:
#     for cle, valeur in element.items():
#         print(f"{cle} - {valeur}")

# Modifier des valeurs, la fonction de Soumailou
# for element in data:
#     if element["nom"] == "TOURE":
#         element["fonction"] = "Developpeur python"
# print(data)

# Ajouter et supprimer une valeur dans un dictionnaire
# for element in data:
#     if element["nom"] == "Toure":
#         element["hobbie"] = "Football"
#     print(element)
#
#     if element["nom"] == "Traore":
#         del element["fonction"]
#     print(element)

employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }

# enlever Patrick du dictionnaire
del employes["id03"]
print(employes)

#  changer l'âge de Julie a 26 ans
for item, valeur in employes.items():
    if item == 'id02':
        valeur["age"] = 26
print(employes)





