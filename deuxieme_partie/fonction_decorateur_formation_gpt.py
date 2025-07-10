"""def decorateur(fonction):
    def nouvelle_fonction():
        print(">>> Avant la fonction")
        fonction()
        print(">>> Après la fonction")

    return nouvelle_fonction()


def dire_bonjour():
    print("Bonjour !")


# J'applique manuellement le décorateur
decorateur(dire_bonjour)"""

"""def mon_decorateur(fonction):
    def nouvelle_fonction(*args, **kwargs):
        print("🎬 Début de l'exécution")
        resultat = fonction(*args, **kwargs)
        print("🎬 Fin de l'exécution")
        return resultat

    return nouvelle_fonction


@mon_decorateur
def soustraction(x, y):
    return x - y


print(soustraction(3, 7))"""

"""import time


def mesure_temps(fonction):
    def nouvelle_fonction():
        debut = time.time()
        print(f"Début d'exécution de la fonction : {debut} secondes")
        resultat = fonction()
        fin = time.time()
        print(f"Temps d'exécution : {fin - debut:.4f} secondes")
        return resultat

    return nouvelle_fonction


@mesure_temps
def operation_lourde():
    for _ in range(10**6):
        pass


operation_lourde()
"""

# niveau 2

def logger(fonction):
    def message(*args, **kwargs):
        print(f"Appel de la fonction {fonction.__name__} avec les arguments : {args} et {kwargs}")
        resultat = fonction(*args, **kwargs)
        return resultat

    return message


@logger
def multiplier(x, y):
    return x * y


print(multiplier(2, 4))










