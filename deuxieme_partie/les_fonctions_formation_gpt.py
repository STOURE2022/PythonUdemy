"""
def saluer(non):
    print(f"Bonjour {non}.")
saluer("Soumailou")
"""

"""
def addition(a, b):
    return a + b
result = addition(2, 5)
print(result)
"""

"""
def saluer(nom='invite'):
    print(f"Salut {nom}")

saluer()
saluer("TOURE")
"""

"""
def somme(*nombres):
    return sum(nombres)


print(somme(1, 2, 3))


def afficher_infos(**infos):
    for cle, valeur in infos.items():
        print(f"{cle} : {valeur}")


afficher_infos(nom="Soumailou", age=30)
"""

"""
a = 5
def afficher():
    global a
    a = 10
    print("Dans la fonction: ", a)
afficher()
print("En dehors: ", a)
"""

"""
def exterieur(x):
    def interieur(y):
        return x + y
    return interieur

addition_5 = exterieur(5)
print(addition_5(3))
"""

"""def appliquer(fonction, valeur):
    return fonction(valeur)
def carre(x):
    return x * x"""

# Base des fonctions
"""def saluer():
    print("Boujour")
saluer()

def saluer(prenom):
    print(f"Bonjour {prenom}")
saluer("Soumailou")

def addition(a, b):
    return a + b
resultat = addition(10, 2)
print(resultat)"""
# Exercice
"""def dire_bonjour(prenom):
    print(f"Bonjour {prenom}")
dire_bonjour("Soumailou")

def addition(x, y):
    resultat = x + y
    return resultat
print(addition(2, 4))"""

"""def dire_bonjour(prenom="ami"):
    '''Afficher une salutation, avec ami par défaut lorsqu'un argument n'est pas donnée'''
    print(f"Bonjour {prenom}")
dire_bonjour()
dire_bonjour("Chef")"""

# Exercice 2
"""def presentation(nom, ville="Paris", pays="France"):
    '''cette fonction nous permet d'afficher le nom et la ville et à noter que le nom est obligatoire, la ville
    et le pays sont par default'''
    return f"Bonjour, je m'appelle {nom} et j'habite à {ville}({pays})"


print(presentation("Soumailou", ville="Bamako", pays="Mali"))
print(presentation("Soumailou", "Palaiseau"))"""

'''
Les fonctions *args : permets de mettre autant d'arguments qu'on veut
'''
from statistics import mean

"""def addition(*args):
    return sum(args)
print(addition(1, 2, 3, 4, 6))"""

"""def presenation(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"{cle} : {valeur}")
presenation(nom="Soumailou", age=28, ville="Paris", commune="Essonne")
"""
# exo 4
"""def moyenne_nombre(*args):
    ''' cette fonction nous permet de calculer la moyenne de nombre inconnu de valeur'''
    return mean(args)
print(moyenne_nombre(1, 2, 3, 4, 5))
"""
"""def somme_nombre(*args):
    print(f"Vous avez recu entrez {len(args)} chiffres et resultat des sommes est {sum(args)}")
somme_nombre(2, 4, 6)
"""
"""def afficher_infos(**kwargs):
    print("Les informations : ", kwargs)
afficher_infos(nom="Soumailou", ville="Palaiseau", fonction="dev python")
"""
"""def somme_nombre(*args):
    print(f"Vous avez recu entrez {len(args)} chiffres et resultat des sommes est {sum(args)}")
liste = [10, 20, 30]
somme_nombre(*liste)
"""
"""def affiche_maximum(*args):
    if not args:
        print("Vous n'avez pas passé de valeurs")
    else:
        print(f"Le plus petit nombre est : {min(args)}")
        print(f"Le plus grand nombre est : {max(args)}")
        print(f"La moyenne des nombres est : {mean(args)}")
affiche_maximum(2, 44, 65, 3, 100, 334)
"""
"""def carte_identite(**kwargs):
    '''cette fonction des informations cle valeur'''
    print("\nVoici tes informations d'identités :")
    for cle, valeur in kwargs.items():
        print(f"{cle} : {valeur}")
carte_identite(nom="TOURE", prenom="Soumailou", ville="palaiseau", pays="France", age=100)
"""

'''def carte_identite(**kwargs):
    """cette fonction des informations cle valeur"""
    print("\nVoici tes informations d'identités :")
    if "nom" not in kwargs or "prenom" not in kwargs:
        print("Erreur, le nom et le prénom sont obligatoires.")
        return
    else:
        for cle, valeur in kwargs.items():
            print(f"{cle} : {valeur}")

carte_identite(nom="TOURE", prenom="Soumailou", ville="palaiseau", pays="France", age=100)
'''

