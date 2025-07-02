"""
"""
import tkinter

"""
import random

print("Bienvenue dans le jeu de role")
vie_policier = 100
vie_bandit = 200
user_bandit_resiste = ''
user_papier_2 = ''
user_papier_1 = ''
seuil_critique_policier = 20
seuil_critique_bandit = 50
choix_coup_bandit = {"petit_coup": 10,
                     "moyen_coup": 20,
                     "coup_marteau": 50,
                     "coup_chaine": 70
                     }
choix_coup_police = {"petit_coup": 10,
                     "moyen_coup": 20,
                     "gros_coup": 30,
                     "coup_tonnerre": 40,
                     "coup_pistolet": 80
                     }

while not(user_bandit_resiste == 'oui' or vie_bandit <= 0 or user_papier_2 == 'non' or user_papier_1 == 'oui'):
    user_papier_1 = input("Le policier demande au bandit, vous arretez : 'oui' ou 'non' ? ").lower()
    if user_papier_1 not in ['oui', 'non']:
        print("Choix inconnu, vous voulez dire 'oui' ou 'non'")
        continue

    if user_papier_1 == 'oui':
        print("Le bandit se fait arrêter... Fin du combat.")
        break

    if user_papier_1 == 'non':
        print("Vous commencez à me mettre en boule.")
        while True:
            user_papier_2 = input("Le policier : Donnez-moi vos papiers ! Le bandit : 'oui' ou 'non' ? ").lower()
            if user_papier_2 in ['oui', 'non']:
                break
            else:
                print("Choix inconnu, vous voulez dire 'oui' ou 'non'")

    if user_papier_2 == 'non':
        print("Prenez ces coups alors ! ")
        for cle, valeur in enumerate(choix_coup_police, 1):
            print(f"{cle}. {valeur}")
        user_bandit_resiste = ''
        while not(user_bandit_resiste == 'oui' or vie_bandit <= 0):
            try:
                user_police = int(input("Policier choisir : "))
                if user_police == 1:
                    vie_bandit -= choix_coup_police["petit_coup"]
                    print(f"Il reste au bandit {vie_bandit} vies")
                elif user_police == 2:
                    vie_bandit -= choix_coup_police["moyen_coup"]
                    print(f"Il reste au bandit {vie_bandit} vies")
                elif user_police == 3:
                    vie_bandit -= choix_coup_police["gros_coup"]
                    print(f"Il reste au bandit {vie_bandit} vies")
                elif user_police == 4:
                    vie_bandit -= choix_coup_police["coup_tonnerre"]
                    print(f"Il reste au bandit {vie_bandit} vies")
                elif user_police == 5:
                    vie_bandit -= random.randrange(50, choix_coup_police["coup_pistolet"], 10)
                    print(f"Il reste au bandit {vie_bandit} vies")
            except ValueError:
                print("choix inconnu, veuillez choisir entre 1 à 5.")
                continue

            if vie_bandit <= 0:
                print("Le bandit est mort, le policier à gagner !")
                break

            if vie_bandit < seuil_critique_bandit:
                print("Vous être presque mort")
                while True:
                    user_bandit_resiste = input(f"Vous êtes dans un état critique il vous reste {vie_bandit} vies,"
                                            f" voulez-vous arrêter 'OUI' ou 'NON' ? ").lower()
                    if user_bandit_resiste in ['oui', 'non']:
                        break
                    else:
                        print("Erreur : sûrement vous avez tapé des chiffres, string non reconnu.")
            if user_bandit_resiste == 'oui':
                print("Le bandit se rend !")
                break
            elif user_bandit_resiste == 'non':
                print("Le combat continue !")
                continue

        else:
            print("La partie est terminé pour le bandit.")
    else:
        print("Sage decision, le bandit se rend.")
        break
else:
    print("Fin de la partie.")
"""
import random

print("Bienvenue dans le jeu de role")
vie_policier = 100
vie_bandit = 200
user_bandit_resiste = ''
user_policier_resiste = ''
user_papier_2 = ''
user_papier_1 = ''
seuil_critique_policier = 20
seuil_critique_bandit = 50
potion_policier = random.randrange(50, 70, 5)
nombe_potion = 3
user_bandit_resiste = ''
choix_coup_bandit = {"petit_coup": 10,
                     "moyen_coup": 20,
                     "coup_marteau": 50,
                     "coup_chaine": 70
                     }
choix_coup_police = {"petit_coup": 10,
                     "moyen_coup": 20,
                     "gros_coup": 30,
                     "coup_tonnerre": 40,
                     "coup_pistolet": 80
                     }

clefs_policier = list(choix_coup_police.keys())
clefs_bandit = list(choix_coup_bandit.keys())

