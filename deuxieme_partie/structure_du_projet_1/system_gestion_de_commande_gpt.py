

print("\n La liste des choix pour la gestion de commande.")
for cle, valeur in enumerate(choix, 1):
    print(f"{cle}. {valeur}")

user_choix = input("Votre choix : ")

while True:
    if user_choix == "1":
        liste_add_supp = ["add_produit", "delete_produit"]
        for cle, valeur in enumerate(liste_add_supp, 1):
            print(f"{cle}. {valeur}")
        user_add_supp = input("\n Choisissez l'action 1: add ou 2: del ==> ")
        if user_add_supp == "1":
            user_ajout_produit = input("Ajouter des produits avec prix (exemple = 'nom_produit':.. ) : ")
            user_ajout_prix_produit = input("Ajouter des produits avec prix (exemple = '...': prix ) : ")
            liste_produits.append({user_ajout_produit: user_ajout_prix_produit})
            print("produit ajouter")
            print(liste_produits)
        elif user_add_supp == "2":
            user_del_produit = input("\n Choisissez l'élément à supprimer  ==> :")
            liste_produits.remove(liste_produits[user_del_produit])
            print("produit supprimer")


