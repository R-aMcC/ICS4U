import tkinter as tk
import json
import Livre
from AnswerField import AnswerField

livres = {}

def main():
    ft = tk.Tk()
    ft.title("Bibliothèque")
    ft.geometry("800x800")
    FTLivres = tk.Frame(ft)
    lblLivre = tk.Label(ft, text="Livres", font=("Arial Bold", 20))

    def ajouter():
        def ajouterLivre(titre, auteur, annee, genre, langues: str,):
            if titre == "" or auteur == "" or annee == "" or genre == "" or langues == "":
                return
            livre = Livre.Livre(titre, auteur, annee, genre)
            for langue in langues.split(","):
                livre.ajouteLangue(langue.strip())
            livres[titre] = livre
            saufegarde()
            afficher()
            FTAdj.grid_forget()
            base.grid(row=1, column=0, padx=10, pady=10)
        FTAdj = tk.Frame(ft)
        lblAdj = tk.Label(FTAdj, text="Ajouter un livre", font=("Arial", 20))
        lblAdj.grid(row=0, column=0, columnspan=2, pady=10)
        lblInfo = tk.Label(FTAdj, text="Remplis toute les informations. \n Sépare les langues par des virgules.")
        lblInfo.grid(row=1, column=0)        
        # Crée des champs de saisie pour les détails du livre
        ansTitre = AnswerField(FTAdj) 
        ansTitre.label = "Titre"
        ansTitre.grid(row=2, column=0)
        ansAuteur = AnswerField(FTAdj)
        ansAuteur.label = "Auteur"
        ansAuteur.grid(row=3, column=0)
        ansAnnee = AnswerField(FTAdj)
        ansAnnee.label = "Annee"
        ansAnnee.grid(row=4, column=0)
        ansGenre = AnswerField(FTAdj)
        ansGenre.label = "Genre"
        ansGenre.grid(row=5, column=0)
        ansLangue = AnswerField(FTAdj)
        ansLangue.label = "Langues"
        ansLangue.grid(row=6, column=0)
        # Bouton pour ajouter le livre
        btnAjouter = tk.Button(FTAdj, text="Ajouter", command=lambda: ajouterLivre(ansTitre.get(), ansAuteur.get(), ansAnnee.get(), ansGenre.get(), ansLangue.get()))
        btnAjouter.grid(row=7, column=0, pady=10)
        FTAdj.grid(row=2, column=0, padx=10, pady=10)

    
        
        



    def enlever():
        FTenlever = tk.Frame(ft)
        lblEnlever = tk.Label(FTenlever, text="Enlever un livre", font=("Arial", 20))
        lblEnlever.grid(row=0, column=0, columnspan=2, pady=10)
        lblInfo = tk.Label(FTenlever, text="Sélectionne un livre à enlever")
        lblInfo.grid(row=1, column=0, columnspan=2)
        for i, (key, value) in enumerate(livres.items()):
            lbl = tk.Label(FTenlever, text=value.titre)
            lbl.grid(row=i+2, column=0)
            btn = tk.Button(FTenlever, text="Enlever", command=lambda key=key: enleverLivre(key))
            btn.grid(row=i+2, column=1)
        FTenlever.grid(row=2, column=0, padx=10, pady=10)

    def enleverLivre(key):
        pass

    
    
    def afficher():    
        nonlocal FTLivres
        FTLivres.destroy()
        canvas = tk.Canvas(ft, width=750, height=400)
        scrollbar = tk.Scrollbar(ft, orient="vertical", command=canvas.yview)
        FTLivres = tk.Frame(canvas)
        FTLivres.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=FTLivres, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.grid(row=1, column=0, padx=10, pady=10)
        scrollbar.grid(row=1, column=4, sticky="ns")
        lblLivre.grid(row=0, column=0, columnspan=3, pady=10)
        FTLivres.columnconfigure([0, 1, 2], weight=1, minsize=250)
        livres = load()
        livreObjs = {}
        for i, (key, value) in enumerate(livres.items()):
            livreObj = Livre.LivreFt(FTLivres, value)
            livreObj.grid(row=i//3+1, column=i%3, sticky="nsew", padx=10, pady=10)
            livreObjs[key] = livreObj


        def scroll(event: tk.Event):
            if len(livreObjs) > 6:
                canvas.yview_scroll(-1*(event.delta//120), "units")
        canvas.bind_all("<MouseWheel>", scroll)





    afficher()
    base = tk.Frame(ft)
    lblBVN = tk.Label(base, text="Bienvenue", font=("Arial", 20))
    lblBVN.grid(row=0, column=0, columnspan=2, pady=10)
    btn1 = tk.Button(base, text="ajouter", command=ajouter) 
    btn1.grid(row=1, column=0, pady=5, padx=5)
    btn2 = tk.Button(base, text="enlever", command=enlever)
    btn2.grid(row=1, column=1, pady=5, padx=5)
    base.grid(row=2, column=0, padx=10, pady=10)



    
    ft.mainloop()

def load():
    try:
        with open("biblio.json", "r") as f:
            data = json.load(f)
            for livre in data:
                tmp = Livre.Livre(livre["titre"], livre["auteur"], livre["annee"], livre["genre"])
                for langue in livre["langues"]:
                    tmp.ajouteLangue(langue)
                livres[tmp.titre] = tmp
    except FileNotFoundError:
        print("Fichier introuvable")
    finally:
        return livres
    

def saufegarde():
    with open("biblio.json", "w") as f:
        json.dump([livre.toJson() for livre in livres.values()], f, indent=4)
    
    



if __name__ == "__main__":
    main()