print("Bienvenur sur notre site")
while True:
    user = input("Veuillez entrez votre mode passe à 8 (caractère alpha-num) : ").lower()

    if not user.isalnum():
        print("❌ Le mot de passe ne doit contenir que des lettres et des chiffres.")
        continue

    contient_lettre = any(c.isalpha() for c in user)
    contient_chiffre = any(c.isdigit() for c in user)

    if not (contient_chiffre and contient_lettre):
        print("❌ Votre mot de passe doit contenir au moins un chiffre et une lettre")
        continue
    elif len(user) > 8:
        print("V❌ otre mot de passe dépasse 8 caractères")
        continue
    elif len(user) < 8:
        print("❌ Votre mot de passe est inférieur à 8 caractères")
        continue
    print("✅ Votre mot de passe est valide")
    break


