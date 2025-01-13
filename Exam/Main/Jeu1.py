"""
-----------------------------------------------------------------------
Auteur: Ryan McCracken
Projet: Jeu de Mathématiques
Date: 2024-09-20
Description: Le jeu demande à l'utilisateur de répondre à 
    des questions de mathématiques. Lorsque l'utilisateur 
    répond à toutes les questions, le jeu affiche des informations
    sur ses résultats. L'utilisateur peut choisir de réessayer les 
    questions manquées, de recommencer avec de nouvelles questions,
    de réessayer avec seulement des questions de la catégorie où il a
    eu le plus de difficulté.
-----------------------------------------------------------------------
"""
import random
import os
from Utils import *

# Opérateurs par défaut
OPERATEURS_DEFAUT = ["+", "-", "*", "x", "/"]




# Génère un opérateur aléatoire d'une liste d'opérateurs
def genereOperateur(operateurs = ["+", "-", "*", "/"]):
    return operateurs[random.randint(0, len(operateurs)-1)]

# Génère n nombres entre min et max
def genereNombres(n, max, min):
    nombres = []
    for i in range(n):
        nombres.append(random.randint(min, max))
    return nombres

# Génère deux nombres aléatoires entre min et max
def genereDeux(max, min):
    nombres = genereNombres(2, max, min)
    return nombres[0], nombres[1]


# Génère un type de question:
#   - 0: x + y = ?
#   - 1: x + ? = y
#   - 2: ? + y = x
def genereType(operateur, x, y, r):
    qType = random.randint(0, 2)
    match qType:
        case 0:
            return f"{x} {operateur} {y} = ?", r
        case 1:
            return f"{x} {operateur} ? = {r}", y
        case 2:
            return f"? {operateur} {y} = {r}", x

# génère un question avec l'opérateur
def genereQuestion(operateur, max = 10, min = -10):
    # Trouve l'opérateur et détermine le type de question
    # Il génère ensuite une question et une réponse
    match operateur:
        case "+":
            val1, val2 = genereDeux(max, min)
            q, a = genereType(operateur, val1, val2, val1+val2)
        case "-":
            val1, val2 = genereDeux(max, min)
            q, a = genereType(operateur, val1, val2, val1-val2)
        case "/":
            q, a = genereDiv(max, min)
        case "*":
            val1, val2 = genereDeux(max, min)
            while val2 == 0:
                val2 = random.randint(min, max)
            q, a = genereType(operateur, val1, val2, val1*val2)
        case "^":
            val1, val2 = genereDeux(max, min)
            q, a = genereType(operateur, val1, val2, val1^val2)
        case _:
            q = None
            a = None 
    return q, a

def genereDiv(max = 10, min = -10):
    # Génère une division
    # assure que le résultat est un entier
    # et que les valeurs ne sont pas 0
    r, val2 = genereDeux(max, min)
    while val2 == 0:
        val2 = random.randint(min, max)
    while r == 0:
        r = random.randint(min, max)
    val1 = val2*r 
    return genereType("/", val1, val2, r)

# Détermine les opérateurs les plus et moins difficiles
def calculDifficultees(reussit:dict, non:dict):
    additions = [0, 0, "additions"]
    soustractions = [0, 0, "soustractions"]
    multiplications = [0, 0, "multiplications"]
    divisions = [0, 0, "divisions"]

    for q in reussit:
        # pour chaque question réussit, détermine l'opérateur et 
        # incrémente le compteur approprié
        q = str(q)
        op = q.split(" ")[1]
        match op:
            case "+":
                additions[0] +=1
            case "-":
                soustractions[0] +=1
            case "*":
                multiplications[0] +=1
            case "/":
                divisions[0] +=1

    for q in non:
        # pour chaque question non réussit, détermine l'opérateur et
        # incrémente le compteur approprié
        q = str(q)
        op = q.split(" ")[1]
        match op:
            case "+":
                additions[1] +=1
            case "-":
                soustractions[1] +=1
            case "*":
                multiplications[1] +=1
            case "/":
                divisions[1] +=1
    totales = [additions, soustractions, multiplications, divisions]
    #valeurs temporaires pour les valeurs maximales et minimales
    valMax = [-1, -1, "null"]
    valMin = [-1, -1, "null"]
    for total in totales:
        # pour chaque opérateur, détermine si le total est plus grand
        # ou plus petit que les valeurs maximales et minimales
        if total[0] > valMax[0]:
            #ignore si totale est 0
            if total[0] == 0:
                continue
            valMax = total
        if total[1] > valMin[1]:
            if total[1] == 0:
                continue
            valMin = total
   


    return valMax, valMin


    
