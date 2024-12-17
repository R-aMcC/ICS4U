import tkinter as tk

class AnswerField(tk.Frame):
    """
    Classe de base pour les champs de réponse. Hérite de tk.Frame, et ajour un label avec un champ de texte
    """
    #Constructeur
    def __init__(self, main):
        """Constructeur de la classe AnswerField \n
        @param: main: tk.Frame - Le frame parent"""
        super().__init__(main)
        # Initialise les champs
        self._label =  tk.Label(self)
        self._label.grid(row=0, column=0, padx=5, pady=5)
        self._text = tk.Entry(self)
        self._text.grid(row=0, column=1, padx=5, pady=5)


    # Méthode pour ajouter du padding
    def pad(self, x = 0, y=0):
        self._label.grid(padx= x, pady= y)
        self._text.grid(padx= x, pady=y)

    @property
    def label(self):
        return self._label.cget("text")
    
    @label.setter
    def label(self, label):
        self._label.config(text=label)


    def get(self):
        return self._text.get()