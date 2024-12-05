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
    
    def ajouterLangue(self, langue):
        self._langues.append(langue)  # Ajoute une langue à la liste des langues

    def __getitem__(self, index):
        return self._langues[index]
    
    def __len__(self):
        return len(self._langues)




class LivreFt(tk.Frame):
    def __init__(self, master, livre:Livre):
        super().__init__(master)
        self._livre = livre
        self._lblt = tk.Label(self, text="Titre: ")
        self._lblt.grid(row=0, column=0)
        self._titre = tk.Label(self, text=livre.titre)
        self._titre.grid(row=0, column=1)
        self._lbla = tk.Label(self, text="Auteur: ")
        self._lbla.grid(row=1, column=0)
        self._auteur = tk.Label(self, text=livre.auteur)
        self._auteur.grid(row = 1, column = 1)
        self._lblan = tk.Label(self, text="Annee: ")
        self._lblan.grid(row=2, column=0)
        self._annee = tk.Label(self, text=livre.annee)
        self._annee.grid(row=2, column=1)
        self._lblg = tk.Label(self, text="Genre: ")
        self._lblg.grid(row=3, column=0)
        self._genre = tk.Label(self, text=livre.genre)
        self._genre.grid(row=3, column=1)
        self._lbll = tk.Label(self, text="Langues: ")
        self._lbll.grid(row=4, column=0, sticky="N")
        self._langues = tk.Label(self, text="")
        for langue in livre:
            self._langues.config(text=self._langues.cget("text") + f"{langue}\n")
        self._langues.grid(row=4, column=1)
        self._btn = tk.Button(self, text="Supprimer")
        self._btn.grid(row=5, column=0, columnspan=2)

    @property
    def btn(self) -> tk.Button:
        return self._btn



        