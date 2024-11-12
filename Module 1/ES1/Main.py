"""
-----------------------------------------------------------------------
Auteur: Ryan McCracken
Projet: Jeu de Mathématiques p.2
Date: 2024-10-9
Description: Un launcher pour un de deux jeux dépendant de l'année de 
    l'utilisateur.
-----------------------------------------------------------------------
"""



from Utils import * 
import Jeu1
import Jeu2




#Main toggle du jeu
def main():
    #Vide l'écran et montre un greeting, qui cherche un nom
    vide()
    greeting()
    nom = input("Nom : ")
    #cherche le niveau, en assurant que c'est un nombre entre 0 (maternelle/jardin) et 12
    niveau = chercheNiveau(nom)
    print("-"*50)
    #Si niveau est 2e ou plus bas, choisi jeu 1. Sinon, jeu2.
    if(niveau <=2):
        print("Vous avez pris le premier jeu: Défi de maths.")
        input("Cliquez sur la touche \"Enter\" pour continuer...")
        #Commence jeu1.main
        Jeu1.main()
    else:
        print("Vous avez pris le deuxième jeu: ")
        input("Cliquez sur la touche \"Enter\" pour continuer...")
        #Commence jeu2.main
        Jeu2.main(nom)
    print("-"*50)
    print("Merci d'avoir joué!")
    print("-"*50)




if __name__ == "__main__":
    main()