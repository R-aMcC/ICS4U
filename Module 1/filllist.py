import random

def remplirListe(n,a,b):
    liste = []
    for i in range(n):
        liste.append(random.randint(a, b))
    return liste
      
def minListe(l):
    return min(l)


nb = int(input("Combien de nombres au hasard voulez-vous choisir? "))

nombresHasard = remplirListe(nb,1,10)
print(nombresHasard)

min = minListe(nombresHasard)
print(f"Le plus petit nombre de la liste est {min}.")