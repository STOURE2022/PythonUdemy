import json

chemin = r"C:\Users\Soumailou\Desktop\pythonProject\FormationUdemuPython\base_tests/data.json"
chemin_1 = r"C:\Users\Soumailou\Desktop\pythonProject\FormationUdemuPython\base_tests/data_1.json"
json_str = '{"nom": "Alice", "age": 30}'


# lire json en python
#data = json.loads(json_str)
#print(data)
# print(data["nom"])

# Ecrire un JSON : convertir un dictionnaire python vers une chaîne json
#data = {'nom': 'Alice', 'age': 30}
#json_str = json.dumps(data, indent=4)
#print(json_str)

# lire un fichier Json

with open(chemin, "r") as f:
    data = json.load(f)
print("la data est : ", data)

# Ecrire dans un fichier json
with open(chemin_1, "w") as f:
    json.dump(data, f, indent=4)
