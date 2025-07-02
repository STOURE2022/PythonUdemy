import json

import requests


response = requests.get("https://jsonplaceholder.typicode.com/users/")
print(response)

if response.status_code == 200:
    data = response.json()
    print("Vous avez accès à l'api.")
    print(data)
else:
    print("Erreur HTTP : ", response.status_code)

diction = json.dumps(data, indent=4)
print(diction)

nombre = len(data)
print("Le nombre totale est :", nombre)

# Le nom et l'email de chaque utilisateur
for element in data:
    print(f"nom : {element['name']} et email : {element['email']}")

# La ville de chaque utilisateur (adresse["city"])

for element in data:
    print(f"nom : {element['name']} et email : {element['email']} et l'adresse : {element['address']['city']}")

# Trouver tous les utilisateurs qui habitent à "South Christy" et afficher leur nom complet
for element in data:
    if element["address"]["city"] == "South Christy":
        print(f"nom : {element['name']} , non_usage : {element['username']}, city : {element['address']['city']}")

# (Bonus) Latitude & longitude de "Clementina DuBuque"

for element in data:
    if element["name"] == "Clementina DuBuque":
        print(f"La geolocalisation de {element['name']} => \nlat :{element['address']['geo']['lat']}, \nlng :{element['address']['geo']['lng']}")