'''
Mini-Projet : Calculateur intelligent de commandes
🧠 Objectif :
Créer une fonction qui prend :
	• des produits et leurs prix via *args (ex. : 10, 15, 5.5)
	• des infos client via **kwargs (ex. : nom, adresse, moyen de paiement, livraison)
Et qui affiche :
	• le total de la commande
	• les infos du client
	• une remarque selon le montant (ex. : si total > 100€, livraison offerte)

🏗️ Instructions :
	1. Crée une fonction facture_commande(*args, **kwargs)
	2. Calcule la somme des prix avec *args
	3. Affiche les infos client avec **kwargs
	4. Si total > 100 €, afficher “🚚 Livraison gratuite offerte !”
	5. Sinon, afficher “Livraison facturée 10€” et l’ajouter au total
Afficher le montant final de la commande
'''
# calculateur intelligent de commande
"""livraison = 10
reduction = 20/100
def facture_commande(*args, **kwargs):

    for num, produit in enumerate(args, 1):
        print(f"Produit {num} : {produit}€")

    print("Les informations du client : ")
    for cle, valeur in kwargs.items():
        print(f"{cle} : {valeur}")

    if sum(args) < 100:
        print("\nLivraison facturée 10€")
        total_somme = sum(args) + 10
        print(f"Facture sans frais de livraison : {sum(args)}€ + livraison {livraison}€ = {total_somme}€")
    elif sum(args) >= 200:
        print("\nVous avez bénéficié d'un reduction 🎉de 20% grâce à votre achats.")
        total_somme_reduct = sum(args) - sum(args)*reduction
        print("\n🚚 Livraison gratuite offerte !")
        print(f"\nFacture prix total : {total_somme_reduct}€")
    else:
        print("\n🚚 Livraison gratuite offerte !")
        print(f"\nFacture prix total : {sum(args)}€")



facture_commande(14, 54, 40, 200, nom="TOURE", adresse="73 rue albert camu", paiement="Carte Bancaire", livraison="Express")
print("Merci pour votre fidelité.")
"""

"""
# Q1 : Soumailou habite à Paris
# Q2 : Si on appelle addiction() sans argument on aura une erreur car on doit retourner la valeur de sum
# Q3 :
   '''info_client(nom="Ali", ville="Paris") : retourne une erreur car email n'est pas defini dans l'appel de la fonction'''
   ''' info_client(nom="Ali", email="ali@email.com") : cela va fonctionner car on a tous les éléments qui repondent à la condition if'''
# Q3 :
  ''' si on inverse l'ordre b=2 et *args on aura un conflit car *args prend tous les valeurs sans limite et en mettant b=2 on le limite '''

# Q3 :
  ''' ce code va nous afficher 30'''
"""

"""def calculer_operation(a, b, operation):
    if operation == "addition":
        return a + b
    elif operation == "soustraction":
        return a - b
    elif operation == "multiplication":
        return a * b
    elif operation == "division":
        if b != 0:
            return a / b
        else:
            print("Division par 0 interdite")
    else:
        return "Opértion inconnue"


print(calculer_operation(6, 0, "division"))"""

# lambda
# Syntaxe
'''
   lambda arguments: expression
'''
"""addition = lambda x, y: x + y
print(addition(2, 3))"""
"""saluer = lambda nom: f"Bonjour {nom}"
print(saluer("Soumailou"))

multiplication = lambda x, y: x * y
print(multiplication(3, 2))"""

"""est_pair = lambda x: True if x % 2 == 0 else False
print(est_pair(47))

est_pair = lambda x: x % 2 == 0
print(est_pair(2))"""

"""carre = lambda x: x*x
print(carre(4))

saluer = lambda nom: f"Salut {nom}, bienvenue !"
print(saluer("Soumailou"))

positif = lambda x: True if x>0 else False
print(positif(-4))

plus_grand = lambda x, y: True if x > y else False
print(plus_grand(6, 8))"""

"""nombre = [1, 2, 3, 4]
resultat = list(map(lambda x: x*2, nombre))
print(resultat)


nombres = [1, 2, 3, 4, 5, 6]
resultat = list(filter(lambda x: x % 2 == 0, nombres))
print(resultat)


personnes = [("Ali", 30), ("Bruno", 25), ("Céline", 35)]
resultat = sorted(personnes, key=lambda x: x[1])
print(resultat)"""

"""# Exo_1: doubler les éléments d'une liste avec map()
nombres = [2, 5, 7, 10]
resultat = list(map(lambda x: x*2, nombres))
print(resultat)
# Exo_2 : filtrer les nombres pairs avec filter
nombres = [1, 2, 3, 4, 5, 6, 7, 8]
resultat = list(filter(lambda x: x % 2 == 0, nombres))
print(resultat)
# Exo_3 : Trier une liste de mots par leur longeur
mots = ["voiture", "chat", "éléphant", "arbre"]
resultat = sorted(mots, key=lambda x: len(x))
print(resultat)
# Appliquer une remise de 10% sur tous les prix
prix = [100, 200, 50, 80]
resultat = list(map(lambda x: (x - x*0.1), prix))
print(resultat)
# Exo_5 :  Garde les prénoms qui commencent par "A"
prenoms = ["Ali", "Bruno", "Aïcha", "Céline", "Abdou"]
resultat = list(filter(lambda x: x[0]=="A", prenoms))
print(resultat)"""

