import tkinter as tk




class Color():
    def __init__(self, f):
        self._r = tk.IntVar()
        self._radR = tk.Checkbutton(f, text="rouge", onvalue=1, offvalue=0, font="Arial 15", variable=self._r)
        self._radR.pack()
        self._g = tk.IntVar()
        self._radG = tk.Checkbutton(f, text="vert ", onvalue=2, offvalue=0, font="Arial 15", variable=self._g)
        self._radG.pack()
        self._b = tk.IntVar()
        self._radB = tk.Checkbutton(f, text="bleu ", onvalue=4, offvalue=0, font="Arial 15", variable=self._b)
        self._radB.pack()

    def getColor(self):
        val = self._r.get()+self._g.get()+self._b.get()
        match(val):
            case 0:
                return "Black", "#000000"
            case 1:
                return "Red", "#FF0000"
            case 2:
                return "Green", "#00FF00"
            case 3:
                return "Yellow", "#FFFF00"
            case 4:
                return "Blue", "#0000FF"
            case 5:
                return "Magenta", "#FF00FF"
            case 6:
                return "Cyan", "#00FFFF"
            case 7:
                return "White", "#FFFFFF"
    
def changeColor():
    name, color = c.getColor()
    btn1.configure(text=name, bg=color)


ft = tk.Tk()

cadre1 = tk.Frame(ft)
cadre1.pack()
c = Color(cadre1)





btn1 = tk.Button(ft, text="TEST", bg = "#FFFFFF", command=changeColor)
btn1.pack()

ft.mainloop()