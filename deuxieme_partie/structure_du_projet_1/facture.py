def facture_total(**kwargs):
    return sum(kwargs.values())


reduction = 10
livraison = 10


def facture_reduction(**kwargs):
    result = sum(kwargs.values())
    if result > 100:
        reduct_10 = (result - result * 0.1)
        print(f"Vous bénéficiez de la réduction : {reduction}% et le total à payer est : {reduct_10}")
        return True
    elif result < 100:
        tarif_plein = result + 10
        print(f"Frais de livraison : {livraison}euros et le total a payé est : {tarif_plein}")
        return False


if __name__ == "__main__":
    print("Exécution du code dans le fichier principal.")




