import tkinter as tk

def switchPage2():
    p1.pack_forget()
    p2.pack()

def switchPage1():
    p2.pack_forget()
    p1.pack()


ft = tk.Tk()
ft.geometry("300x300")

p1 = tk.Frame(ft, bg="#55aacc", width=100, height=100)
p1.pack(pady=1, padx=1)

p2 = tk.Frame(ft, bg ="#ccaa55", width=100, height=100)

lblp1 = tk.Label(p1, text="Voici la page 1", font="Arial 15 bold", pady=10, bg = "#55aacc")
lblp1.pack()


btnp1 = tk.Button(p1, text="Page suivante", pady=10, command=switchPage2)
btnp1.pack()

lblp2 = tk.Label(p2, text="Voici la page 2", font="Arial 15 bold", pady=10, bg="#ccaa55")
lblp2.pack()
btnp2 = tk.Button(p2, text="Recommencer", pady=10, command=switchPage1)
btnp2.pack()


ft.mainloop()
