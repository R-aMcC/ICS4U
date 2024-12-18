import tkinter as tk

class Livre:
    
    def __init__(self, titre, auteur, annee, genre):
        self._titre = titre
        self._auteur = auteur
        self._annee = annee
        self._genre = genre
        self._langues = []  # Initialise la liste des langues

    @property
    def titre(self):
        return self._titre
    
    @titre.setter
    def titre(self, titre):
        self._titre = titre
    
    @property 
    def auteur(self):
        return self._auteur
    
    @auteur.setter
    def auteur(self, auteur):
        self._auteur = auteur
    
    @property
    def annee(self):
        return self._annee
    
    @annee.setter
    def annee(self, annee):
        if annee < 0:
            print("L’année ne peut pas être négatif.")  # Vérifie que l'année n'est pas négative
        else:
            self._annee = annee

    @property
    def genre(self):
        return self._genre
    
    @property
    def langues(self):
        return self._langues
    
    def ajouteLangue(self, langue):
        self._langues.append(langue)  # Ajoute une langue à la liste des langues
    
    def __getitem__(self, index):
        return self._langues[index]
    
    def __len__(self):
        return len(self._langues)
    
    def toJson(self):
        return {
            "titre": self._titre,
            "auteur": self._auteur,
            "annee": self._annee,
            "genre": self._genre,
            "langues": self._langues
        }
    def __str__(self):
        return f"{self._titre} de {self._auteur} ({self._annee})"



class LivreFt(tk.Frame):
    def __init__(self, master, livre: Livre):
        super().__init__(master, width=250, height=150, borderwidth=1, relief="solid")

        self.pack_propagate(False)
        self._livre:Livre = livre
        self._livreDict = self._livre.toJson()
        self.columnconfigure(0, weight=0, minsize=100)
        self.columnconfigure(1, weight=1)


        self._elements = {}
        for i, (key, value) in enumerate(self._livreDict.items()):
            if(key == "langues"):
                lblTitre = tk.Label(self, text="Langues:", width=10, anchor="w")
                lblContent = tk.Label(self, text="\n".join(value), justify=tk.LEFT, wraplength=120, anchor="w")
            else:
                niceKey = self.getNicerKey(key)
                lblTitre = tk.Label(self, text=niceKey, width=10, anchor="w")
                lblContent = tk.Label(self, text=value, justify=tk.LEFT, wraplength=120, anchor="w")   
            lblTitre.grid(row=i, column=0, sticky="NW", padx = 7, pady=2)
            lblContent.grid(row=i, column=1, sticky="NW")
            self._elements[key] = (lblTitre, lblContent)     


    @staticmethod
    def getNicerKey(key: str):
        return key.capitalize()+": "
    
class LivreENLV(tk.Frame):
    def __init__(self, master, livre:Livre):
        super().__init__(master, relief="solid", borderwidth=1)
        #self.columnconfigure(0, weight=0, minsize=100)
        #self.columnconfigure(1, weight=1)
        self._livre = livre
        self._lblTitre = tk.Label(self, text=livre.titre, width=20, anchor="w", wraplength=100, padx=5, pady=5)
        self._btnElever = tk.Button(self, text="Enlever", width=7, padx=5, pady=5)
        self._lblTitre.grid(row=0, column=0)
        self._btnElever.grid(row=0, column=1)
    
    @property
    def livre(self):
        return self._livre

    @property
    def btnElever(self):
        return self._btnElever

    @btnElever.setter
    def btnElever(self, command):
        self._btnElever.configure(command=command) 

    

    




        
        


        