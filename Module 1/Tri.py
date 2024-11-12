import time
import random

def tri(liste:list) -> list:
    for i in range(len(liste)-1):
        max = liste[len(liste)-i-1]
        for ii in range(len(liste)-i):
            if liste[ii] > max:
                max = liste[ii]
        liste.remove(max)
        liste.insert(len(liste)-i, max)
    return liste


def insere(element, liste:list):
    i = 0
    while i<len(liste) and liste[i]<element:
        i+=1 
    liste.insert(i, element)
    return liste


def inseretri(liste:list):
    for i in  range(len(liste)):
        liste = insere(liste.pop(i), liste)    
    return liste
   


#liste1 = [3, 2, 4, 6, 5, 7, 2, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 1]
#tri(liste1)

#liste2 = [1, 2, 4, 6, 7, 8]
#print(insere(5, liste2))

#liste3 = [1, 4, 2, 7, 9, 9, 2, 5, 3]
#print(liste3)
#print(inseretri(liste3))


def main():
    nombres = []
    for i in range(100000):
        nombres.append(random.randint(1, 100))

    tempsDepart = time.time()
    nombresSelection = tri(nombres.copy())
    tempsSelection = time.time()-tempsDepart

    #tempsDepart = time.time()
    #nombresInsertion = inseretri(nombres.copy())
    #tempsInsertion = time.time() - tempsDepart

    print(f"Le tri par sélection a pris {tempsSelection} secondes a s'exécuter")
    #print(f"Le tri par insertion a pris {tempsInsertion} secondes a s'exécuter")
    


if __name__ == "__main__":
    main()