def titre():
    # Affiche le titre du jeu
    print(f"""


{"██████╗   ███████╗  ███████╗  ███████╗      ██████╗   ███████╗      ███╗   ███╗   █████╗   ████████╗  ██╗  ██╗":^100}
{"██╔══██╗  ██╔════╝  ██╔════╝  ╚═███╔═╝      ██╔══██╗  ██╔════╝      ████╗ ████║  ██╔══██╗  ╚══██╔══╝  ██║  ██║":^100}
{"██║  ██║  █████╗    █████╗      ███║        ██║  ██║  █████╗        ██╔████╔██║  ███████║     ██║     ███████║":^100}
{"██║  ██║  ██╔══╝    ██╔══╝      ███║        ██║  ██║  ██╔══╝        ██║╚██╔╝██║  ██╔══██║     ██║     ██╔══██║":^100}
{"██████╔╝  ███████╗  ██║       ███████╗      ██████╔╝  ███████╗      ██║ ╚═╝ ██║  ██║  ██║     ██║     ██║  ██║":^100}
{"╚═════╝   ╚══════╝  ╚═╝       ╚══════╝      ╚═════╝   ╚══════╝      ╚═╝     ╚═╝  ╚═╝  ╚═╝     ╚═╝     ╚═╝  ╚═╝":^100}
            """)
    print("―"*100)
    
                






def main(nom, parent):
    parent.destroy()
    questions = []
    operateur = ""
    # Boucle principale
    while True:
        vide()
        reussit = {}
        nonReussit = {}
        titre()
        # Utilise les questions déjà générées ou génère de nouvelles questions (n est déterminé par l'utilisateur) 
        for i in range(len(questions) if len(questions) != 0 else chercheNum("Combien de questions voulez-vous?").__abs__()):
            vide()
            titre()
            # Génère une question et une réponse
            q, a = genereQuestion(genereOperateur() if operateur == "" else operateur) if len(questions) == 0 else questions[i]
            # Affiche la question et denmande à l'utilisateur de répondre
            inp = chercheNum(q)
            if(inp == a):
                # Si la réponse est correcte, ajoute la question à la liste des questions réussites
                print("Bravo! Vous aviez eu la bonne réponse!")
                reussit[q] = a
            else:
                # Si la réponse est incorrecte, ajoute la question à la liste des questions non réussites
                print("Désolé, ceci n'est pas la bonne réponse")
                nonReussit[q] = a
            #Attend que l'utilisateur appuie sur ENTER pour continuer
            inp = input("Cliquez sur la touche ENTER pour continuer...")
            vide()
        
        # Affiche les résultats

        y = len(reussit)
        n = len(nonReussit)
        sauvegarde(nom, 0, [y, n])
        #trouve les opérateurs les plus et moins difficiles
        meilleur, pire = calculDifficultees(reussit, nonReussit)
        titre()
        print(f"{"| Résultats |":-^30}")
        print(f"Vous avez répondu à {y+n} questions.")
        print(f"Vous avez eu une note de {int(y/(y+n)*100)}%")
        print(f"Avec {y} bonne réponses et {n} mauvais réponses.")
        #si le nom est nul, tous est 0 (aucune question manqué)
        if pire[2] != "null":
            print(f"Vous avez eu le plus de difficulté avec {pire[2]},")
            totalTMP = pire[0]+pire[1]
            print(f"Dont {int(pire[0]/totalTMP*100) if totalTMP != 0 else 100}% des réponses étaient vraies ({pire[0]} bonnes réponses, {pire[1]} mauvaises réponses).")

        # si le nom est nul, tous est 0 (aucune des questions à été réussie)
        if meilleur[2] != "null":
            print(f"Vous avez eu le moins de difficulté avec {meilleur[2]},")
            totalTMP = meilleur[0]+meilleur[1]
            print(f"Dont {int(meilleur[0]/totalTMP*100) if totalTMP != 0 else "100"}% des réponses étaient vraies ({meilleur[0]} bonnes réponses, {meilleur[1]} mauvaises réponses).")

        # Demande à l'utilisateur s'il veut réessayer les questions manquées, recommencer avec de nouvelles questions, réessayer avec seulement des questions de la catégorie où il a eu le plus de difficulté ou quitter
        print(f"Pour réessayer les questions manquées, entrer \"1\".")
        print(f"Pour réessayer avec des nouveaux questions, entrer \"2\".")
        if pire[2] != "null":
            print(f"Pour réessayer avec seulement des questions de {pire[2]}, entrer \"3\".")
        print(f"Pour quitter, entrer \"q\".")
        inp = input("Choix: ")

        while(inp != "1" and inp != "2" and inp != "3" and inp != "q"):
            #assure que l'entrée est valide
            vide()
            titre()
            inp = input("Voulez-vous réessayer les questions manquées, ou recommencer avec de nouvelles questions, ou quitter? (1/2/3/q): ")
        match inp:
            case "1":
                questions = list(nonReussit.items())
            case "2":
                questions = []
            case "3":
                questions = []
                match pire[2]:
                    case "additions":
                        operateur = "+"
                    case "soustractions":
                        operateur = "-"
                    case "multiplications":
                        operateur = "*"
                    case "divisions":
                        operateur = "/"
                    case _:
                        operateur = ""
            case "q":
                break
                
        

    
    



if __name__ == "__main__":
    main()