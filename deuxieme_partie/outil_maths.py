def carre(nombre):
    return nombre * nombre


def cube(nombre):
    return nombre * nombre * nombre


print("Ce code s'exécute pour ce fichier outil_maths.py et pour les fichiers qui ont importés ce fichier outil_maths.py")

if __name__ == "__main__":
    print("Ce code s'exécute uniquement pour le fichier outil_math.py")
    print(f"Le carré : ", carre(2))
    print(f"Le cube : ", cube(2))
