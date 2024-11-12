# Ryan McCracken, 2024/09/09


import math


def printAire(name, area):
    print(f"L'aire du {name} est de {round(area, 2)} unitées carrée")

def aireTriangle(b, h):
    printAire("triangle", b*h/2)
def aireCercle(r):
    printAire("cercle", math.pi*math.pow(r, 2))
def aireRectangle(b, h):
    printAire("rectangle", b*h)
def airSquare(c):
    printAire("carré", math.pow(c, 2))
def aireTrapeze(pb, gb, h):
    printAire("trapèzoïde", ((pb+gb)/2)*h)

def isNum(inp):
    try:
        tmp = float(inp)
        return True
    except:
        return False
    
def getNum(msg):
    while True:
        inpA = input(msg)
        if(isNum(inpA)):
            return float(inpA)
        else:
            print("[ERREUR] Pas un nombre réel")



print("""
      OPTIONS:
        Triangle
        Cercle
        Rectangle
        Carré
        Trapèzoïde
      """)

def findArea():
    while True:
        aType = input("Choisis une figure geométrique pour calculer l'aire \nCHOIX: ")
        match aType.lower():
            case "triangle":
                aireTriangle(getNum("BASE: "), getNum("HAUTEUR: "))
                break
            case "cercle":
                aireCercle(getNum("RAYON: "))
                break
            case "rectangle":
                aireRectangle(getNum("BASE: "), getNum("HAUTEUR: "))
                break
            case "carré":
                airSquare(getNum("COTÉ"))
                break
            case "Trapèzoïde":
                aireTrapeze(getNum("BASE 1: "), getNum("BASE 2:"), getNum("HAUTEUR"))
                break
            case _:
                print("Option non reconnue.")


findArea()
            