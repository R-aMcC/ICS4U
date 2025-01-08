import tkinter as tk
import Jeu1
import Jeu2
from Utils import *


def main(parent:tk.Tk, jeuRecommande, nom):
    mainFt = tk.Frame(parent)

    lblInfo = tk.Label(mainFt, text="Bienvenue! \n Choisissez un jeu pour commencer.", font=("Arial", 20))
    lblInfo.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    lblRecommandation = tk.Label(mainFt, text=f"Jeu Recommandé", font=("Arial Italic", 12))
    lblRecommandation.grid(row=1, column=jeuRecommande, padx=5, pady=5)

    btnJeu1 = tk.Button(mainFt, text="Jeu de Maths", font=("Arial", 15), command=lambda: Jeu1.main(nom))
    btnJeu1.grid(row=2, column=0, padx=5, pady=5)
    btnJeu2 = tk.Button(mainFt, text="Jeu de Monnaie", font=("Arial", 15), command=lambda: Jeu2.main(nom))
    btnJeu2.grid(row=2, column=1, padx=5, pady=5)

    mainFt.pack(fill=tk.BOTH)

