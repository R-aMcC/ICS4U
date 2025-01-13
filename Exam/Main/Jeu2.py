"""
-----------------------------------------------------------------------
Auteur: Ryan McCracken
Projet: Jeu de Mathématiques p.2 - Interface graphique
Date: 2024-11-19
Description: Le jeu donne une somme d'argent à l'utilisatuer, et il doit 
    indiquer le bon nombre de morceaus d'argent pour arriver à la somme
    donné.
-----------------------------------------------------------------------
"""

from Utils import *
from Class import *
import random
import tkinter as tk


class Results(tk.Frame):
    """Classe pour montrer si tu a gagné ou non \n
        @param main: Le frame principal 
        @param obtenue: Le dictionaire des valeurs obtenues 
        @param valeur: La valeur attendue 
        @param scores: La liste des scores (Réussit, manqué)
    """
    def __init__(self, main, obtenue, valeur, scores:list):
        """
        @param main: Le frame principal 
        @param obtenue: Le dictionaire des valeurs obtenues 
        @param valeur: La valeur attendue 
        @param scores: La liste des scores (Réussit, manqué)
    """
        super().__init__(main)
        # Verifie si la valeur est correcte
        if obtenue == piecesMonnaie(valeur):
            # Parfaitement bien, réussit de la manière la plus efficace
            self._label = tk.Label(self, text="Bravo! \n Vous avez donné la bonne réponse!", font="Arial 15")
            scores[0] += 1
        elif monnaieTotale(obtenue) == valeur:
            # Bonne réponse, mais pas la manière la plus efficace
            self._label = tk.Label(self, text="Bravo! \n Vous avez donné la bonne réponse, \n mais il y a une manière plus efficace", font="Arial 15")
            scores[1] += 1
        else:
            # Mauvaise réponse
            self._label = tk.Label(self, text=f"Uh oh! \n Vous n'avez pas donné la bonne réponse! \n ({printMonnaieREC(monnaieTotale(obtenue))} au lieu de {printMonnaieREC(valeur)})", font="Arial 15")
            scores[1] += 1
        # Montre le label et définit les autres widgets
        self._label.grid(row=0, column=0, rowspan=3, columnspan=2, padx=10, pady=5)
        self._btnContinue = tk.Button(self, text="Continue", font="Arial 15")
        self._btnContinue.grid(row=3, column=0, padx=10, pady=5)
        self._btnFini = tk.Button(self, text="Quitter", font="Arial 15")
        self._btnFini.grid(row=3, column=1, padx=10, pady=5)

    def setCommandContinue(self, command):
        self._btnContinue.configure(command=command)

    def setCommandFini(self, command):
        self._btnFini.configure(command=command)






#Liste de commandes de sortie valide
OUI = ["y", "yes", "oui", "o"]
NON = ["n", "non", "no"] 
#Font par défaut
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

def printMonnaieREC(q):
    """Fonction recursive pour "pretty print" l'argent"""
    q = str(q)
    if q == "":
        return "$"
    rs = ""
    if(len(q) == 2):
        rs += "."
    rs += q[0]
    return rs+printMonnaieREC(q[1:len(q)])

def monnaieTotale(liste: dict):
    """Calcule la somme"""
    total = 0
    for piece in liste:
        #cherche le nombre de chaque morceau
        n = liste[piece]
        #Prend sa valeur
        total += n*VALID_PIECES[piece]
    return total
    



def piecesMonnaie(prix):
    """Calcule la quantité d'argent le plus efficace pour arriver à la somme """
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


