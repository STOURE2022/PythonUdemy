liste_employes = ["Alice", "Bruno", "Charlie", "Diane", "Emma"]
votre_choix = 0
while votre_choix != 5:
    print("[1] Voulez vous afficher la liste des employés ?")
    print("[2] Vous recherchez quel prénom ?")
    print("[3] Voulez-vous ajouter un nouvel employé ?")
    print("[4] Voulez-vous supprimer un employé ?")
    print("[5] Voulez vous quitter le programme ?")
    choix_1 = 1
    choix_2 = 2
    choix_3 = 3
    choix_4 = 4
    choix_5 = 5
    votre_choix = int(input("Quel est votre choix ? "))
    if votre_choix == choix_1:
        print(liste_employes)
    elif votre_choix == choix_2:
        user_1 = input("Entrez le prénom que vous cherchez ")
        if user_1 in liste_employes:
            print("Le prénom recherché existe")
        else:
            print("Le prénom recherché n'existe pas")
    elif votre_choix == choix_3:
        user_3 = input("Entrez le prénom de l'employé à ajouter ")
        liste_employes.append(user_3)
        print(liste_employes)
    elif votre_choix == choix_4:
        print(liste_employes)
        user_4 = input("Entrez le prénom de l'employé que vous voulez supprimer ")
        if user_4 in liste_employes:
            liste_employes.remove(user_4)
            print("Supprimer avec succès ! ")
        else:
            print("Le prénom que vous souaitez supprimer n'existe pas, veuillez vérifier")
        print(liste_employes)
else:
    print("Fermeture du programme")
