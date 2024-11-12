"""
-------------------------------------------------------------
Auteur: Ryan McCracken
Projet: Rendre la monnaie

Ce projet prends une valeur décimale et imprime la quantité 
d'argent à remettre. (nombre de 2$, 1$, 25¢, 10¢, 5¢) 
Si aucune valeur est donné, un nombre aléatoire entre 0.05
et 10.00 sera utilisé à sa place  
-------------------------------------------------------------
"""

import random
import tkinter as tk




def monnaie():
    return random.randint(5, 1000)/100

pieces = {"2.00$": 200, 
          "1.00$": 100,
          "0.25$":  25,
          "0.10$":  10, 
          "0.05$":   5}


def pieces_monnaie(prix):
    prix = int((prix+4)/5)*5
    pieces_recus = {}
    for piece in pieces:
        valeur = pieces[piece]
        tmpN = prix // valeur
        pieces_recus[piece] = tmpN
        prix -= tmpN*valeur
    
    return pieces_recus

def estNombre(inp):
    try:
        tmp = float(inp)
        return True
    except:
        return False
    
def checheNombre(msg):
    while True:
        inpA = input(msg)
        if(inpA == ""):
            val = monnaie()
            print(f"Prix aléatoire: {val}")
            return val
        elif(estNombre(inpA)):
            return float(inpA)
        else:
            print("[ERREUR] Pas un nombre réel")




        
def main():
    print("-"*39)
    print (f"{" Calcul de monnaie ":-^39}")
    print("-"*39)

    print("\nEntre un prix. Si aucun prix est donné\n   un nombre aléatoire sera utilisé   \n")

    prix = checheNombre("PRIX: ")*100
    totale = 0
    print()
    print(f"{"*** Arrondis vers le haut ***":^39}")
    print()
    pieces_recus = pieces_monnaie(prix)
    for piece in pieces_recus:
        n = int(pieces_recus[piece])
        totale += n*pieces[piece]
        print(f"{piece}{n:>34}")
    print(f"TOTALE: {f"{format(totale/100, ".2f")}$":>31}")
    print("-"*39)


def tmp():
    print("Test")


#Tout le code pouur le GUI
fenetre = tk.Tk()
fenetre.title("Monnaie")
fenetre.geometry("700x500")
fenetre.configure(bg="#4444bb")

lblTitre = tk.Label(fenetre, text="Monnaie", font="Arial 20", bg="#4444bb", fg="#ffffff")
lblTitre.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

lblMonnaie = tk.Label(fenetre, text="Quantité d'argent: 0.00$",bg="#4444bb", fg="#ffffff", font="Arial 17")
lblMonnaie.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

lbl5 = tk.Label(fenetre, text="0.05$ :", bg="#4444bb", fg="#ffffff", font="Arial 15")
lbl5.grid(row=2, column=0, pady=5)

txt5 = tk.Entry(fenetre)
txt5.grid(row=2, column=1, pady=5)

lbl10 = tk.Label(fenetre, text="0.10$ :", bg="#4444bb", fg="#ffffff", font="Arial 15")
lbl10.grid(row=3, column=0, pady=5)

txt10 = tk.Entry(fenetre)
txt10.grid(row=3, column=1, pady=5)

lbl25 = tk.Label(fenetre, text="0.25$ :", bg="#4444bb", fg="#ffffff", font="Arial 15")
lbl25.grid(row=4, column=0, pady=5)

txt25 = tk.Entry(fenetre)
txt25.grid(row=4, column=1, pady=5)

lbl100 = tk.Label(fenetre, text="1.00$ :", bg="#4444bb", fg="#ffffff", font="Arial 15")
lbl100.grid(row=5, column=0, pady=5)

txt100 = tk.Entry(fenetre)
txt100.grid(row=5, column=1, pady=5)

lbl200 = tk.Label(fenetre, text="2.00$ :", bg="#4444bb", fg="#ffffff", font="Arial 15")
lbl200.grid(row=6, column=0, pady=5)

txt200 = tk.Entry(fenetre)
txt200.grid(row=6, column=1, pady=5)

btnGo = tk.Button(fenetre, width=15, text="Vérifier", font="Arial 15", command=tmp)
btnGo.grid(row=7, column=0, columnspan=2, pady=10)



def main2():
    fenetre.mainloop()




if __name__ == "__main__":
    #main()
    main2()

