import tkinter as tk

def affiche():
    lblTitre.grid(row=0,column=0)
    btnAffiche.configure(state=tk.DISABLED)
    btnCache.configure(state=tk.NORMAL)

def cache():
    lblTitre.grid_forget()
    btnAffiche.configure(state=tk.NORMAL)
    btnCache.configure(state=tk.DISABLED)


ft = tk.Tk()
ft.geometry("200x300")

lblTitre = tk.Label(ft, text="Texte", font="Arial 20 bold", fg="#6ab1b1")
lblTitre.grid(column=0, row=0)

btnAffiche = tk.Button(ft, text="Afichez le texte", font = "Arial 15", command=affiche, state=tk.DISABLED)
btnAffiche.grid(row=1, column=0)

btnCache = tk.Button(ft, text="Cachez le texte", font = "Arial 15", command=cache)
btnCache.grid(row=2, column=0)




ft.mainloop()