def main(nom = "", parent = None):
    if parent:
        parent.destroy()
    """
    Méthode principale pour le jeu de monnaie
    """
    # Les résultats
    scores = [0, 0]

    
        


    def commenceJeu():
        """Méthode pour commencer le jeu"""
        instructions.grid_forget()
        # Oublie les anciens frames et crée un nouveau jeu.
        oubli(app)
        Jeu(jeu)
        jeu.grid(row=1, column=0)

    def fin():
        """Méthode pour finir le jeu.
          \n Montre si tu a réussit ou non"""
        #Crée un nouveau frame pour les résultats
        resTotal = tk.Frame(app)
        lbl = tk.Label(resTotal, text=f"Vous avez réussit {scores[0]} questions, et vous avez manqué {scores[1]} questions \n Ceci arrive avec un pourcentage de réussie de {int(scores[0]/(scores[0]+scores[1])*100)}%", font=DEFAULT_FONT)
        lbl.grid(row=0, column=0, padx=10, pady=5, rowspan=2)
        btn = tk.Button(resTotal, text="Terminé", font=DEFAULT_FONT, command=app.quit)
        btn.grid(row=2, column=0, padx=10, pady=5)
        sauvegarde(nom, 1, scores)

        #Oublie les anciens frames
        oubli(app)
        #Montre les résultats
        resTotal.grid(row=1, column=0)



    def Jeu(jeu):
        """Créé la question avec l'interface. \n
        Contient les NumberFields, les boutons et les instructions"""
        def soumets():
            """Méthode pour soumettre la réponse"""
            #Crée un dictionnaire pour les valeurs
            argent = {}
            #Ajoute les valeurs des NumberFields
            for field in inputList:
                #Trouve la valeur et le label
                label, value = field.get()
                #Ajoute la valeur au dictionnaire
                argent[label] = value
            # Ajoute l'interface du fin jeu
            finJeu = Results(app, argent, monnaie, scores)
            finJeu.setCommandContinue(commenceJeu)
            finJeu.setCommandFini(fin)
            #Oublie le jeu et montre les résultats
            jeu.grid_forget()
            finJeu.grid(row=1, column=0)

        #Crée la somme d'argent
        monnaie = genereMonnaie()
        #Crée un label pour la somme d'argent
        lblMonnaie = tk.Label(jeu, text=f"Donne: {printMonnaieREC(monnaie)}", font=DEFAULT_FONT)
        lblMonnaie.grid(row=0, column=0, padx=10, pady=5)

        #Crée les NumberFields. Rows est le nombre de colonnes
        rows = 2
        inputs = tk.Frame(jeu)
        inputList = []
        i:int = 0
        # Crée un NumberField pour chaque pièce valide
        for piece in VALID_PIECES:
            field = NumberField(inputs, piece)
            #Place le NumberField dans la grille en fonction de Rows
            field.grid(column=i%rows, row=i//rows, pady=10, padx=10)
            field.pad(x=15)
            field._label.configure(font=DEFAULT_FONT)
            #Ajoute le NumberField à la liste
            inputList.append(field)
            i+=1

        #Crée un frame pour les résultats
        resultat = tk.Frame(jeu)
        #Instructions
        resLbl = tk.Label(resultat, text="Clickez sur le bouton pour \n soumettre votre réponse", font="Arial 15")
        resLbl.grid(row=0, column=0, rowspan=2, padx=10, pady=5)
        #Bouton pour soumettre
        btn = tk.Button(resultat, text="Continue", font = DEFAULT_FONT, command=soumets)
        btn.grid(row=0, column=1, padx=10, pady=5)
        #Ajoute les frames à la fenètre
        inputs.grid(row=1, column=0)
        resultat.grid(row=2, column=0)

    #Crée l'application
    app = Application()
    app._lbl.configure(text="Jeu de monnaie")
    app.title("Jeu de monnaie")
    #Crée les frames
    jeu = tk.Frame(app)
    instructions = tk.Frame(app)
    #Instructions avant de commencer le jeu
    lblInst = tk.Label(instructions, text="Une somme d'argent sera présenté. Vous aurez besoin d'indiquer \n le nombre pieces de monnaie requise pour atteindre cette quantité \n d'argent, en utilisant le moins de pieces possibles", font="Arial 15")
    lblInst.grid(row=0, column=0, padx=10, pady=5)
    btnInst = tk.Button(instructions, text="Continuer", font=DEFAULT_FONT, command=commenceJeu)
    btnInst.grid(row=1, column=0, padx=10, pady=5)
    instructions.grid(row=1, column=0)

    #Montre l'application
    app.mainloop()




if __name__ == "__main__":
    main()
