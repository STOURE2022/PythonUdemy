user = int(input("Entrez votre table souhaite (exple. 7) : "))
for i in range(0, 10+1):
    produit = i * user
    print(f"{user} * {i} = {produit}")
