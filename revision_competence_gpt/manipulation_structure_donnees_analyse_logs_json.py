"""Contexte – Analyse de logs JSON
Tu reçois un fichier JSON contenant des événements journaliers générés par différents serveurs dans un datacenter. Chaque événement contient :
le nom du serveur
un horodatage
un indicateur de CPU (%)
un indicateur de RAM (%)
et un status ("OK", "WARNING", "CRITICAL")"""
"""from statistics import mean

logs = [
    {"server": "srv-01", "timestamp": "2025-07-13T08:00:00", "cpu": 88, "ram": 74, "status": "OK"},
    {"server": "srv-01", "timestamp": "2025-07-13T12:00:00", "cpu": 91, "ram": 80, "status": "WARNING"},
    {"server": "srv-02", "timestamp": "2025-07-13T09:00:00", "cpu": 98, "ram": 95, "status": "CRITICAL"},
    {"server": "srv-03", "timestamp": "2025-07-13T10:00:00", "cpu": 63, "ram": 70, "status": "OK"},
    {"server": "srv-02", "timestamp": "2025-07-13T14:00:00", "cpu": 95, "ram": 90, "status": "WARNING"},
    {"server": "srv-01", "timestamp": "2025-07-13T16:00:00", "cpu": 93, "ram": 82, "status": "CRITICAL"},
    {"server": "srv-03", "timestamp": "2025-07-13T15:00:00", "cpu": 68, "ram": 73, "status": "OK"},
]


def analyse_logs(logs: list):
    # Regroupe les données par serveur

    intermediare_cpu ={
        "srv-01": {
            "cpu": [element["cpu"] for element in logs if element["server"] == "srv-01"],
            "alertes": [element["status"] for element in logs if element["server"] == "srv-01"
                        and element["status"] != "OK"]
        },
        "srv-02": {
            "cpu": [element["cpu"] for element in logs if element["server"] == "srv-02"],
            "alertes": [element["status"] for element in logs if element["server"] == "srv-02"
                        and element["status"] != "OK"]
        },
        "srv-03": {
            "cpu": [element["cpu"] for element in logs if element["server"] == "srv-03"],
            "alertes": [element["status"] for element in logs if element["server"] == "srv-03"
                        and element["status"] != "OK"]
        }
    }
    # Calcule pour chaque serveur : la moyenne CPU ; le nombre total d’alertes (WARNING ou CRITICAL)

    #Conserve seulement les serveurs : qui ont au moins 2 événements, ET une moyenne CPU ≥ 90, OU au moins 2 alertes
    moyenne_cpu = {
        "means": {cle: mean(valeur["cpu"]) for cle, valeur in intermediare_cpu.items() if mean(valeur["cpu"]) >= 90},
        "nbre_alertes": {cle: len(valeur["alertes"]) for cle, valeur in intermediare_cpu.items() if valeur["alertes"]}
    }

    tri_moyen_cpu = [dict(sorted(valeur.items(), key=lambda x: x[1], reverse=True)) for cle, valeur in moyenne_cpu.items()]

    for valeur in tri_moyen_cpu:
        for cl, val in valeur.items():
            print(f"{cl} -> {valeur}, moyenne CPU : {moyenne_cpu['means']}")

    return tri_moyen_cpu


analyse_logs(logs)"""

from statistics import mean

# Données JSON simulées
logs = [
    {"server": "srv-01", "timestamp": "2025-07-13T08:00:00", "cpu": 88, "ram": 74, "status": "OK"},
    {"server": "srv-01", "timestamp": "2025-07-13T12:00:00", "cpu": 91, "ram": 80, "status": "WARNING"},
    {"server": "srv-02", "timestamp": "2025-07-13T09:00:00", "cpu": 98, "ram": 95, "status": "CRITICAL"},
    {"server": "srv-03", "timestamp": "2025-07-13T10:00:00", "cpu": 63, "ram": 70, "status": "OK"},
    {"server": "srv-02", "timestamp": "2025-07-13T14:00:00", "cpu": 95, "ram": 90, "status": "WARNING"},
    {"server": "srv-01", "timestamp": "2025-07-13T16:00:00", "cpu": 93, "ram": 82, "status": "CRITICAL"},
    {"server": "srv-03", "timestamp": "2025-07-13T15:00:00", "cpu": 68, "ram": 73, "status": "OK"},
]

def analyse_logs(logs: list):
    # Étape 1 — Regrouper les événements par serveur
    regroupement = {}
    for event in logs:
        nom = event["server"]
        if nom not in regroupement:
            regroupement[nom] = []
        regroupement[nom].append(event)

    # Étape 2 — Calculer la moyenne CPU et le nombre d’alertes
    resume = {}

    for serveur, evenements in regroupement.items():
        if len(evenements) < 2:
            continue  # On ignore les serveurs avec moins de 2 événements

        # Liste des valeurs CPU
        cpu_values = [e["cpu"] for e in evenements]
        cpu_moyenne = mean(cpu_values)

        # Nombre d’alertes (WARNING ou CRITICAL)
        nb_alertes = sum(1 for e in evenements if e["status"] in ("WARNING", "CRITICAL"))

        # Condition : moyenne CPU ≥ 90 OU au moins 2 alertes
        if cpu_moyenne >= 90 or nb_alertes >= 2:
            resume[serveur] = {
                "moyenne_cpu": cpu_moyenne,
                "alertes": nb_alertes
            }

    # Étape 3 — Trier les serveurs :
    # d'abord par nombre d'alertes décroissant, puis par moyenne CPU décroissante
    trie = dict(
        sorted(
            resume.items(),
            key=lambda x: (x[1]["alertes"], x[1]["moyenne_cpu"]),
            reverse=True
        )
    )

    # Étape 4 — Affichage des résultats
    for serveur, infos in trie.items():
        print(f"{serveur} → {infos['alertes']} alertes, moyenne CPU : {infos['moyenne_cpu']:.2f}%")

    return trie  # Optionnel, utile pour test ou appel externe


if __name__ == "__main__":
    print("Le programme s'exécute ici")
    analyse_logs(logs)
