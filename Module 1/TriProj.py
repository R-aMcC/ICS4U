import random
import time
import sys

def listeHasard(quantite, min = 1, max = 10):
    liste = []
    for i in range(quantite):
        liste.append(random.randint(min, max))
    return liste

def chercheNum(msg, vals:list[int] = None):
    inp = input(msg)
    #Lorsque l'entrée n'est pas un nombre entier, redemande à l'utilisateur pour un autre nombre
    while True:
        while not(inp.replace("-", "").isdigit()):
            inp = input(f"[ERRUR] {inp} n'est pas un nombre entier. \nRéponse: ")
        if vals== None or int(inp) in vals:
            break
        inp = input(f"[ERREUR] {inp} n'est pas l'un des option permis. \nRéponse:")
    return int(inp)

def quickSort(liste, l, h, ordre):
    if(l<h):
        p = partition(liste, l, h, ordre)

        quickSort(liste, l, p-1, ordre)
        quickSort(liste, p+1, h, ordre)

def partition(liste, l, h, ordre):
    pivot = liste[h]
    i = l - 1
    if ordre == 1:
        for j in range(l, h):
            if liste[j] < pivot:
                i += 1
                liste[i], liste[j] = liste[j], liste[i]
    elif ordre == 2:
        for j in range(l, h):
            if liste[j] > pivot:
                i += 1
                liste[i], liste[j] = liste[j], liste[i]
    liste[i + 1], liste[h] = liste[h], liste[i + 1]
    return i + 1





def main():
    print(f"{"Trie une liste de nombres au hasard":-^50}")
    q = chercheNum("Combien de nombres veux-tu générer? : ")
    min = chercheNum(" - plus petit nombre à générer : ")
    max = chercheNum(" - plus grand nombre à générer :")
    print("Dans quel ordre veux-tu tirer la liste?")
    print(" 1. Ordre croissant")
    print(" 2. Ordre décroissant")
    ordre = chercheNum("Choix (1 ou 2): ", [1, 2])
    nombres = listeHasard(q, min, max)
    nombresTire = nombres.copy()
    t = time.time()
    nombresSORT = nombres.copy().sort()
    tfs = time.time()-t
    t = time.time()
    quickSort(nombresTire, 0, len(nombresTire)-1, ordre)
    tf = time.time()-t
    print(f"Liste original: \n{nombres}")
    print(f"Liste tirée: \n{nombresTire}")
    print(f"Temps: {tf} secondes")
    print(f"Temps: (liste.sort()) {tfs} secondes")
    




if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    main()
    sys.setrecursionlimit(1000)
