import json
from pathlib import Path
from manipulation_structure_donnees_analyse_logs_json import analyse_logs

path_dir = Path.home() / 'downloads'
path_dir.mkdir(exist_ok=True)
path_file = path_dir / "rapport_serveurs.json"
path_file.touch(exist_ok=True)

# Lire un fichier logs.json avec json.load(...)
with open("logs.json", "r") as f:
    data = json.load(f)

result = analyse_logs(data)
print(result)

if path_file.exists():
    with open(path_file, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4)

if __name__ == "__main__":
    print("ce fichier se lance ici.")
