import json

# 1. Chaîne JSON simulée comme une réponse d'API

json_response = '''
{
  "utilisateur": {
    "id": 42,
    "nom": "Alice",
    "email": "alice@example.com",
    "projets": ["Data", "IA", "Web"]
  }
}
'''
# conversion en dictionnaire
data = json.loads(json_response)
print(data)
# Accès aux données
print("ID :", data["utilisateur"]["id"])
print("Email :", data["utilisateur"]["email"])
print("Projets :", data["utilisateur"]["projets"])
print("Deuxième projet :", data["utilisateur"]["projets"][1])