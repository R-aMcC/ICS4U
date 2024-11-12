import tkinter as tk

def isNum(val):
    try:
        float(val)
        return True
    except(ValueError):
        return False

def add():
    val1 = txtVal1.get()
    val2 = txtVal2.get()
    if(not(isNum(val1) and isNum(val2))):
        lblRes.configure(text= "Assure que les deux entrées sont des nombres")
        return
    res = float(val1)+float(val2)
    lblRes.configure(text=f"La somme est {res}")
    

fenetre = tk.Tk()
fenetre.title("Somme")
fenetre.geometry("300x300")


lblBonjour = tk.Label(fenetre, text="Addition",
    font="Times 20 bold",
    fg="#000000",
    wraplength=150,
    padx=50, pady=10)
lblBonjour.pack()

txtVal1 = tk.Entry(fenetre, text="Valeur 1",
    font = "Times 12",
    fg="#000000")
txtVal1.pack()

lblAdd = tk.Label(fenetre, text = "+",
    font="Times 20 bold",
    fg="#000000",
    wraplength=150,
    padx=50, pady=10)
lblAdd.pack()

txtVal2 = tk.Entry(fenetre, text="Valeur 2",
    font = "Times 12",
    fg="#000000")
txtVal2.pack()

btnEnter = tk.Button(fenetre, text = "Go", font = "Times 12", fg="#000000", bg = "#aaaaaa", command=add, pady=10).pack()

lblRes = tk.Label(fenetre, text="Entrez les valeurs et clickez sur le bouton", font="Times 12", fg="#000000", pady = 10)
lblRes.pack()


fenetre.mainloop()