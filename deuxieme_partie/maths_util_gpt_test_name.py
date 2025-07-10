def addition(x, y):
    return x + y


def soustraction(x, y):
    return x - y


print("🔹 Ce message s'affiche à chaque fois qu'on lit ce fichier ici ou ailleur dans un module d'import")


if __name__ == "__main__":
    print("✅ ce code ne s'exécute que si on exécute maths_util_gpt_name directement ici")
    print(addition(4, 7))
    print(soustraction(4, 7))