import random

print("Bienvenue dans le jeu mysterieux")
valeur_myster = random.randrange(1, 100)
nombre_essai = 5

for i in range(nombre_essai):
    user = input("Pour quitter entrez : q ou entrez une valeur pour trouver : ").lower()

    if user == 'q':
        print("Fin du jeu, merci d'avoir joué.")
        break

    try:
        conversion = int(user)
    except ValueError:
        print("Veuillez entrez des nombres ou 'q' pour quitter le programme")
        continue

    essai = nombre_essai - (i+1)
    if essai > 0:
        print(f"Il vous reste {essai} essai")
    else:
        print(f"Dommange le nombre mysterieux est : {valeur_myster}")
        break

    if conversion == valeur_myster:
        print(f"Bravo vous avez trouvé le nombre mysterieux : {valeur_myster}")
        break
    elif conversion > valeur_myster:
        print("Votre valeur est plus grand que le nombre mysterieux, réessayez")
    else:
        print("Votre valeur est plus petit que le nombre mysterieux, réessayez")
