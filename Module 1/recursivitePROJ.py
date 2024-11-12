import time
import sys

def fois(a, b):
    # addittion a avec elle meme b fois, recursivement
    if b < 0:
        #si b est négtif, il faut l'inverser
        return -fois(a, -b)
    return a + fois(a, b-1) if b > 1 else a if b != 0 else 0




# Comme toujours, cette fonction cherche un nombre réel
def chercheNombre(msg):
    inp = input(msg)
    while not inp.replace("-", "").isdigit():
        inp = input("Entre un nombre entier: ")
    return int(inp) 


def main():
    print("Entre 2 nombres pour les multiplier")
    #Chercher les nombres
    val1 = chercheNombre("Nombre 1: ")
    val2 = chercheNombre("Nombre 2: ")
    #fait le calcul
    ans = fois(val1, val2)
    print(f"Le produit de {val1} et {val2} est {ans}")

#Vérifier si le fichier est le fichier principal
if __name__ == "__main__":
    main()

