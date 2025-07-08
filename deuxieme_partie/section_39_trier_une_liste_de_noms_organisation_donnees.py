from pathlib import Path

# chemin du fichier
path_dir = Path.home() / "Downloads" / "Zone_test"
path_dir.mkdir(exist_ok=True)
path_file = path_dir / "prenoms.txt"
path_file.touch(exist_ok=True)
path_file_trie = path_dir / "new_prenoms_trier.txt"
path_file_trie.touch(exist_ok=True)


# écrire dans le fichier
if path_file.exists():
    path_file.write_text("Charlotte, Raphaël,  Jade, Justin, Zoe, Jeanne, Elsa, Mathis, Sara, David. Chloe, Ludovic,"
                         " Nicolas, Léo, Mathieu, Charles, Apolline, Noemie, Heloïse, Anaïs, Philippe, Antoine, Lina,"
                         " Laura, Pauline, Simon, Maxime, Victoire, Noah, Emilie, Gabrielle, Louise, Nathan, Logan, "
                         "Margaux, Clemence, Inès, Tommy, Isaac, Malik, Yasmine, Lena, Juliette, Eva, Elisa, Lisa, "
                         "Salome, Ambre, Emma, Marie, Maya, Dylan, Mathilde, Noa, Christopher, Anna, Alexis, Elise, "
                         "Guillaume, Adam, Alexandre, Victor, Sarah, Lou, Lucas, Lola, Victoria, Capucine, Jonathan, "
                         "Clara, Camille, Lea, Félix, Gabriel, Cédric, Josephine, Alex, Sofia, Benjamin, Loïc, Thomas, "
                         "Elliot, Romane, Agathe, Alix, Manon, Vincent, Alice, Samuel, Hugo, Diane, Julien, Jacob, "
                         "Margot, Nina, Valentine, Rose, Jérémy, Julie, Anthony, Julia, Tristan, Olivier, Louis, Adèle,"
                         " Michaël, Lucie")

contenu = path_file.read_text()
print(contenu)
contenu_1 = contenu.split()
new_contenu = []
for prenom in contenu_1:
    prenom = prenom.strip()
    prenom = prenom.replace(",", "").replace(".", "")
    new_contenu.append(prenom)

# écrire dans un fichier
with open(path_file_trie, "w") as f:
    f.write("\n".join(sorted(new_contenu)))


"""
liste = "rose     ,          prune, , .orange, kiwi,  ananas , ....,        , tomate..., coco , .. ;;;;;;"
contenu = liste.strip().replace(",", "").replace(".", "").replace(";", "").split()
contenu.sort()

print(contenu)

"""







