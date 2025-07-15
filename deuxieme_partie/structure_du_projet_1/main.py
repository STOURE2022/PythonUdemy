from produits import ajout_produits
from produits import trier_produits
from facture import facture_total, facture_reduction
from clients import info_clients
from outis import log_args

liste_produits = ajout_produits(Clavier=20, souris=23, Ecran=54, stylo=8)
print("🛒 Produits ajoutés : ", liste_produits)
print("📦 Produits triés : ", trier_produits(liste_produits))
print("💳 Total facture (sans réduction/livraison) : ", facture_total(**liste_produits))
facture_reduction(**liste_produits)
print("👤 Informations client : ", info_clients(nom="TOURE", pays="France"))


if __name__ == "__main__":
    print("Exécution du code dans le fichier principal.")
