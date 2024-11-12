import tkinter as tk
import idlelib.tooltip as info
from time import sleep

def aideF1(event):
    aide()


def aide():
    lblMsg.configure(text="Ceci est un message d'aide")
    

ft = tk.Tk()
ft.geometry("300x200")


btnAide = tk.Button(ft, text="Aide", command=aide)
btnAide.pack()

lblMsg = tk.Label(ft, pady=15)
lblMsg.pack()

inf  = info.Hovertip(btnAide, "Cliquez pour de l'aide")
ft.bind('<F1>', aideF1)


ft.mainloop()
