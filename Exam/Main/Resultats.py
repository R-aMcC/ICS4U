from Utils import *
import json
import os
import tkinter as tk



def main(nom:str, parent, enseignant):
    def details(data, frame, btn):
        btn.grid_forget()
        print(data)
        ft = tk.Frame(frame)
        ft.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        i = 0
        for element in data:
            lblRes = tk.Label(ft, text=f"Note: {int(element['reussit']/(element['reussit']+element['echecs'])*100)}% \n Questions réussies: {element["reussit"]} Questions échouées {element["echecs"]}", font=("Arial", 12))
            lblRes.grid(row=i, column=0, padx=5, pady=5)
            i+=1

        btnAnnuler = tk.Button(ft, text="Annuler", font=("Arial", 12), command=lambda: btn.grid(row=2, column=0, columnspan=2, padx=5, pady=5))
        btnAnnuler.grid(row=i, column=0, columnspan=2, padx=5, pady=5)

        
    nom = nom.lower()
    data = load()
    oubli(parent, grid=False)

    parent.geometry("")
    ft = tk.Frame(parent)
    ft.pack()
    lblTitre = tk.Label(ft, text="Résultats", font=("Arial", 20))
    lblTitre.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    res1 = tk.Frame(ft)
    res1.grid(row=1, column=0, padx=5, pady=5, sticky="n")

    lblTitre1 = tk.Label(res1, text="Jeu de Maths", font=("Arial", 15))
    lblTitre1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    ftResultats1 = tk.Frame(res1, borderwidth=1, relief="solid", highlightbackground="#bbbbbb", highlightthickness=1)
    ftResultats1.grid(row=1, column=0, padx=5, pady=5)

    if(nom in data[0]):
        reussit = 0
        echecs = 0

        for resultat in data[0][nom]:
            reussit += resultat["reussit"]
            echecs += resultat["echecs"]

        lblMoyenne = tk.Label(ftResultats1, text=f"Moyenne: {int(reussit/(reussit+echecs)*100)}%", font=("Arial", 12))
        lblMoyenne.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        lblReussit = tk.Label(ftResultats1, text=f"Questions réussies: {reussit}", font=("Arial", 12))
        lblReussit.grid(row=1, column=0, padx=5, pady=5)
        lblEchecs = tk.Label(ftResultats1, text=f"Questions échouées: {echecs}", font=("Arial", 12))
        lblEchecs.grid(row=1, column=1, padx=5, pady=5)

        btnDetails = tk.Button(ftResultats1, text="Détails", font=("Arial", 12))
        btnDetails.configure(command=lambda btnDetails = btnDetails: details(data[0][nom], ftResultats1, btnDetails))
        btnDetails.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    else:
        lblInfo = tk.Label(ftResultats1, text="Aucun résultat trouvé", font=("Arial", 12))
        lblInfo.grid(row=2, column=0, columnspan=2, padx=5, pady=5)




    res2 = tk.Frame(ft)
    res2.grid(row=1, column=1, padx=5, pady=5, sticky="n")

    lblTitre2 = tk.Label(res2, text="Jeu de Monnaie", font=("Arial", 15))
    lblTitre2.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    ftResultats2 = tk.Frame(res2, borderwidth=1, relief="solid", highlightbackground="#bbbbbb", highlightthickness=1)
    ftResultats2.grid(row=1, column=0, padx=5, pady=5)

    if(nom in data[1]):
        reussit = 0
        echecs = 0

        for resultat in data[1][nom]:
            reussit += resultat["reussit"]
            echecs += resultat["echecs"]

        lblMoyenne = tk.Label(ftResultats2, text=f"Moyenne: {int(reussit/(reussit+echecs)*100)}%", font=("Arial", 12))
        lblMoyenne.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        lblReussit = tk.Label(ftResultats2, text=f"Questions réussies: {reussit}", font=("Arial", 12))
        lblReussit.grid(row=1, column=0, padx=5, pady=5)
        lblEchecs = tk.Label(ftResultats2, text=f"Questions échouées: {echecs}", font=("Arial", 12))
        lblEchecs.grid(row=1, column=1, padx=5, pady=5)
        btnDetails = tk.Button(ftResultats2, text="Détails", font=("Arial", 12))
        btnDetails.configure(command=lambda btnDetails = btnDetails: details(data[1][nom], ftResultats2, btnDetails))
        btnDetails.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    else:
        lblInfo = tk.Label(ftResultats2, text="Aucun résultat trouvé", font=("Arial", 12))
        lblInfo.grid(row=2, column=0, columnspan=2, padx=5, pady=5)



    







def load():
    if(not os.path.exists("resultats.json")):
        with open("resultats.json", "w") as f:
            json.dump([{},{}], f, indent=4)
    
    with open("resultats.json", "r") as f:
        data = json.load(f)
        return data
        