while not (user_bandit_resiste == 'oui' or user_policier_resiste == 'oui' or vie_bandit <= 0 or vie_policier <= 0 or
           user_papier_2 == 'non' or user_papier_1 == 'oui'):
    user_papier_1 = input("Le policier demande au bandit, vous arretez : 'oui' ou 'non' ? ").lower()
    if user_papier_1 not in ['oui', 'non']:
        print("Choix inconnu, vous voulez dire 'oui' ou 'non'")
        continue

    if user_papier_1 == 'oui':
        print("Le bandit se fait arrêter... Fin du combat.")
        break

    if user_papier_1 == 'non':
        print("Vous commencez à me mettre en boule.")
        while True:
            user_papier_2 = input("Le policier : Donnez-moi vos papiers ! Le bandit : 'oui' ou 'non' ? ").lower()
            if user_papier_2 in ['oui', 'non']:
                break
            else:
                print("Choix inconnu, vous voulez dire 'oui' ou 'non'")

    if user_papier_2 == 'non':
        print("Prenez ces coups alors ! ")
        print("\n--- Tour du Policier ---")
        while not (user_bandit_resiste == 'oui' or vie_bandit <= 0 or vie_policier <= 0):
            for i, coup in enumerate(clefs_policier, 1):
                print(f"{i}. {coup}")

            if nombe_potion > 0:
                print(f"P. utiliser une potion(+{potion_policier} vies) - {nombe_potion} restantes")

            user_police_potion = input("Policier: entrez un chiffre (1-5) pour attaquer ou 'P' pour "
                                       "utiliser une potion : ").lower()

            if user_police_potion == 'p':
                if nombe_potion > 0:
                    vie_policier += potion_policier
                    nombe_potion -= 1
                    print(f"Potion utilisée ! Vie du policier : {vie_policier} | Potions restantes : {nombe_potion}")
                else:
                    print("Vous n'avez plus de potions !")
                continue

            try:
                for i, coup in enumerate(clefs_policier, 1):
                    print(f"{i}. {coup}")
                user_police = int(user_police_potion)
                coup_policier_choisi = clefs_policier[user_police - 1]
                degats = choix_coup_police[coup_policier_choisi]
                if choix_coup_police == "coup_pistolet":
                    degats = random.randrange(50, 70, 5)
                vie_bandit -= degats
                print(f"le policier a choisi {coup_policier_choisi} et inflige {degats} dégâts")
                print(f"Il reste {vie_bandit} vies au bandit.")

                print("\n---- Replique du bandit ----")

                for i, coup in enumerate(clefs_bandit, 1):
                    print(f"{i}. {coup}")
                while True:
                    try:
                        user_bandit = int(input("Bandit choisir le coup : "))
                        if user_bandit in range(1, len(choix_coup_bandit) + 1):
                            break
                    except ValueError:
                        print("Erreur soit le type ou le nombre choisi n'est pas reconnu")
                coup_bandit_choisi = clefs_bandit[user_bandit - 1]
                degats = choix_coup_bandit[coup_bandit_choisi]
                if coup_bandit_choisi == "coup_chaine":
                    degats = random.randrange(50, 70, 5)
                vie_policier -= degats
                print(f"le bandit a choisi {coup_bandit_choisi} et inflige {degats} dégâts")
                print(f"Il reste {vie_policier} vies au policier.")

            except ValueError:
                print("choix inconnu, veuillez choisir entre 1 à 5.")
                continue

            if vie_bandit <= 0:
                print("Le bandit est mort, Victoire pour le policier !")
                break

            if vie_policier <= 0:
                print("Le Policier est mort, Victoire pour le bandit !")
                break

            if vie_bandit < seuil_critique_bandit:
                print("Le bandit est presque mort.")
                while True:
                    user_bandit_resiste = input(f"Le Bandit est dans un état critique il lui reste {vie_bandit} vies,"
                                                f" voulez-vous arrêter 'OUI' ou 'NON' ? ").lower()
                    if user_bandit_resiste in ['oui', 'non']:
                        break
                    else:
                        print("Erreur : sûrement vous avez tapé des chiffres, string non reconnu.")
            if user_bandit_resiste == 'oui':
                print("Le bandit se rend !")
                break
            elif user_bandit_resiste == 'non':
                print("Le combat continue !")
                continue

            if vie_policier < seuil_critique_policier:
                print("Monsieur le policier, vous être presque mort !")
                while True:
                    user_policier_resiste = input(f"Le Policier est dans un état critique, il lui reste {vie_policier} "
                                                  f"vies, voulez-vous arrêter 'OUI' ou 'NON' ? ").lower()
                    if user_policier_resiste in ['oui', 'non']:
                        break
                    else:
                        print("Erreur : sûrement vous avez tapé des chiffres, string non reconnu.")
            if user_policier_resiste == 'oui':
                print("Le Policier laisse le bandit partir !")
                break
            elif user_policier_resiste == 'non':
                print("Le combat continue !")
                continue

        else:
            print("La partie est terminé pour le bandit.")

    else:
        print("Sage decision, le bandit se rend.")
        break
else:
    print("Fin de la partie.")
