import os
import json


# dossier de sauvegarde
path_dossier = r"C:\Users\Soumailou\Desktop\pythonProject\FormationUdemuPython\PythonUdemy\base_tests\dossier_test_os"

# Création d'un dossier de sauvegarde avant les actions

if not os.path.exists(path_dossier):
    os.makedirs(path_dossier)
    print(f"📁Le dossier créé : {path_dossier}.")
else:
    print(f"📁 Dossier {path_dossier} existe déjà.")

# Création d'un fichier de sauvegarde dans le dossier s'il existe avant les actions

if os.path.exists(path_dossier):
    user_choise_name_file = input("Donnez un nom à votre fichier json sans l'extension : ")
    convert_json = f"{user_choise_name_file}.json"
    path_file_complet = os.path.join(path_dossier, convert_json)
    print(path_file_complet)
else:
    print("Vous ne pouvez pas créer de fichier dans ce repetoire car il n'existe pas")

# exemple de donner à enregistrer
data = {
    "groupe": "Développeurs Python",
    "membres": [
        {"nom": "Alice", "niveau": "avancé"},
        {"nom": "Bob", "niveau": "intermédiaire"}
    ]
}

# Enregistrement dans le fichier

with open(path_file_complet, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Données enregistrées avec succès dans le fichier {convert_json}.")


