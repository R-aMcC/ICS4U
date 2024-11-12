import tkinter as tk


class Application(tk.Tk):
    def __init__(self, title = ""):
        super().__init__() 
        self._lbl = tk.Label(self, text=title, font="Arial 20 bold")
        self._lbl.grid(row=0, column=0)


class AnswerField(tk.Frame):
    def __init__(self, main):
        super().__init__(main)
        self._label =  tk.Label(self)
        self._label.grid(row=0, column=0, padx=5, pady=5)
        self._text = tk.Entry(self)
        self._text.grid(row=0, column=1, padx=5, pady=5)

    def pad(self, x = 0, y=0):
        self._label.grid(padx= x, pady= y)
        self._text.grid(padx= x, pady=y)

class NumberField(AnswerField):

    def _validate(self, newValue):
        return newValue.isdigit() or newValue == ""


    def __init__(self, main, text):
        super().__init__(main)
        self._labelText = text
        validateCommand = (self.register(self._validate), "%P")
        value = tk.IntVar()
        self._text.configure(validatecommand=validateCommand, validate="key", justify="center", width=5)
        self._text.insert(0, "0")
        self._label.configure(text=text, font="Arial 15")

    def get(self):
        return  self._labelText, int(self._text.get())


class Results(tk.Frame):
    def __init__(self, main, win:bool):
        super().__init__(main)
        if win:
            self._label = tk.Label(self, text="Bravo! \n Vous avez donné la bonne réponse!", font="Arial 15")
        else:
            self._label = tk.Label(self, text="Uh oh! \n Vous n'avez pas donné la bonne réponse!", font="Arial 15")
        self._label.grid(row=0, column=0, rowspan=2, padx=10, pady=5)
        self._btn = tk.Button(self, text="Confirme", font="Arial 15")
        self._btn.grid(row=0, column=1, padx=10, pady=5)

    def setCommand(self, command):
        self._btn.configure(command=command)
    
    


        
    

