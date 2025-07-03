import json
import os

# Dossier cible
path_dossier = r"C:\Users\Soumailou\Desktop\pythonProject\FormationUdemuPython\PythonUdemy\base_tests"

liste_course = []
panel_choix = [
    "Ajouter un élément à la liste de courses",
    "Retirer un élément de la liste de courses",
    "Afficher les éléments de la liste de courses",
    "Vider la liste de courses",
    "Quitter le programme",
    "Sauvegarder la liste"
]

user = 0
while user != 5:
    print("\n📋 Bienvenue dans votre liste de courses")
    print("Faites votre choix d'action :\n")

    for num, valeur in enumerate(panel_choix, 1):
        print(f"{num}. {valeur}")

    nbre_choice = len(panel_choix)

    try:
        user = int(input(f"\nQuel est votre choix d'action [1 à {nbre_choice}] ? "))
    except ValueError:
        print(f"❌ Erreur : veuillez entrer un chiffre entre 1 et {nbre_choice}.")
        continue

    if user not in range(1, nbre_choice + 1):
        print(f"❌ Votre choix n'est pas compris entre 1 et {nbre_choice}.")
        continue

    if user == 1:
        user_ajout = input("Quel élément vous voulez ajouter ? ").capitalize()
        liste_course.append(user_ajout)
        print("✅ Élément ajouté avec succès.")

    elif user == 2:
        user_supp = input("Quel élément vous voulez retirer ? ").capitalize()
        if user_supp in liste_course:
            liste_course.remove(user_supp)
            print(f"✅ Élément retiré avec succès.")
        else:
            print("❌ Cet élément n'existe pas dans la liste.")

    elif user == 3:
        if liste_course:
            print("\n📝 Voici votre liste de courses :")
            for index, element in enumerate(liste_course, 1):
                print(f"{index}. {element}")
        else:
            print("❌ Votre liste est vide.")

    elif user == 4:
        secu = input("⚠️ Voulez-vous vraiment vider votre liste ? (oui/non) : ").lower()
        if secu == 'oui':
            liste_course.clear()
            print("✅ Liste vidée avec succès.")
        elif secu == 'non':
            print("ℹ️ Suppression annulée.")
        else:
            print("❌ Choix invalide.")

    elif user == 6:
        # Vérifier l'existence du dossier
        if not os.path.exists(path_dossier):
            os.makedirs(path_dossier, exist_ok=True)
            print("📁 Dossier créé.")
        else:
            print("📁 Dossier déjà existant.")

        # Nom du fichier
        user_file_creation = input("Nom du fichier (sans extension) : ")
        convert_file = f"{user_file_creation}.json"
        chemin_file = os.path.join(path_dossier, convert_file)

        # Si fichier existe, proposer de recharger
        if os.path.exists(chemin_file):
            user_decide = input(f"⚠️ Le fichier existe. Voulez-vous l'écraser ? (oui/non) : ").lower()
            if user_decide == 'non':
                try:
                    with open(chemin_file, "r", encoding="utf-8") as f:
                        liste_course = json.load(f)
                    print("📄 Liste rechargée avec succès. Vous pouvez continuer à l'utiliser.")
                    continue  # Retour à la boucle principale
                except Exception as e:
                    print("❌ Erreur lors du chargement du fichier :", e)
                    continue
            elif user_decide != 'oui':
                print("❌ Réponse invalide. Annulation de la sauvegarde.")
                continue

        # Écriture/sauvegarde
        try:
            with open(chemin_file, "w", encoding="utf-8") as f:
                json.dump(liste_course, f, indent=4, ensure_ascii=False)
            print("✅ Liste sauvegardée avec succès.")
        except Exception as e:
            print("❌ Erreur lors de la sauvegarde :", e)

print("👋 Fin du programme !")
