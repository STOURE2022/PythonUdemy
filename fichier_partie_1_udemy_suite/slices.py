"""
liste = ["Java", "Python", "C++"]
print(liste[::])
"""

"""
liste = ["Maxime", "Martine", "Christophe", "Carlos", "Michael", "Eric"]
# Les trois premiers employés ("Maxime", "Martine" et "Christopher") dans une liste trois_premiers
trois_premiers = liste[:3]
print(trois_premiers)
#Les trois premiers employés ("Maxime", "Martine" et "Christopher") dans une liste trois_premiers
trois_derniers = liste[3:6:1]
print(trois_derniers)
#Tous les employés sauf le premier et le dernier dans une liste milieu
milieu = liste[1:5]
print(milieu)
# Le premier et le dernier employé dans une liste premier_dernier
#premier_dernier = liste[0::5]
premier_dernier = [liste[0], liste[5]]
print(premier_dernier)
"""
"""
# 1_ mini-exercice
jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
# Extrais un jour sur deux, à partir de Lundi
print(jours[::2])
# Extrais un jour sur deux, à partir de Mardi
print(jours[1::2])

# 2_ Inverser une liste Mini-exercice 2 :
jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
print(jours[::-1])
"""
"""
jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
#jours[1] = "Bon"
#print(jours)
jours.insert(1, "Cool")
print(jours)
jours.remove("Cool")
print(jours)
"""
"""
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(len(alpha))
# les 5 premiers
print(alpha[0:5])
# les 5 derniers
print(alpha[21::])
# tous sauf les 5 derniers
print(alpha[:-5])
"""
# Exercice pratique pour toi
"""
employes = ["Alice", "Bob", "Charlie", "Diane"]
employes[1] = "Bruno"
employes.insert(3, "Emma")
print(employes)
"""
"""
employes = ["Alice", "Bruno", "Charlie", "Diane", "Emma"]
user = input("Vous cherchez quel prénom ? ")
if user in employes:
    print("Prénom trouvé")
else:
    print("Prénom non trouvé")
"""
"""
liste_employes = ["Alice", "Bruno", "Charlie", "Diane", "Emma"]
user = input("vous recherchez quel prénom ? ")
if user in liste_employes:
    print("Prénom trouvé")
elif user not in liste_employes:
    ajout = input("vous voulez ajouter un nom si oui entrez le prénom ? ")
    liste_employes.append([ajout])
else:
"""
"""
liste_employes = ["Alice", "Bruno", "Charlie", "Diane", "Emma"]
user = input("1 : Voulez vous afficher la liste des employés 'OUI' ou 'NON' ? "
             "2 : vous recherchez quel prénom ? "
             "3 : Voulez-vous ajouter un nouvel employé ? "
             "4 : Voulez-vous supprimer un employé ? "
             "5 : Voulez vous quitter le programme")
"""
"""
Créer un programme qui propose à l’utilisateur un menu avec plusieurs choix :

csharp
Copier
Modifier
[1] Afficher la liste des employés
[2] Rechercher un prénom
[3] Ajouter un nouvel employé
[4] Supprimer un employé
[5] Quitter
Le programme tourne en boucle tant que l’utilisateur ne choisit pas [5] Quitter.

✅ Fonctions à intégrer :
input() pour les choix

in, .append(), .remove(), .count(), etc.

boucle while pour répéter le menu

conditions if pour chaque option
"""








