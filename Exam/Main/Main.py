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
import Selection






#Main toggle du jeu
def main():
    num:int = -1
    nom:str = None

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
            menuPrincipale.pack_forget()
            Selection.main(ft, 0 if int(niveau)<=2 else 1, nom)

        
    
    # Tkinter
    # Fenètre primaire
    ft = tk.Tk()

    ft.geometry("600x500")
    ft.title("Page primaire")

    # Frame 1
    menuPrincipale = tk.Frame(ft)
    menuPrincipale.pack(fill=tk.BOTH, expand=True)

    menuPrincipaleElements = tk.Frame(menuPrincipale)
    menuPrincipaleElements.pack(fill=tk.BOTH, expand=True)
    

    # Infos pour menu principale
    lbltitre = tk.Label(menuPrincipaleElements, text="Bienvenue! \n Entrez votre nom et niveau scolaire pour commencer.", font="Arial 15 bold")
    lbltitre.grid(row=0, column=0, rowspan=2, columnspan=2, padx=5, pady=5)

    lblNom = tk.Label(menuPrincipaleElements, text="Nom :", font="Arial 15")
    lblNom.grid(row=2, column=0, padx=5, pady=20)

    lblNiveau = tk.Label(menuPrincipaleElements, text="Niveau Scolaire :", font="Arial 15")
    lblNiveau.grid(row=3, column=0, padx=5, pady=5)

    txtNom = tk.Entry(menuPrincipaleElements)
    txtNom.grid(row=2, column=1, padx=5, pady=5)

    txtNiveau = tk.Entry(menuPrincipaleElements)
    txtNiveau.grid(row=3, column=1, padx=5, pady=5)

    btnCommence = tk.Button(menuPrincipaleElements, text="Commencer", command=commence, font="Arial 15")
    btnCommence.grid(row=4, column=0, columnspan=2, padx=5, pady=20)

    lblInfo = tk.Label(menuPrincipaleElements, text="" , font="Arial 12 bold")
    lblInfo.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

    btnEnseignant = tk.Button(menuPrincipale, text="Je suis un enseignant", font="Arial 15", command=lambda: Selection.main(ft, nom="enseignant", enseignant=True))
    btnEnseignant.pack(anchor="sw", side="left", padx=10, pady=10)


    

    ft.mainloop()
        





    










if __name__ == "__main__":
    main()
    