"""
-----------------------------------------------------------------------
Auteur: Ryan McCracken
Projet: Jeu de Mathématiques p.2
Date: 2024-10-9
Description: Un launcher pour un de deux jeux dépendant de l'année de 
    l'utilisateur.
-----------------------------------------------------------------------
"""


import tkinter as tk
from Utils import * 
import Jeu1
import Jeu2






#Main toggle du jeu
def main():
    num:int = -1
    nom:str = None
    def commenceJeu():
        #Quite le fenètre tkinter
        ft.destroy()
        if(num == 0):
            #commence jeu 1
            Jeu1.main()
        else:
            #commence jeu 2
            Jeu2.main(nom)

    def commence():
        #Cherche les données
        nonlocal num
        nonlocal nom    
        niveau = txtNiveau.get()
        nom = txtNom.get()
        #Assure que le numéro est valide
        if(not(niveau.isdigit() and (int(niveau)<=12 and int(niveau)>=0))):
            lblInfo.configure(text="Assurez vous que \"Niveau \" est un niveau valide. \n (0-12, 0 pour maternelle/jardin)")
        else:
            #Change de menu
            lblInfo.configure(text="")
            menuPrincipale.pack_forget()
            menuAvantJeu.pack()
            if(int(niveau)<=2):
                #Commence jeu 1 après le bouton
                lblPrejeu.config(text=f"Bonjour {nom}! \n Vous avez pris le premier jeu: Défi de maths. \n Cliquez sur le bouton pour commencer")
                num = 0
            else:
                #commende jeu 2 après le bouton
                lblPrejeu.config(text=f"Bonjour {nom}! \n Vous avez pris le deuxième jeu: Calcul de monnaie. \n Cliquez sur le bouton pour commencer")
                num = 1

        
    
    # Tkinter
    # Fenètre primaire
    ft = tk.Tk()
    ft.geometry("600x500")
    ft.title("Page primaire")
    ft.configure(bg="#bbbbbb")

    # Frame 1
    menuPrincipale = tk.Frame(ft, bg="#bbbbbb")
    menuPrincipale.pack(fill=tk.BOTH)

    # Frame 2
    menuAvantJeu = tk.Frame(ft, bg="#bbbbbb")

    # Infos pour menu principale
    lbltitre = tk.Label(menuPrincipale, text="Bienvenue! \n Entrez votre nom et niveau scolaire pour commencer.", font="Arial 15 bold", bg="#bbbbbb")
    lbltitre.grid(row=0, column=0, rowspan=2, columnspan=2, padx=5, pady=5)

    lblNom = tk.Label(menuPrincipale, text="Nom :", font="Arial 15", bg="#bbbbbb")
    lblNom.grid(row=2, column=0, padx=5, pady=20)

    lblNiveau = tk.Label(menuPrincipale, text="Niveau Scolaire :", font="Arial 15", bg="#bbbbbb")
    lblNiveau.grid(row=3, column=0, padx=5, pady=5)

    txtNom = tk.Entry(menuPrincipale)
    txtNom.grid(row=2, column=1, padx=5, pady=5)

    txtNiveau = tk.Entry(menuPrincipale)
    txtNiveau.grid(row=3, column=1, padx=5, pady=5)

    btnCommence = tk.Button(menuPrincipale, text="Commencer", command=commence, font="Arial 15")
    btnCommence.grid(row=4, column=0, columnspan=2, padx=5, pady=20)

    lblInfo = tk.Label(menuPrincipale, text="" , font="Arial 12 bold", bg="#bbbbbb")
    lblInfo.grid(row=5, column=0, columnspan=2, padx=5, pady=10)


    # Info pour menu préjeu
    lblPrejeu = tk.Label(menuAvantJeu, bg="#bbbbbb", font="Arial 15 bold", padx=5, pady=15)
    lblPrejeu.grid(row=0, column=0, columnspan=3, rowspan=3)

    btn2 = tk.Button(menuAvantJeu, text= "Commencer", font = "Arial 15 bold", padx=5, pady=10, command=commenceJeu)
    btn2.grid(row=4, column=1)
    ft.mainloop()
        





    










if __name__ == "__main__":
    main()
    