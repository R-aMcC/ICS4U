"""
-------------------------------------------------------------
Auteur: Ryan McCracken
Projet: 1-100

Ce projet prends des valeurs de l'utilisateur j'usqu'il entre 
une commande de sortie, dans {COMMANDES_DE_SORTIE}. Il
prend ensuite la liste de nombres et trouve plusieurs 
données différentes de la liste
-------------------------------------------------------------

"""

# Liste de inputs qui quite le programme
COMMANDES_DE_SORTIE = ["quit", "q", "quitter", "exit", "sort", ""]

#Cherche des nombres ausi longtemps que inp n'est pas une commande de sortie
def prendNombres(max, codes):
    nombres = []
    max = 100
    print(f"{f"Entre un nombre entier entre 1 et {max}.":^48}")
    while True:
        # Appèle une fonction qui assure cherche un nombre. La fonction retourne 
        # EXIT lorsqu'une code de sortie est donnée.
        inp = prendNombre(max, codes,)
        # Vérifie que le nombre est entre 1 et le max (et pas EXIT)
        while(inp !="EXIT" and (int(inp)<1 or int(inp)>max)):
            print(f"[ERREUR] {inp} n'est pas entre 1 et {max}.")
            inp = prendNombre(max, codes)
        
        if(inp == "EXIT"):
            break
        nombres.append(int(inp))
        
    return nombres


def prendNombre(max, codes):
    inp = input(f"NOMBRE: ")
    # Checrche un nombre entier ou une commande de sortie.
    while (not(inp.isdigit()) and not(inp.lower() in codes)):
        inp = input(f"[ERREUR] {inp} n'est pas un nombre entier. \nNOMBRE: ")
    # retourne EXIT si le l'input se figure dans les codes de sortie.
    if(inp.lower() in codes):
        return "EXIT"
    return inp
    
def calculeMoyenne(liste):
    # sum retourne l'adition de toute les items, divise par 2 pour calculer la moyenne)
    return sum(liste)/2

def pairesImpaires(liste):
    paires = []
    impaires = []
    #parcourt tous les éléments de la liste
    for num in liste:
        # si num%2 == 0, le nombre est paire, alors on l'ajoute au nombres paires, sinon 
        # c'est impaire et on l'ajoute au nombres impaires
        if num%2 == 0:
            paires.append(num)
        else:
            impaires.append(num)
    # Retourne deux éléments: la longeur des nombre paires, la longeur des nombres impaires
    return len(paires), len(impaires)
    
def chercheMode(liste):
    # Créé un nouveau dictionaire vide
    # EXEMPLE:
    # dict = {Key1:Value, Key2:Value}
    counts = {}
    for num in liste:
        # Si l'élément n'existe pas, créé le avec une valeur de 1
        # Si elle éxiste, augmente la valeur par 1
        if(counts.get(num) == None):
            counts[num] = 1
        else:
            counts[num] += 1
    try:
        #retourne le Key de l'élément avec le Value le plus élévé
        return max(counts, key=counts.get)
    except:
        #Si ceci faillit, il n'y a aucun élément dans le dictionaire
        return None


def chercheMediane(liste):
    #Organise la liste en ordre du plus petit au plus élevé
    liste.sort()
    grandeur = len(liste)
    # Si la longeur de la liste est de 0, la liste est vide.
    if grandeur == 0:
        return None
    # Si la longeur de la liste est impaire, on peut prendre l'élément centrale
    # Sinon, il faut trouver la moyenne des deux éléments
    if grandeur%2 != 0:
        #Prends le point millieu
        return liste[int(grandeur/2-0.5)]
    else:
        #Prend élément avant et après le centre
        return (liste[int(grandeur/2)]+liste[int(grandeur/2)-1])/2


def main():
    print(f"\n {"| Instructions |":-^48} \n")
    print(f"{"Entre des numéros entre 1 et 100. Le code":^48}")
    print(f"{"Prends ensuite les nombres et retourne de":^48}")
    print(f"{"l'information à propos des éléments de la":^48}")
    print(f"{"liste. Elle calcule le nombre d'éléments,":^48}")
    print(f"{"le nombre d'éléments paires et impaires,":^48}")
    print(f"{"et le mode et  la moyenne de l'ensemble.":^48}")
    print(f"{"Pour quitter, entre un des codes de sortie":^48} \n")
    print(f"{"| Codes de sortie |":-^48}")
    for code in COMMANDES_DE_SORTIE:
        if code != "":
            print(f"- {code}")
        else:
            print("- (vide)")
    print("-"*48)
    nombres = prendNombres(100, COMMANDES_DE_SORTIE)
    paire, impaire = pairesImpaires(nombres)
    mode = chercheMode(nombres)
    mediane = chercheMediane(nombres)
    print(f"{"| Résultats |":-^48}")
    print(f"- Grandeur de la liste: {len(nombres):>24}")
    print(f"- Nombres paires: {paire:>30}")
    print(f"- Nombres impaires: {impaire:>28}")
    print(f"- Mode de l'ensemble: {mode if mode!= None else "Aucun":>26}")
    print(f"- Médiane de l'ensemble: {"Aucun" if mediane==None else int(mediane) if str(mediane).endswith("0") else mediane:>23}")
    print("-"*48)

main()
