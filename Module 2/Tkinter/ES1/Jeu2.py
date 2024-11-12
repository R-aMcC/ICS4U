"""
-----------------------------------------------------------------------
Auteur: Ryan McCracken
Projet: Jeu de Mathématiques p.2
Date: 2024-10-9
Description: Le jeu donne une somme d'argent à l'utilisatuer, et il doit 
    indiquer le bon nombre de morceaus d'argent pour arriver à la somme
    donné.
-----------------------------------------------------------------------
"""







from Utils import *
from Class import *
import random
#Liste de commandes de sortie valide
OUI = ["y", "yes", "oui", "o"]
NON = ["n", "non", "no"] 
DEFAULT_FONT = "Arial 15 bold"
#Liste de morceaus valide
VALID_PIECES = {"5.00$": 500,
                "2.00$": 200, 
                "1.00$": 100,
                "0.25$":  25,
                "0.10$":  10, 
                "0.05$":   5}

#Génere un nombre pour l'argent
def genereMonnaie(lim = 1000):
    return int((random.randint(1, lim)+4)/5)*5
"""
#Imprime l'argent du format (1000) -> (10.00$)
def printMonnaie(q):
    q = str(q)
    #commence un string vide pour le text
    sb = ""
    for i in range(len(q)):
        # si c'est la deuxième dernière charactère ajoute un "." 
        if(i == len(q)-2):
            sb += "."
        sb += q[i]
    sb += "$"
    #Retourne ce string
    return sb
"""

def printMonnaieREC(q):
    #Fonction recursive pour "pretty print" l'argent
    q = str(q)
    if q == "":
        return "$"
    rs = ""
    if(len(q) == 2):
        rs += "."
    rs += q[0]
    return rs+printMonnaieREC(q[1:len(q)])

def monnaieTotale(liste: dict):
    #Calcule la somme
    total = 0
    for piece in liste:
        #cherche le nombre de chaque morceau
        n = liste[piece]
        #Prend sa valeur
        total += n*VALID_PIECES[piece]
    return total
    



def piecesMonnaie(prix):
    # "Calcule la quantité d'argent le plus efficace pour arriver à la somme "
    pieces_recus = {}
    for piece in VALID_PIECES:
        #trouve la valeur du morceau
        valeur = VALID_PIECES[piece]
        #Trouve le nombre d'entiers qui rentre
        tmpN = prix // valeur
        #Définit la valeur comme étant le nombre
        pieces_recus[piece] = tmpN
        prix -= tmpN*valeur
    
    return pieces_recus


def titre():
    vide()
    print("""
 ██████╗    █████╗    ██╗        ██████╗   ██╗   ██╗   ██╗              ██████╗   ██╗    █████╗   ██████╗     ██████╗   ███████╗  ███╗   ██╗ ████████╗
██╔════╝   ██╔══██╗   ██║       ██╔════╝   ██║   ██║   ██║              ██╔══██╗  ██║   ██╔══██╗  ██╔══██╗   ██╔════╝   ██╔════╝  ████╗  ██║ ╚══██╔══╝
██║        ███████║   ██║       ██║        ██║   ██║   ██║              ██║  ██║  ╚═╝   ███████║  ██████╔╝   ██║  ███╗  █████╗    ██╔██╗ ██║    ██║
██║        ██╔══██║   ██║       ██║        ██║   ██║   ██║              ██║  ██║        ██╔══██║  ██╔══██╗   ██║   ██║  ██╔══╝    ██║╚██╗██║    ██║
╚██████╗   ██║  ██║   ███████╗  ╚██████╗   ╚██████╔╝   ███████╗         ██████╔╝        ██║  ██║  ██║  ██║   ╚██████╔╝  ███████╗  ██║ ╚████║    ██║
 ╚═════╝   ╚═╝  ╚═╝   ╚══════╝   ╚═════╝    ╚═════╝    ╚══════╝         ╚═════╝         ╚═╝  ╚═╝  ╚═╝  ╚═╝    ╚═════╝   ╚══════╝  ╚═╝  ╚═══╝    ╚═╝

""")
    print("-"*100)



