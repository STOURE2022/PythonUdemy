def ajout_produits(**kwargs):
    return dict(kwargs)


def trier_produits(produits):
    return sorted(produits, key=lambda x: len(x))


if __name__ == "__main__":
    print("Exécution du code dans le fichier principal.")



