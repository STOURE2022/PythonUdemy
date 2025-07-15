import json
from statistics import mean

path_file_logs = r"C:\Users\Soumailou\Desktop\pythonProject\FormationUdemuPython\PythonUdemy\revision_competence_gpt" \
                 r"\projet\data\activity_logs.json"
path_file_report = r"C:\Users\Soumailou\Desktop\pythonProject\FormationUdemuPython\PythonUdemy" \
                   r"\revision_competence_gpt\projet\out\rapport_prioritaire.json"

# Étape 1 : Lecture des données
with open(path_file_logs, "r") as f:
    contenu = json.load(f)


#Étape 2 : Traitement des données
def analyse_logs(logs: list):
    # regoupement par serveur
    regroupement = {}
    for event in contenu:
        nom = event["server"]
        if nom not in regroupement:
            regroupement[nom] = []
        regroupement[nom].append(event)

    resume = {}

    for cle, serveurs in regroupement.items():
        if len(serveurs) < 3:
            continue
        # Moyenne cpu
        recolte_cpu = [serveur["cpu"] for serveur in serveurs]
        means_cpu = mean(recolte_cpu)
        # Moyenne ram
        recolte_ram = [serveur["ram"] for serveur in serveurs]
        means_ram = mean(recolte_ram)
        # Moyenne disque
        recolte_disque = [serveur["disk"] for serveur in serveurs]
        means_disque = mean(recolte_disque)

        recolte_alertes = [serveur["status"] for serveur in serveurs if
                           serveur["status"] in ("CRITICAL", "WARNING")]
        nbre_alertes = len(recolte_alertes)

        if means_cpu >= 85 or means_disque >= 90 or nbre_alertes >= 3:
            resume[cle] = {
                "Moyenne cpu": means_cpu,
                "Moyenne ram": means_ram,
                "Moyenne Disk": means_disque,
                "Nombres alertes": nbre_alertes
            }

    tri = dict(sorted(resume.items(), key=lambda x: (x[1]["Moyenne cpu"], x[1]["Moyenne ram"],
                                                     x[1]["Moyenne Disk"], x[1]["Nombres alertes"]), reverse=True))

    for cl, val in tri.items():
        print(f"{cl} -> {val['Nombres alertes']} alertes | CPU: {val['Moyenne cpu']:.2f}% | "
              f"RAM: {val['Moyenne ram']:.2f}% | Disk: {val['Moyenne Disk']:.2f}%")

    return tri


resultat = analyse_logs(contenu)


with open(path_file_report, "w", encoding="utf-8") as f:
    json.dump(resultat, f, indent=4)


if __name__== "__main__":
    print("le code se lance ici")