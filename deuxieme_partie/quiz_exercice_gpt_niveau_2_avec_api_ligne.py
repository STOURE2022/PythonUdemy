import json

import requests

# 1. Requête GET vers l'API (liste des posts)

response = requests.get("https://jsonplaceholder.typicode.com/posts/")

# 2. Vérifie que tout s'est bien passé
if response.status_code == 200:
    print("Vous avez accès à l'api.")
    data = response.json()
    print(data)
else:
    print("Erreur HTTP :", response.status_code)
    data = []

# Affiche le nombre total de posts reçus

print("le nombre total est :", len(data))

# Affiche le titre du 5e post (index 4)
print("Titre du 5e post : ", data[4]["title"])

# Affiche tous les posts de l'utilisateur ayant userId = 3

for element in data:
    if element["userId"] == 3:
        print("-", element["title"])