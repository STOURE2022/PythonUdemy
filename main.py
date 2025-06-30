"""
Les structures conditionnelles :
if, elif, else

Les liste (se sont des liés de stockages des objets) :
append, remove, extend

Les boucles (permet de faire répéter une tache plusieurs fois) :
for, while

La fonction raw string permet d'éviter les caractères spéciaux dans les chaines

"""
"""
a = 5 + 5
b = float(a)
d = bool(b)
print(d)
a, b = 2, 6
print(b)
print(id(True))
print(id(True))
prenom = "Pierre"
age = 20
majeur = True
compte_en_banque = 20135.384
a = 3
print("la valeur a est : " + str(a))
"""
"""
nombre = 14
resultat = "Le nombre est de " + str(nombre)
print(resultat)
"""
"""
a = "2"
b = "6"
c = "3"
resultat = "la somme de 2 + 6 + 3 font " + str(int(a)+int(b)+int(c))
print(resultat)
"""
"""
a = 2
b = 6
c = 3
resultat = str(a) + " " + "+" + " " + str(b) + " " + "+" + " " + str(c)
print(resultat)
"""
"""
valeur = input("Quelle est votre valeur : ")
print("Il a mis " + str(valeur))
"""
"""
nom = input("Quel est votre nom : ")
print("Je m'appelle " + str(nom))
ville = input("Quelle est votre ville : ")
print("Je suis de " + str(ville))
age = input("Quel est votre âge : ")
print("Vous avez " + str(age) + "an(s)")
"""
"""
nom = input("Quel est votre nom : ")
ville = input("Quelle est votre ville : ")
age = input("Quel est votre âge : ")
print(f"D'après toutes les infos vous êtes {nom}, vous habitez à {ville} et vous avez {age} an(s)")
"""
"""
a = " gerDanger"
print(a.replace("Dan", "Coura"))
print(a.rstrip("ger"))
print(a.lstrip("ger"))
"""

a = ["1", "2", "3", "4"]
print(a.split(", "))




