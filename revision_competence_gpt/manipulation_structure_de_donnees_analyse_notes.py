from statistics import mean

notes = {
    "Aïcha": [12, 15, 14, 16],
    "Moussa": [8, 9, 10],
    "Fatou": [17, 18, 16, 19],
    "Oumar": [10, 10, 11],
    "Seydou": [20, 19, 19],
}


def analyse_notes(**kwargs):
    moyenne = {cle: mean(valeur) for cle, valeur in kwargs.items()}

    filtrer = {cle: valeur for cle, valeur in moyenne.items() if valeur > 12}

    trie = dict(sorted(filtrer.items(), key=lambda x: x[1], reverse=True))

    for nom, moyen in trie.items():
        result = f"{nom} -> moyenne: {moyen}"
        print(result)

    return trie


analyse_notes(**notes)
