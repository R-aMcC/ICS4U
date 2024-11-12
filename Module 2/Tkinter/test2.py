import tkinter as tk

def calcule():
    h = float(txtHauteur.get())
    b = float(txtBase.get())
    lblAns.configure(text=f"L'aire du triangle est : {b*h/2}")



fenetre = tk.Tk()
fenetre.title("Aire d'un triangle")
fenetre.geometry("1000x500")
fenetre.configure(bg = "#639999")


lblHauteur = tk.Label(fenetre, text="Hauteur : ", bg = "#639999", fg="#ffffff", font="Arial 14")
lblHauteur.grid(column=1, row=0, padx=5, pady=5)

lblBase = tk.Label(fenetre, text="Base : ", bg = "#639999", fg = "#ffffff", font="Arial 14")
lblBase.grid(column=1, row=1, padx=5, pady=5)

lblAns = tk.Label(fenetre, text="Remplis les valeur et cliquez \n sur le bouton pour calculer",
    bg="#639999", fg="#ffffff", font="Arial 14", padx=50, pady=10)
lblAns.grid(column=0, row=3, columnspan=3, padx=5, pady=5)

txtHauteur = tk.Entry(fenetre, font="Arial 14", width=20)
txtHauteur.grid(column=2, row=0, pady=5)

txtBase = tk.Entry(fenetre,font="Arial 14")
txtBase.grid(column=2, row=1, pady=5)

btnCalcule = tk.Button(fenetre, text="Calculer", font="Arial 14", command=calcule, width=19)
btnCalcule.grid(column=2, row=2, pady=5)

fenetre.mainloop()