"""# niveau intermédiaire
# Exo_1: Trier une liste de dictionnaire par âge
personnes = [
    {"nom": "Ali", "age": 25},
    {"nom": "Soumailou", "age": 30},
    {"nom": "Bruno", "age": 20}
]
tri = sorted(personnes, key=lambda x: x["age"])
print(tri)
# Exo_2 : Appliquer une fonction définie à l’aide de lambda
# Crée une fonction 'appliquer_remise' qui prend un prix et renvoie ce prix avec -10%
prix = [120, 75, 300, 50]
resultat = list(map(lambda x: (x - x*0.1), prix))
print(resultat)
# Exo_3 : Combiner map() + filter()
# 👉 Étape 1 : Multiplier tous les nombres par 3 (map)
# 👉 Étape 2 : Garder seulement les résultats supérieurs à 100 (filter)
nombres = [10, 25, 40, 5]
multi = list(map(lambda x: x*3, nombres))
print(multi)
super_100 = list(filter(lambda x: x>100, multi))
print(super_100)
# Exo_4 : Trier une liste de produits selon leur prix
produits = [
    {"nom": "souris", "prix": 15},
    {"nom": "clavier", "prix": 25},
    {"nom": "écran", "prix": 150},
    {"nom": "USB", "prix": 8}
]
tri = sorted(produits, key=lambda x: x["prix"])
print(tri)
# Exo_5 :
''' Exercice 5 (mini projet bonus) :
Créer une fonction analyse_notes qui :
Prend une liste de notes
Garde seulement celles au-dessus de 10 (filter)
Affiche la moyenne des notes retenues'''
notes = [1, 3, 5, 6, 10, 11, 13, 15, 16, 17, 18, 20]
analyse_notes = list(filter(lambda x: x > 10, notes))
print(analyse_notes)
print(f"La moyenne : {mean(analyse_notes)}")"""

# Mini projet — Analyse des commandes clients
commandes = [
    {"client": "Ali", "montant": 120, "pays": "France"},
    {"client": "Bruno", "montant": 80, "pays": "France"},
    {"client": "Soumailou", "montant": 300, "pays": "Mali"},
    {"client": "Aïcha", "montant": 20, "pays": "France"},
    {"client": "Marie", "montant": 150, "pays": "Mali"},
]
# 1 Affiche la liste des clients triés par montant (du plus petit au plus grand).
tri_montant = sorted(commandes, key=lambda x: x["montant"])
print(tri_montant)
# 2 Filtrer les clients qui ont dépensé plus de 100€.
depense_plus = list(filter(lambda x: x["montant"] > 100, commandes))
print(depense_plus)
# 3 Appliquer une remise de 10% à tous les clients (avec map).
remise = list(map(lambda x: (x["montant"] - x["montant"] * 0.1), commandes))
# remise = list(map(lambda x: {**x, "montant": x["montant"] * 0.9}, commandes))
print(remise)
# 4 Afficher les clients du pays “France” uniquement.
pays_unique = list(filter(lambda x: x["pays"] == "France", commandes))
print(pays_unique)


# 5 Bonus : calculer le total dépensé après remise.
def total_after_remise(*args):
    return sum(args)


print("La somme totale après remise est : ", total_after_remise(*remise))

#  Quiz d’auto-évaluation (niveau intermédiaire)
# Que fait exactement la fonction map() ?
# La fonction map() permet de d'effectuer des opérations sur chaque élément de la liste

# Quelle est la différence entre map() et filter() ?
# la fonction map() permet d'agir sur chaque élément de la liste alors que la fonction filter permet de filtrer
# et de garde uniquement les éléments qu'on a besoin dans la liste

# Comment trier une liste de dictionnaires par une clé personnalisée ?
#  Pour trier une liste de dictionnaire par une clé personnalisée on utilise la fonction sorted(), avec le lambda
#  dans laquelle on précise la clé dans les expressions

# Que renvoie sorted([3, 1, 2], reverse=True) ?
# elle nous renvoi une liste ordonnée [1, 2, 3]

# Écris une lambda qui retourne la racine carrée d’un nombre.
# carre = lambda x: squart(x)

# Peut-on combiner map() et filter() dans une seule ligne ?
#  Oui on peut combiner les fonctions map() et filter ensembe, ils permettent d'agir sur chaque element de la liste, puis
# les filtrer en fonction de ce que l'on souhaite

# Comment utiliser lambda avec sorted() ?
# pour utiliser lambda avec sorted() on fait par exemple
# exemple = sorted(liste, key=lambda x: x*2)