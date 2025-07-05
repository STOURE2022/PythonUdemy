from pathlib import Path


d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

chemin = Path.home() / "Downloads" / "Animation"
chemin.mkdir(exist_ok=True)

for cle, valeurs in d.items():
    chemin_animation = chemin / cle
    chemin_animation.mkdir(exist_ok=True)
    for valeur_sous in valeurs:
        chemin_final = chemin_animation / valeur_sous
        chemin_final.mkdir(exist_ok=True)




