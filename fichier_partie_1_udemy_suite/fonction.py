"""
def saluer(nom="ami"):
    print(f'Bonjour {nom}')


saluer()
"""
"""
def multiplication(a, b):
    resultat = a * b
    return resultat


print(multiplication(2, 8))
"""
"""
Crée une fonction afficher_table qui :

prend un nombre n (ex : 5)

prend un paramètre limite avec une valeur par défaut de 10

affiche la table de n de 1 à limite
"""

"""
def affiche_table(n=10):
    for i in range (11):
        if i * n != 0:
            print(f"{n} * {i} = {n * i}")


affiche_table(4)
"""
"""
def affiche_table(n, limite=10):
    for i in range(n, limite + 1):
        print(f"{n} * {i} = {n * i}")


affiche_table(3, 5)
"""
"""
def generer_table(n, limite=10):
    table = []
    for i in range(n, limite+1):
        ligne = f"{n} * {i} = {n*i}"
        table.append(ligne)
    return table


resultat = generer_table(2, 10)
for ligne in resultat:
    print(ligne)
"""

"""
def min_max(liste):
    return min(liste), max(liste)


petit, grand = min_max([3, 6, 1, 9])
print("Le plus petit : ", petit)
print("Le plus grand : ", grand)
"""
"""
def statistiques_table(n, limite=10):
    lignes = []
    resultat = []
    for i in range(1, limite + 1):
        produit = n * i
        table = f"{n} * {i} = {produit}"
        lignes.append(table)
        resultat.append(produit)
    min_val = min(resultat)
    max_val = max(resultat)

    return lignes, min_val, max_val


table, plus_petit, plus_grand = statistiques_table(2, 10)

for ligne in table:
    print(ligne)

print(f"Le plus petit résulat de la liste  : {plus_petit} ")
print(f"Le plus grand résulat de la liste  : {plus_grand} ")
"""