def main(nom = ""):
    reussit = []
    non = []
    commence = True
    while commence:
        titre()
        # INstructions
        print("Une somme d'argent sera présenté. Vous aurez besoin d'indiquer le nombre pieces de monnaie")
        print(" requise pour atteindre cette quantité d'argent, en utilisant le moins de pieces possibles")
        input("Cliquez sur \"Enter\" pour continuer...")
        titre()
        #Prend une somme
        monnaie = genereMonnaie()
        #Quantité à donnner 
        print(f"Donne {printMonnaieREC(monnaie)}")
        argent = {}
        #Cherche la quantité pour chaque pièce
        for piece in VALID_PIECES:
            q = chercheNum(f"{piece} : ", False, False)
            argent[piece] = int(q)
        #Cherche la quantité déterminé par l'ordi
        res = piecesMonnaie(monnaie)
        #Si tout est le même, les valeurs sont exactes
        if argent == res:
            print(f"Bravo! Vous avez donné {printMonnaieREC(monnaie)}")
            reussit.append(monnaie)
        elif monnaieTotale(argent) == monnaieTotale(res):
            #Si la totale est exacte, mais les morceaux ne sont pas les mêmes
            print(f"Vous aviez donné la bonne somme d'argent, mais pas dans la manière la plus efficace")
            reussit.append(monnaie)
        else:
            #Si la quantité n'est pas exacte
            print(f"Désolé, vous avez donnée {printMonnaieREC(monnaieTotale(argent))} au lieu de {printMonnaieREC(monnaie)}.")
            non.append(monnaie)
        inp = input("Voulez vous recommencer? (o/n) : ").lower()
        #Si inp est non, le jeu est fini
        while not (inp in OUI or inp in NON):
            inp = input("[ERRUR] Pas une option : ")
        if(inp in NON):
            commence = False

        #montre les informations finales
    print("Score final: ")
    print(f"Vous aviez réussit {len(reussit)} questions,")
    print(f"vous aviez manqué {len(non)} questions.")
    print(f"Ceci fait un taux de réussite de {int(len(reussit)/(len(reussit)+len(non))*100)}%  ")
    

def soumets():
    argent = {}
    for field in inputList:
        label, value = field.get()
        argent[label] = value
    print(argent)
    if(argent == piecesMonnaie(monnaie)):
        print("YES")
    else:
        print("NO")
    finJeu = Results(app, argent == piecesMonnaie(monnaie))
    jeu.grid_forget()
    finJeu.grid(row=1, column=0)

        




def commenceJeu():
    instructions.grid_forget()
    jeu.grid(row=1, column=0)




app = Application()
app._lbl.configure(text="Jeu de monnaie")
jeu = tk.Frame(app)
instructions = tk.Frame(app)

lblInst = tk.Label(instructions, text="Une somme d'argent sera présenté. Vous aurez besoin d'indiquer \n le nombre pieces de monnaie requise pour atteindre cette quantité \n d'argent, en utilisant le moins de pieces possibles", font="Arial 15")
lblInst.grid(row=0, column=0, padx=10, pady=5)
btnInst = tk.Button(instructions, text="Continuer", font=DEFAULT_FONT, command=commenceJeu)
btnInst.grid(row=1, column=0, padx=10, pady=5)
instructions.grid(row=1, column=0)


monnaie = genereMonnaie()
lblMonnaie = tk.Label(jeu, text=f"Donne: {printMonnaieREC(monnaie)}", font=DEFAULT_FONT)
lblMonnaie.grid(row=0, column=0, padx=10, pady=5)



inputs = tk.Frame(jeu)
inputList = []
i:int = 0
for piece in VALID_PIECES:
    field = NumberField(inputs, piece)
    field.grid(column=i%2, row=i//2, pady=10, padx=10)
    field.pad(x=15)
    field._label.configure(font=DEFAULT_FONT)
    inputList.append(field)
    i+=1


resultat = tk.Frame(jeu)
resLbl = tk.Label(resultat, text="Clickez sur le bouton pour \n soumettre votre réponse", font="Arial 15")
resLbl.grid(row=0, column=0, rowspan=2, padx=10, pady=5)
btn = tk.Button(resultat, text="Confirme", font = DEFAULT_FONT, command=soumets)
btn.grid(row=0, column=1, padx=10, pady=5)
inputs.grid(row=1, column=0)
resultat.grid(row=2, column=0)





    


if __name__ == "__main__":
    app.mainloop()
    #main()
