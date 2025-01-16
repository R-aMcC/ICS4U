from Utils import *
import json
import os
import tkinter as tk
import Selection


def main(nom:str, parent, enseignant, jeu):
    nom = nom.lower() # Assure que le nom est en minuscule
    data = load() # Prends les donées du fichier
    oubli(parent, grid=False) # Vide l'écran
    parent.title("Résultats") # Change le titre de la fenêtre
    parent.geometry("1075x750") # Change la taille de la fenêtre
    ft = tk.Frame(parent) 
    ft.pack()
    lblTitre = tk.Label(ft, text="Résultats", font=("Arial", 20))
    lblTitre.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    canvas = tk.Canvas(ft) # Canvas pour le scrolling
    canvas.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    sb = tk.Scrollbar(ft, orient="vertical", command=canvas.yview) #Sccrollbar
    sb.grid(row = 1, column=2, sticky="ns")
    ftRes = tk.Frame(canvas)
    ftRes.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))) #Fait le scrolling fonctionner
    canvas.create_window((0,0), window=ftRes, anchor="nw")
    canvas.configure(width=1025, height=600, yscrollcommand=sb.set)
    def scroll(event: tk.Event):
        canvas.yview_scroll(-1*(event.delta//120), "units")

    def enter(event): # Ajoute le scroll quand la souris est sur le canvas
            event.widget.bind_all("<MouseWheel>", scroll)

    def leave(event): # Enlève le scroll quand la souris n'est plus sur le canvas
        event.widget.unbind_all("<MouseWheel>")
    canvas.bind("<Enter>", enter) # Ajoute les événements
    canvas.bind("<Leave>", leave) # Ajoute les événements





    res1 = tk.Frame(ftRes) #Écran pour les résultats du jeu de maths
    res1.grid(row=0, column=0, padx=5, pady=5, sticky="n")

    lblTitre1 = tk.Label(res1, text="Jeu de Maths", font=("Arial", 15))
    lblTitre1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    ftResultats1 = tk.Frame(res1, borderwidth=1, relief="solid")
    ftResultats1.grid(row=1, column=0, padx=5, pady=5)

    res2 = tk.Frame(ftRes) # Écran pour les résultats du jeu de monnaie
    res2.grid(row=0, column=1, padx=5, pady=5, sticky="n")

    lblTitre2 = tk.Label(res2, text="Jeu de Monnaie", font=("Arial", 15))
    lblTitre2.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    ftResultats2 = tk.Frame(res2, borderwidth=1, relief="solid", highlightbackground="#bbbbbb", highlightthickness=1)
    ftResultats2.grid(row=1, column=0, padx=5, pady=5)

    if enseignant: # Si le bouton enseignant est pèsé, montre toute les résultats
        moyennes1 = []
        moyennes2 = []
        i = 0
        for nom in data[0]: 
            # Montre les résultats pour chaque élève du jeu 1
            ftEleve = tk.Frame(ftResultats1, borderwidth=1, relief="solid")
            ftEleve.columnconfigure([0, 1], minsize=200)
            ftResultats = tk.Frame(ftEleve)
            moyenne = chercheResultats(data, nom, 0, ftResultats) # Montre les résultats
            moyennes1.append(moyenne)
            lblNom = tk.Label(ftEleve, text=f"Nom: {nom.capitalize()}", font=("Arial", 12))
            lblNom.grid(row=0, column=0, padx=5, pady=5)

            lblMoyenne = tk.Label(ftEleve, text=f"Moyenne: {moyenne}%", font=("Arial", 12))
            lblMoyenne.grid(row=0, column=1, padx=5, pady=5)


            btnDetails = tk.Button(ftEleve, text="Détails", font=("Arial", 12), command=lambda frame = ftResultats: show(frame, 1, 0, 2))
            btnDetails.grid(row=0, column=2, padx=5, pady=5)

            ftEleve.grid(row=i+1, column=0, padx=5, pady=5, sticky="nsew")
            i+=1
        lblMoyenne1 = tk.Label(ftResultats1, text=f"Moyenne de la classe: {int(sum(moyennes1)/len(moyennes1))}%", font=("Arial", 12)) # Montre la moyenne de la classe
        lblMoyenne1.grid(row=0, column=0, columnspan=3, padx=25, pady=25)

        j = 0
        for nom in data[1]:
            # Montre les résultats pour chaque élève du jeu 2
            ftEleve = tk.Frame(ftResultats2, borderwidth=1, relief="solid", width=500, height=50)
            ftEleve.columnconfigure([0, 1], minsize=200)
            ftResultats = tk.Frame(ftEleve)
            moyenne = chercheResultats(data, nom, 1, ftResultats) # Montre les résultats
            moyennes2.append(moyenne)
            lblNom = tk.Label(ftEleve, text=f"Nom: {nom.capitalize()}", font=("Arial", 12))
            lblNom.grid(row=0, column=0, columnspan=1, padx=5, pady=5)

            lblMoyenne = tk.Label(ftEleve, text=f"Moyenne: {moyenne}%", font=("Arial", 12))
            lblMoyenne.grid(row=0, column=1, padx=5, pady=5)

            btnDetails = tk.Button(ftEleve, text="Détails", font=("Arial", 12), command=lambda frame = ftResultats: show(frame, 1, 0, 2))
            btnDetails.grid(row=0, column=2, padx=5, pady=5)

            ftEleve.grid(row=j+1, column=0, padx=5, pady=5, sticky="nsew")
            j+=1
        lblMoyenne2 = tk.Label(ftResultats2, text=f"Moyenne de la classe: {int(sum(moyennes2)/len(moyennes2))}%", font=("Arial", 12)) # Montre la moyenne de la classe
        lblMoyenne2.grid(row=0, column=0, columnspan=3, padx=25, pady=25)
        
    else:
        chercheResultats(data, nom, 0, ftResultats1) #Montre les résultats de l'élève seulement si ce n'est pas un enseignant
        chercheResultats(data, nom, 1, ftResultats2) #Jeu 2


    btnBack = tk.Button(ft, text="Retour", command=lambda nom=nom, parent=parent, enseignant=enseignant: Selection.main(parent, jeu, nom, enseignant), font="Arial 15")
    btnBack.grid(row=2, column=0, columnspan=2, padx=5, pady=15)

def annuler(btn, frame):
    frame.grid_forget() # Enlève le frame
    btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5) # Remet le bouton
        

def details(data, frame, btn):
    # Montre les détails des résultats
    btn.grid_forget()
    ft = tk.Frame(frame)
    ft.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    i = 0
    for element in data:
        # Montre les résulats par essaie
        lblRes = tk.Label(ft, text=f"Note: {int(element['reussit']/(element['reussit']+element['echecs'])*100)}% \n Questions réussies: {element["reussit"]} Questions échouées {element["echecs"]}", font=("Arial", 12))
        lblRes.grid(row=i, column=0, padx=5, pady=5)
        i+=1

    btnAnnuler = tk.Button(ft, text="Annuler", font=("Arial", 12), command=lambda btn=btn: annuler(btn, ft))
    btnAnnuler.grid(row=i, column=0, columnspan=2, padx=5, pady=5)

def show(frame:tk.Frame, row, column, columnspan):
    #Montre ou cache un frame selon si il est déjà montré
    gridInfo = frame.grid_info()
    if gridInfo:
        frame.grid_forget()
    else:
        frame.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)

