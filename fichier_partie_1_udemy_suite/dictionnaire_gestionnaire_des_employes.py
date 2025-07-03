employes = {"Alice": "Comptable", "Bruno": "Développeur", "Charlie": "Designer"}
mon_choix = 0
while mon_choix != 5:
    print("Menu, choisissez le chiffre qui vous correspond : ")
    print("[1] Afficher tous les employés et leurs rôles")
    print("[2] Rechercher un prénom et afficher son rôle")
    print("[3] Ajouter un nouvel employé avec un rôle")
    print("[4] Supprimer un employé")
    print("[5] Quitter")
    mon_choix = int(input("Quel est votre choix ? "))
    if mon_choix == 1:
        for cle, valeur in employes.items():
            print(f"{cle} - {valeur}")
    elif mon_choix == 2:
        user_search = input("Entrez votre prénom pour avoir son rôle. ").capitalize()
        if user_search in employes:
            print(f"{user_search} est {employes[user_search]}")
        else:
            print("Ce prénom est introuvable")
    elif mon_choix == 3:
        user_ajout_cle = input("Donnez le prénom du nouveau employé à ajouter (clé) : ")
        user_ajout_val = input("Donnez son rôle (valeur) : ")
        employes[user_ajout_cle] = user_ajout_val
        print(employes)
    elif mon_choix == 4:
        user_del = input("Entrez le prénom de l'employé à supprimer : ")
        if user_del in employes:
            del employes[user_del]
            print("Supprimer avec succès : ", employes)
        else:
            print("Suppression impossible car ce prénom n'existe pas")
else:
    print("Fermeture du programme")
