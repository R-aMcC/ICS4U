"""
-----------------------------------------------------------------------
Auteur: Ryan McCracken
Projet: Jeu de Mathématiques p.2
Date: 2024-10-9
Description: Utilitées pour les 3 autres fichiers
-----------------------------------------------------------------------
"""





import os
import json
import tkinter as tk


# Cherche un nombre entier de l'utilisateur
def chercheNum(msg, call = True, negatif = True, codes:list[str] = None):
    if(call):
        print(msg)
        inp = input("Entre un nombre entier: ")
    else:
        inp = input(msg)
    #Lorsque l'entrée n'est pas un nombre entier, redemande à l'utilisateur pour un autre nombre
    while not((inp.replace("-", "") if negatif else inp).isdigit()):
        inp = input(f"[ERRUR] {inp} n'est pas un nombre entier. \n{"Réponse" if call else msg} ")
    return int(inp)

def chercheNiveau(nom):
    #Cherche un Niveau scolaire de l'utilisateur
    inp = input("Niveau scolaire : ")
    while not(inp.isdigit()) or int(inp)>12 or int(inp)<0:
        #Assure que l'année est une vraie année
        print("Entre un niveau valide (1-12, 0 pour maternel/jardin)")
        input("Pesez \"Enter\" pour continuer...")
        vide()
        # "Refresh" l'écran avec l'information
        greeting(nom)
        inp = input("Niveau scolaire : ")
    return int(inp)

def greeting(nom = None, niveau = None):
    #Print un greeting. Utile pour remettre l'info sur l'écran après un vide()
    print("-"*50)
    print("Bienvenue !")
    print("Entrez votre nom et niveau scolaire pour commencer.")
    if nom != None:
        print(f"Nom : {nom}") 
    if niveau != None:
        print(f"Niveau : {niveau}")

def vide():
    # Efface l'écran
    os.system('cls' if os.name == 'nt' else 'clear')

def sauvegarde(nom, jeu, resultats):
    # Sauvegarde les résultats dans un fichier JSON
    if(not os.path.exists("resultats.json")):
        with open("resultats.json", "w") as f:
            json.dump([{},{}], f, indent=4) # Crée un fichier vide
    with open("resultats.json", "r+") as f: 
        data = None
        try:
            data = json.load(f) # Charge les résultats
        except ValueError as e:
            if isinstance(e, json.decoder.JSONDecodeError):
                print(f"is instance, message = {e.msg}")
                if(e.msg == "Expecting value"): # Si le fichier est vide
                    data == [{}, {}]
            else:
                raise RuntimeError("Something went wrong")
        f.seek(0)
        f.truncate()
        if(data == None):
            data = [{},{}]
            # Sauvegarde les résultats
            data[jeu][nom] = [{"reussit": resultats[0], "echecs": resultats[1]}]
        elif nom in data[jeu]:
            dataNom:list = data[jeu][nom] # list
            dataNom.append({"reussit": resultats[0], "echecs": resultats[1]})
        else:
            data[jeu][nom] = [{"reussit": resultats[0], "echecs": resultats[1]}]
        json.dump(data, f, indent=4)

def oubli(main, type = tk.Frame, grid = True):
        """Méthode pour oublier les widgets \n
        Oublie tous les widgets de type donné dans une fenètre donnée
        """
        for widget in main.winfo_children():
            if isinstance(widget, type):
                if grid:
                    widget.grid_forget()
                else:
                    widget.pack_forget()