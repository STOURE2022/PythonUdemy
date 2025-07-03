import os

path_file = r"C:\Users\Soumailou\Desktop\pythonProject\FormationUdemuPython\PythonUdemy\base_tests\liste_course.json"
os.path.join(path_file, "liste_course.json")

liste_course = []
panel_choix = [
    "Ajouter un élément à la liste de courses",
    "Retirer un élément de la liste de courses",
    "Afficher les éléments de la liste de courses",
    "Vider la liste de courses",
    "Quitter le programme",
]
user = 0
while user != 5:
    print("\nBienvenue dans votre liste de course")
    print("\nFaite votre choix d'action : ")

    for num, valeur in enumerate(panel_choix, 1):
        print(f"{num}. {valeur}")

    nbre_choice = len(panel_choix)

    try:
        user = int(input(f"\nQuel est votre choix d'action [1 à {nbre_choice}] ? "))
    except ValueError:
        print(f"\nErreur : veuillez entrez un chiffre entre 1 à {nbre_choice}.")
        continue

    if user not in range(1, len(panel_choix)+1):
        print(f"\nVotre choix n'est pas compris entre 1 et {nbre_choice}.")
        continue

    if user == 1:
        user_ajout = input("\nQuel élément vous voulez ajouter ? ").capitalize()
        liste_course.append(user_ajout)
        print("\nElément ajouter avec succès")
        print(liste_course)
    elif user == 2:
        user_supp = input("\nQuel élément vous voulez retirer ? ")
        if user_supp in liste_course:
            liste_course.remove(user_supp)
            print(f"L'élément est rétiré avec succès. \n{liste_course}")
        else:
            print("\nVotre élément n'existe pas de base dans la liste.")
    elif user == 3:
        if liste_course:
            print("\nVoici votre liste de course : ")
            for index, element in enumerate(liste_course, 1):
                print(f"{index}. {element}")
        else:
            print("\nVotre liste de course est vide.")
    elif user == 4:
        secu = input("\nAttention, vous allez vider votre liste, voulez-vous cette action (oui ou non) ? ").lower()
        if secu == 'oui':
            if liste_course:
                liste_course.clear()
                print("\nListe vidé avec succès", liste_course)
            else:
                print("\nVotre liste est déjà vide")
        elif secu == 'non':
            print("\nSuppression abandonné !")
        else:
            print("\nChoix de suppression inconnu, veuillez choisir entre 'OUI' ou 'NON'")
else:
    print("\nFin du programme !")
