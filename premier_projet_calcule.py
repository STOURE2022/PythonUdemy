print("🧮 Calculatrice")
operation = input("\nVous voulez quelle opération (+, -, /, *; %) ? ")
while True:
    print("\n(Entrez 'q' pour quitter à tout moment)")
    saisi_1 = input("Entrez votre 1er nombre : ")
    if saisi_1.lower() == 'q':
        break
    saisi_2 = input("Entrez votre 2eme nombre : ")
    if saisi_2.lower() == 'q':
        break
    try:
        nb_1 = float(saisi_1)
        nb_2 = float(saisi_2)
        if operation == '+':
            calcul = nb_1 + nb_2
            print(f"{nb_1} {operation} {nb_2} = {calcul}")
        elif operation == '-':
            calcul = nb_1 - nb_2
            print(f"{nb_1} {operation} {nb_2} = {calcul}")
        elif operation == '*':
            calcul = nb_1 * nb_2
            print(f"{nb_1} {operation} {nb_2} = {calcul}")
        elif operation == '/':
            calcul = nb_1 / nb_2
            print(f"{nb_1} {operation} {nb_2} = {calcul}")
        elif operation == '%':
            calcul = nb_1 % nb_2
            print(f"{nb_1} {operation} {nb_2} = {calcul}")
        else:
            print("type d'opération inconnu")
    except ValueError:
        print("Vous n'entrez pas que des chiffres")

print("Fin du programme")
