import tkinter as tk
import json
import Livre
from AnswerField import AnswerField

livres = {}

def main():
    # Crée la fenêtre principale, intitulée "Bibliothèque"
    ft = tk.Tk()
    ft.title("Bibliothèque")
    ft.geometry("820x820")
    ft.columnconfigure(0, minsize=820)

    FTMain = tk.Frame(ft) # (Contiendra le canvas de livre et titres)
    FTMain.grid(row=0, column=0)
    FTLivres = tk.Frame(FTMain) # Ici ce tiendra tous les livres
    lblLivre = tk.Label(FTMain, text="Livres", font=("Arial Bold", 20)) # Titre
    
    def forget(widget):
        """
        Méthode pour revenir à l'écran d'accueil
        widget: Le widget à oublier
        """
        widget.grid_forget()
        base.grid(row=2, column=0, padx=10, pady=10)

    def ajouter():
        """
        Méthode pour créer le menu pour ajouter un livre
        """


        def ajouterLivre(titre, auteur, annee, genre, langues: str,):
            """
            Méthode qui ajoute le livre.
            """
            if titre == "" or auteur == "" or annee == "" or genre == "" or langues == "":
                return
            livre = Livre.Livre(titre, auteur, annee, genre) # Créé l'élément
            for langue in langues.split(","): # Ajoute les languages
                livre.ajouteLangue(langue.strip()) #Assure aucun "Trailing space"
            livres[titre] = livre # Ajoute le livre dans le dictionaire
            sauvegarde() # Saufegarde la liste
            afficher() # "Refresh" l'écran
            forget(FTAdj) # Retourne à l'écran d'accueil
        
        FTAdj = tk.Frame(ft) # Élément qui contient toute les Text Boxs pour l'ajout d'un livre
        lblAdj = tk.Label(FTAdj, text="Ajouter un livre", font=("Arial", 20)) # Titre
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
        btnAnnuler = tk.Button(FTAdj, text="Annuler", command=lambda: forget(FTAdj)) # Bouton pour annuler (retour au menu principale)
        btnAnnuler.grid(row=7, column=1, pady=10)
        FTAdj.grid(row=2, column=0, padx=10, pady=10)

    
        
        



    def enlever():
        """
        Méthode pour enlever un livre de la bibliothèque
        """
        FTenlever = tk.Frame(ft) # Cadre parent qui contiennt tout les éléments
        lblEnlever = tk.Label(FTenlever, text="Enlever un livre", font=("Arial", 20)) # Titre
        lblEnlever.grid(row=0, column=0, columnspan=2, pady=10)
        lblInfo = tk.Label(FTenlever, text="Sélectionne un livre à enlever") # Intrucctions
        lblInfo.grid(row=1, column=0, columnspan=2)
        

        canvas = tk.Canvas(FTenlever, width=750, height=150) # Canvas pour les livres. Canvas est utilisé pour laisse l'utilisateur "scroll" si il y a trops d'éléments
        scrollbar = tk.Scrollbar(FTenlever, orient="vertical", command=canvas.yview) # Scrollbar pour le canvas
        FTList = tk.Frame(canvas) # Cadre qui contient les livres
        FTList.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))) # Controle le bounding du scroll pour le canvas
        canvas.create_window((0, 0), window=FTList, anchor="nw") # Ajoure le cadre au canvas
        canvas.configure(yscrollcommand=scrollbar.set) # Configure le scrollbar pour montrer la position du canvas
        canvas.grid(row=2, column=0, padx=10, pady=10)
        scrollbar.grid(row=2, column=1, sticky="ns")
        livresENLVObj = {}
        for i, (key, value) in enumerate(livres.items()): # Crée un élément pour chaque livre
            livreENLV = Livre.LivreENLV(FTList, value)
            livreENLV.grid(row=i//3+2, column=i%3, pady=10, padx=10) # Place l'élément dans le cadre, 3 éléments par ligne
            livresENLVObj[key] = livreENLV
            livreENLV.btnElever = lambda key=key: enleverLivre(key) # Ajoute la méthode pour enlever le livre
        
        btnAnnuler = tk.Button(FTenlever, text="Annuler", command=lambda: forget(FTenlever)) # Bouton qui retoure à l'écran d'accueil
        btnAnnuler.grid(row=3, column=0, pady=10)

        
        FTenlever.grid(row=2, column=0, padx=10, pady=10)


        def scroll(event: tk.Event):
            if len(livresENLVObj) > 6: # Si il y a plus de 6 éléments, permet le scroll
                canvas.yview_scroll(-1*(event.delta//120), "units") # Scroll le canvas


        def enter(event): # Ajoute le scroll quand la souris est sur le canvas
            event.widget.bind_all("<MouseWheel>", scroll)

        def leave(event): # Enlève le scroll quand la souris n'est plus sur le canvas
            event.widget.unbind_all("<MouseWheel>")

        canvas.bind("<Enter>", enter) # Ajoute les événements
        canvas.bind("<Leave>", leave) # Ajoute les événements
        
        def enleverLivre(key):
            if key in livres: # Si l'élément est dans le dictionaire, enlève le
                del livres[key]
                sauvegarde() # saufgarde le nouveau dictionaire dans le fichier
                afficher() # "Refresh" l'écran
                forget(FTenlever) # Retourne à l'écran d'accueil

    

    
    
    def afficher():    
        """
        Méthode qui affiche toute les livres dans l'écran principale
        """
        nonlocal FTLivres
        FTLivres.destroy() # Enlève les éléments précédents
        canvas = tk.Canvas(FTMain, width=750, height=400) #défini le canvas
        scrollbar = tk.Scrollbar(FTMain, orient="vertical", command=canvas.yview) # Défini le scrollbar
        FTLivres = tk.Frame(canvas) # créé le cadre pour les livres
        FTLivres.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))) # Ajoute le bounding pour le scroll
        canvas.create_window((0, 0), window=FTLivres, anchor="nw") # Ajoute le cadre au canvas, ancré en haut à gauche
        canvas.configure(yscrollcommand=scrollbar.set) # Configure le scrollbar pour montrer la position du canvas
        canvas.grid(row=1, column=0, padx=10, pady=10)
        scrollbar.grid(row=1, column=4, sticky="ns")
        lblLivre.grid(row=0, column=0, columnspan=3, pady=10)
        FTLivres.columnconfigure([0, 1, 2], weight=1, minsize=250) # Configure les colonnes pour les livres - Asure qu'ils sont de la même taille
        livres = load() # Cherche les livres du fichier
        livreObjs = {}
        for i, (key, value) in enumerate(livres.items()): # Ajoute un élément pour chaque livre, 3 par ligne
            livreObj = Livre.LivreFt(FTLivres, value)
            livreObj.grid(row=i//3+1, column=i%3, sticky="nsew", padx=10, pady=10) # Ancre les au centre et ajoute un padding
            livreObjs[key] = livreObj


        def scroll(event: tk.Event):
            if len(livreObjs) > 6: # Scroll si le nombre d'éléments est adéquat (6)
                canvas.yview_scroll(-1*(event.delta//120), "units")


        def enterLivres(event): # Ajoute le scroll quand la souris est sur le canvas
            event.widget.bind_all("<MouseWheel>", scroll)

        def leaveLivres(event): # Enlève le scroll quand la souris n'est plus sur le canvas
            event.widget.unbind_all("<MouseWheel>")
        canvas.bind("<Enter>", enterLivres) # Ajoute les événements
        canvas.bind("<Leave>", leaveLivres) # Ajoute les événements





    afficher()
    base = tk.Frame(ft) # Écrans de base
    lblBVN = tk.Label(base, text="Bienvenue", font=("Arial", 20))
    lblBVN.grid(row=0, column=0, columnspan=2, pady=10)
    btn1 = tk.Button(base, text="Ajouter un livre", command=ajouter) # Bouton pour ajouter un livre
    btn1.grid(row=1, column=0, pady=5, padx=5)
    btn2 = tk.Button(base, text="Enlever un livre", command=enlever) # Bouton pour enlever un livre
    btn2.grid(row=1, column=1, pady=5, padx=5)
    base.grid(row=2, column=0, padx=10, pady=10)



    
    ft.mainloop()

def load():
    """
    Méthode pour charger les livres du fichier
    """
    try:
        with open("biblio.json", "r") as f: # Assure aucun memory leak en cas d'erreur en ouvrant le fichier uniquement dans cette boucle
            data = json.load(f) # Charge les données dans un élément JSON (Liste d'éléments)
            for livre in data: # Pour chaque élément dans la liste
                tmp = Livre.Livre(livre["titre"], livre["auteur"], livre["annee"], livre["genre"]) # Créé un objet Livre de l'élément
                for langue in livre["langues"]: # Pour chaque langue
                    tmp.ajouteLangue(langue) # AJoute la langue à l'objet
                livres[tmp.titre] = tmp
    except FileNotFoundError: # Si le fichier n'existe pas
        print("Fichier introuvable")
    finally:  # Retourne le dictionaire de livres
        return livres
    

def sauvegarde():
    """
    Méthode pour enregistrer les livres dans le fichier
    """
    with open("biblio.json", "w") as f: # Ouvre le fichier en écriture
        json.dump([livre.toJson() for livre in livres.values()], f, indent=4) # Écrit les livres dans le fichier, en suivant le formatage JSON
        # Pour chaque élément dans le dictionaire, prend sa valuer, qui est l'objet, et le convertit en JSON
        # avec la méthode créé. Écrit ensuite ces éléments dans un fichier, avec un "Pretty print" indent de 4
    
    



if __name__ == "__main__":
    main()