def chercheResultats(data, nom, jeu, parent):
    if(nom in data[jeu]): # Si le nom est dans les résultats
        reussit = 0
        echecs = 0

        for resultat in data[jeu][nom]: # Pour chaque résultat, ajoute les réussites et les échecs
            reussit += resultat["reussit"]
            echecs += resultat["echecs"]

        lblMoyenne = tk.Label(parent, text=f"Moyenne: {int(reussit/(reussit+echecs)*100)}%", font=("Arial", 12)) # Moyenne
        lblMoyenne.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        lblReussit = tk.Label(parent, text=f"Questions réussies: {reussit}", font=("Arial", 12)) # Réussites
        lblReussit.grid(row=1, column=0, padx=5, pady=5)
        lblEchecs = tk.Label(parent, text=f"Questions échouées: {echecs}", font=("Arial", 12)) # Échecs
        lblEchecs.grid(row=1, column=1, padx=5, pady=5)

        btnDetails = tk.Button(parent, text="Détails", font=("Arial", 12))
        btnDetails.configure(command=lambda btnDetails = btnDetails: details(data[jeu][nom], parent, btnDetails))
        btnDetails.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        return int(reussit/(reussit+echecs)*100) # Retourne la moyenne
    else:
        lblInfo = tk.Label(parent, text="Aucun résultat trouvé", font=("Arial", 12)) # Si il n'y a pas de résultat
        lblInfo.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        return -1
    





# Cherche les résultats du fichier
def load():
    if(not os.path.exists("resultats.json")): # Si le fichier n'existe pas, crée le
        with open("resultats.json", "w") as f:
            json.dump([{},{}], f, indent=4)
    
    with open("resultats.json", "r") as f: # Ouvre le fichier
        data = json.load(f) # Prends les données
        return data # Retourne les données