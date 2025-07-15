from statistics import mean

ventes = {
    "Clavier": [100, 120, 130],
    "Souris": [75, 95],
    "Écran": [400, 420, 410, 390],
    "Tapis de souris": [15]
}

# Écrire une fonction moyenne_ventes() qui retourne un dictionnaire {produit: moyenne_des_ventes}.
# Afficher uniquement les produits dont la moyenne des ventes dépasse 100.
# Trier les résultats par moyenne décroissante.


def moyenne_ventes(**kwargs):
    moyenne = {cle: mean(valeur) for cle, valeur in kwargs.items()}
    filtrer = {cle: valeur for cle, valeur in moyenne.items() if valeur > 100}
    trie = dict(sorted(filtrer.items(), key=lambda x: x[1], reverse=True))
    return trie


print(moyenne_ventes(**ventes))