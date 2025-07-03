# Boucle for
# liste = [1, 2, 3]
# for i in range(5):
#    print(i)
# for element in liste:
#    print(element)
# chaine = "Soumailou"
# for i in chaine:
#    print("salut", i)

# Boucle_while
"""
i = 0
while i < 20:
    print("ça marche", i)
    i += 1
"""
"""
liste = ["1", "2", "Paul", "5", "Pierre"]
for element in liste:
    if element.isdigit():
        continue
    print(element)
"""
"""
liste = ["1", "2", "Paul", "5", "Pierre"]
for element in liste:
    if element.isdigit():
        break
    print(element)
"""
"""
liste = list(range(10))
print(liste)
for i in liste:
    if i % 2 == 0:
        continue
    else:
        print(i)
"""
"""
liste = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nombre_positifs = [ element for element in liste if element > 0]
print(nombre_positifs)
"""

#Dans cet exercice nous allons afficher les noms de 10 utilisateurs grâce à une boucle.
"""
liste = ["Alice", "Bruno", "Carla", "David", "Emma", "Fatou", "Gaspard", "Hawa", "Ibrahim", "Julie"]
for prenom in liste:
    print(prenom)
"""
"""
# Exercice : Afficher un mot à l'envers
mots = "Python"
direct = [mot for mot in mots]
direct.reverse()
inverse = ", ".join(direct)
print(inverse)
"""
"""
mots = "Python"
for mot in reversed(mots):
    print(mot)
"""
"""
mots = "Python"
conversion = [mot for mot in mots]
for i in conversion:
    print(f"{conversion.index(i)} : {i}")
"""
"""
mots = "Python"
for i, mot in enumerate(mots):
    print(i, mot)

"""

















