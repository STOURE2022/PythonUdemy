"""
liste = []
print(liste)
# liste.append([250, "bon"])
liste.extend([3, 5, 7, "G"])
print(liste)
liste.remove("G")
print(liste)
"""
"""
liste = [3, 5, 7, 3, 1, 2, 3, 8, 3, 0, 2]
for element in liste[:]:
    if element == 3:
        liste.remove(3)
print(liste)
"""
# les indices
"""
liste = ["Python", "C++", "java"]
print(liste[-3])
"""

# Récupérez le premier et le dernier nombre contenus dans cette liste dans les variables 'nombre_premier' et 'nombre_dernier'.
"""
nombres = [1, 2, 3, 4, 5, 4, 3, 2, 1]
nombre_premier = nombres[0]
nombre_dernier = nombres[-1]
print(nombre_premier)
print(nombre_dernier)
"""
# Récupérer l'élément 'Python' contenu dans la liste dans la variable 'langage'.
"""
langages = ["Java", "Python", "C++"]
print(langages[1])
"""
# Changez la position de l'élément 'Python' dans la liste pour qu'il se retrouve à la fin de la liste (["Java", "C++", "Python"])
"""
liste = ["Java", "Python", "C++"]
liste.remove("Python")
liste.append("Python")
print(liste)
"""

#employes = ["Carlos", "Max", "Martine", "Patrick", "Alex"]
#r = employes.index("Martine")
#r = employes.count("Martine")
#employes.sort()
#employes.reverse()
#element = employes.pop(2)
#r = employes.clear()
#print(employes)
#employes.append("Carlos")
#print(employes)
#ajout =" ".join(employes)
#print(ajout )

"""
employes = "Carlos, Max, Martine, Patrick, Alex"
element = employes.split(", ")
#element_propre = ","
print(element)
"""
"""
#Vérifier qu'un élément est dans une liste
liste = [1, 2, 3, 4, 5, 6]

if 6 in liste:
    print("Le nombre 6 a bien été ajouté à la liste.")
else:
    print("Le nombre 6 n'a  pas bien été ajouté à la liste.")
print(liste)
"""
"""
# liste imbriquée
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
afficher = matrix[1][1]
print(afficher)
"""
"""
langages = [["Python", "C++"], "Java"]
nombres = [1, [4, [2, 3]], 5, [6], [[7]]]

langage = langages[0][0]
nombre = nombres[1][1][0], nombres[4][0][0]
print(langage)
print(nombre)
"""
villes = ['Paris', 'Lille', 'Lyon']
print(villes[0:2])
print(villes[:-2])












