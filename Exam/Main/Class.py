import tkinter as tk






class Application(tk.Tk):
    """
    Application de base. Hérite de tk.Tk, avec l'ajour d'un label titre
    """
    # Constructeur
    def __init__(self, title = ""):
        """Constructeur de la classe Application \n
        @param title: str - Le titre de la fenètre"""
        #Initialise la fenètre
        super().__init__() 
        # Configure le titre
        self._lbl = tk.Label(self, text=title, font="Arial 20 bold")
        self._lbl.grid(row=0, column=0)


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

class NumberField(AnswerField):
    """
    Champ de réponse pour les nombres. Hérite de AnswerField, et ajoute une validation pour les nombres
    """
    # Méthode pour valider les nombres
    def _validate(self, newValue):
        return newValue.isdigit() or newValue == ""

    # Constructeur
    def __init__(self, main, text):
        """Constructeur de la classe NumberField \n
        @param main: tk.Frame - Le frame parent \n
        @param text: str - Le texte du label
        """
        super().__init__(main)
        # Initialise les champs
        self._labelText = text
        self._label.configure(text=text)
        validateCommand = (self.register(self._validate), "%P")
        # Aroute la validation
        self._text.configure(validatecommand=validateCommand, validate="key", justify="center", width=5)
        self._label.configure(text=text, font="Arial 15")

    # Méthode pour obtenir les valeurs
    def get(self):
        return  self._labelText, int(self._text.get() if self._text.get() != "" else 0)

    
    


        
    

