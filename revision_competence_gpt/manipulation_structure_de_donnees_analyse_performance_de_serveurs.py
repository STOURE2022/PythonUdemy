""" Objectifs :
Écrire une fonction serveurs_chauds(**kwargs) qui :

Calcule la moyenne CPU par serveur

Ignore les serveurs avec moins de 3 jours de données

Conserve ceux dont la moyenne CPU > 70%

Trie le résultat par moyenne CPU décroissante

Affiche le résultat proprement :
"srv-002 : moyenne CPU = 94.00% """

from statistics import mean

serveurs = {
    "srv-001": [
        {"cpu": 75, "ram": 60},
        {"cpu": 80, "ram": 70},
        {"cpu": 72, "ram": 65},
    ],
    "srv-002": [
        {"cpu": 95, "ram": 90},
        {"cpu": 93, "ram": 88},
    ],
    "srv-003": [
        {"cpu": 70, "ram": 45},
        {"cpu": 78, "ram": 50},
        {"cpu": 98, "ram": 40},
        {"cpu": 66, "ram": 48},
    ],
    "srv-004": [
        {"cpu": 60, "ram": 80},
        {"cpu": 65, "ram": 82},
        {"cpu": 62, "ram": 85},
        {"cpu": 63, "ram": 83},
    ]
}


def serveurs_chauds(**kwargs):
    filtrer_donnees = {cle: valeur for cle, valeur in kwargs.items() if len(valeur) > 3}

    moyenne_cpu = {cle: mean([element["cpu"] for element in valeur]) for cle, valeur in filtrer_donnees.items()}

    conver_cpu = {cle: valeur for cle, valeur in moyenne_cpu.items() if valeur >= 70}

    trie = dict(sorted(conver_cpu.items(), key=lambda x: x[1], reverse=True))

    for cle, element in trie.items():
        print(f"{cle} : moyenne CPU = {element:.2f}%")

    return trie


serveurs_chauds(**serveurs)
