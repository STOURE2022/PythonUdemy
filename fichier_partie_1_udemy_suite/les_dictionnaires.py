"""
employes = {"Alice":"Comptable", "Bruno":"Développeur", "Charlie":"Designer"}
# Accès aux valueurs
print(employes["Alice"])
# Ajouter ou modifier
employes["Emma"] = "RH"
print(employes)
# Supprimer un élément
del employes["Bruno"]
print(employes)
# Vérifier si une clé existe
"Alice" in employes
# Parcourir toutes les paires
for nom, role in employes.items():
# Obtenir des clés
employes.keys()
# Obtenir les valeurs
employes.values()
"""
# Exemple
employes = {"Alice":"Compatble", "Bruno":"Développeur"}
# Ajout
employes["Emma"] = "RH"
print(employes)
# Rechercher un élement dans le dictionnaire
if 'Bruno' in employes:
    print(f"Bruno est {employes['Bruno']}")
else:
    print("Bruno n'est pas employé")
# Supprimer
del employes["Alice"]
print(employes)

# Afficher tous les employés
for nom, valeur in employes.items():
    print(f"{nom} - {valeur}")

