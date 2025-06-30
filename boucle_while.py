"""
fruits = ["Banane", "Pomme"]
viande = ["Veau gras", "Poulet"]
choix = 0
while choix != 3:
    print("Bienvenue choisissez un numéro de panier pour connaître le contenu : ")
    print("[1] : panier mysterieux 1")
    print("[2] : panier mysterieux 2")
    print("[3] : Quitter le programme")
    choix = int(input("Entrez votre chiffre de choix : "))
    if choix == 1:
        fruit_1 = ", ".join(fruits)
        print(f"Vous avez gagnez un panier de fruits :", fruit_1)
    elif choix == 2:
        fruit_2 = ", ".join(viande)
        print(f"Vous avez gagnez un panier de viande :", fruit_2)
    else:
        print("Choix inconnu, veillez reprendre")
else:
    print("fin du programme")
"""
"""
mots = "PYTHON"
mot_explo = [mot for mot in mots]
print(mot_explo)
"""
"""
nombres = [0, 2, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 23, 24, 26, 28, 30, 32, 34, 36, 38, 39 40, 42, 44, 46, 48, 50]
nombres_pairs = []
for nombre in nombres:
    if nombre % 2 == 0:
        nombres_pairs.append(nombre)
print(nombres_pairs)
"""

"""
nombres = [0, 2, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 23, 24, 26, 28, 30, 32, 34, 36, 38, 39, 40, 42, 44, 46, 48, 50]
nombres_pairs = [nombre for nombre in nombres if nombre % 2 == 0]
print(nombres_pairs)
"""







