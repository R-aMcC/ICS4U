import tkinter as tk
import json
import Livre
from AnswerField import AnswerField

livres = {}

def main():
    ft = tk.Tk()
    ft.title("Bibliothèque")
    ft.geometry("820x820")
    ft.columnconfigure(0, minsize=820)
    FTMain = tk.Frame(ft)
    FTMain.grid(row=0, column=0)
    FTLivres = tk.Frame(FTMain)
    lblLivre = tk.Label(FTMain, text="Livres", font=("Arial Bold", 20))
    
    def forget(widget):
        widget.grid_forget()
        base.grid(row=2, column=0, padx=10, pady=10)

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
        lblInfo.grid(row=1, column=0, columnspan=2)        
        # Crée des champs de saisie pour les détails du livre
        ansTitre = AnswerField(FTAdj) 
        ansTitre.label = "Titre"
        ansTitre.grid(row=2, column=0, columnspan=2)
        ansAuteur = AnswerField(FTAdj)
        ansAuteur.label = "Auteur"
        ansAuteur.grid(row=3, column=0, columnspan=2)
        ansAnnee = AnswerField(FTAdj)
        ansAnnee.label = "Annee"
        ansAnnee.grid(row=4, column=0, columnspan=2)
        ansGenre = AnswerField(FTAdj)
        ansGenre.label = "Genre"
        ansGenre.grid(row=5, column=0, columnspan=2)
        ansLangue = AnswerField(FTAdj)
        ansLangue.label = "Langues"
        ansLangue.grid(row=6, column=0, columnspan=2)
        # Bouton pour ajouter le livre
        btnAjouter = tk.Button(FTAdj, text="Ajouter", command=lambda: ajouterLivre(ansTitre.get(), ansAuteur.get(), ansAnnee.get(), ansGenre.get(), ansLangue.get()))
        btnAjouter.grid(row=7, column=0, pady=10)
        btnAnnuler = tk.Button(FTAdj, text="Annuler", command=lambda: forget(FTAdj))
        btnAnnuler.grid(row=7, column=1, pady=10)
        FTAdj.grid(row=2, column=0, padx=10, pady=10)

    
        
        



    def enlever():
        FTenlever = tk.Frame(ft)
        lblEnlever = tk.Label(FTenlever, text="Enlever un livre", font=("Arial", 20))
        lblEnlever.grid(row=0, column=0, columnspan=2, pady=10)
        lblInfo = tk.Label(FTenlever, text="Sélectionne un livre à enlever")
        lblInfo.grid(row=1, column=0, columnspan=2)
        

        canvas = tk.Canvas(FTenlever, width=750, height=150)
        scrollbar = tk.Scrollbar(FTenlever, orient="vertical", command=canvas.yview)
        FTList = tk.Frame(canvas)
        FTList.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=FTList, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.grid(row=2, column=0, padx=10, pady=10)
        scrollbar.grid(row=2, column=1, sticky="ns")
        livresENLVObj = {}
        for i, (key, value) in enumerate(livres.items()):
            livreENLV = Livre.LivreENLV(FTList, value)
            livreENLV.grid(row=i//3+2, column=i%3, pady=10, padx=10)
            livresENLVObj[key] = livreENLV
            livreENLV.btnElever = lambda key=key: enleverLivre(key)
        
        btnAnnuler = tk.Button(FTenlever, text="Annuler", command=lambda: forget(FTenlever))
        btnAnnuler.grid(row=3, column=0, pady=10)

        
        FTenlever.grid(row=2, column=0, padx=10, pady=10)


        def scroll(event: tk.Event):
            if len(livresENLVObj) > 6:
                canvas.yview_scroll(-1*(event.delta//120), "units")


        def enter(event):
            event.widget.bind_all("<MouseWheel>", scroll)

        def leave(event):
            event.widget.unbind_all("<MouseWheel>")

        canvas.bind("<Enter>", enter)
        canvas.bind("<Leave>", leave)
        
        def enleverLivre(key):
            if key in livres:
                del livres[key]
                saufegarde()
                afficher()
                forget(FTenlever)

    

    
    
    def afficher():    
        nonlocal FTLivres
        FTLivres.destroy()
        canvas = tk.Canvas(FTMain, width=750, height=400)
        scrollbar = tk.Scrollbar(FTMain, orient="vertical", command=canvas.yview)
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


        def enterLivres(event):
            event.widget.bind_all("<MouseWheel>", scroll)

        def leaveLivres(event):
            event.widget.unbind_all("<MouseWheel>")
        canvas.bind("<Enter>", enterLivres)
        canvas.bind("<Leave>", leaveLivres)





    afficher()
    base = tk.Frame(ft)
    lblBVN = tk.Label(base, text="Bienvenue", font=("Arial", 20))
    lblBVN.grid(row=0, column=0, columnspan=2, pady=10)
    btn1 = tk.Button(base, text="Ajouter un livre", command=ajouter) 
    btn1.grid(row=1, column=0, pady=5, padx=5)
    btn2 = tk.Button(base, text="Enlever un livre", command=enlever)
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