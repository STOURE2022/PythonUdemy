"""Écrire une fonction ventes_fortes(**kwargs) qui :

Calcule la moyenne des ventes de chaque fruit

Ignore les fruits qui ont moins de 4 semaines de données

Garde seulement ceux dont la moyenne est ≥ 120

Trie les résultats par moyenne décroissante

Affiche chaque fruit au format :"""

from statistics import mean

ventes = {
    "Pommes": [120, 135, 110, 98],
    "Bananes": [60, 65, 70],
    "Oranges": [200, 210, 190],
    "Poires": [80, 90, 85],
    "Mangues": [150, 170, 160],
    "Ananas": [130, 140, 125, 135]
}


def ventes_fortes(**kwargs):
    filtrer_ignore = {cle: element for cle, element in kwargs.items() if len(element) >= 4}

    moyenne = {cle: mean(valeur) for cle, valeur in filtrer_ignore.items()}

    filtrer_garde = {cle: valeur for cle, valeur in moyenne.items() if valeur >= 120}

    trie = dict(sorted(filtrer_garde.items(), key=lambda x: x[1], reverse=True))

    for fruit, moyen in trie.items():
        print(f"{fruit} : moyenne ventes = {moyen}")

    return trie


ventes_fortes(**ventes)
