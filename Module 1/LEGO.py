print("À tu l'age pour jouer avec les LEGOs?")

age = -1
while True:
    inp = input("Quel est ton age? \nAGE: ")
    try:
        age = int(inp)
        if(age == -1):
            print("Quelque chose s'est mal passé. Essaie encore...\n")
        elif(age >=3 and not(age>=100)):
            print("Vous pouvez jouer avec du LEGO")
            break
        elif(age <3):
            print("Vous êtes trop jeunes pour jouer avec du LEGO")
            break
        else:
            print("Vous êtes trop vieux pour jouer avec du LEGO")
            break
    except:
        print("[ERREUR] Entre votre age comme un nombre entier")