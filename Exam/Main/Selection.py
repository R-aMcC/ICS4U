import tkinter as tk
import Jeu1
import Jeu2
import Resultats
from Utils import *


def main(parent:tk.Tk, jeuRecommande = None, nom = "", enseignant = False):
    oubli(parent, grid=False) # Vide l'écran
    parent.title("Selection")
    mainFt = tk.Frame(parent)
    lblInfo = tk.Label(mainFt, text="Bienvenue! \n Choisissez un jeu pour commencer.", font=("Arial", 20))
    lblInfo.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    if(jeuRecommande != None): # Si un jeu est recommandé
        lblRecommandation = tk.Label(mainFt, text=f"Jeu Recommandé", font=("Arial Italic", 12)) 
        lblRecommandation.grid(row=1, column=jeuRecommande, padx=5, pady=5) # Positionne le au dessus du jeu recommandé

    btnJeu1 = tk.Button(mainFt, text="Jeu de maths", font=("Arial", 15), command=lambda: Jeu1.main(nom, parent)) # Bouton pour le jeu 1
    btnJeu1.grid(row=2, column=0, padx=5, pady=5)
    btnJeu2 = tk.Button(mainFt, text="Jeu de monnaie", font=("Arial", 15), command=lambda: Jeu2.main(nom, parent)) # Bouton pour le jeu 2
    btnJeu2.grid(row=2, column=1, padx=5, pady=5)
    btnResultats = tk.Button(mainFt, text="Voir les résultats", font=("Arial", 15), command=lambda: Resultats.main(nom, parent, enseignant, jeuRecommande)) # Bouton pour voir les résultats
    btnResultats.grid(row=3, column=0, columnspan=2, padx=5, pady=40)


    mainFt.pack(fill=tk.BOTH)