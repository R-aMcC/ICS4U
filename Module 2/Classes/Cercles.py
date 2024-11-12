import math
class Cercle:
    rayon:float

    def __init__(self):
        self._rayon = 0
    
    def setRayon(self, rayon):
        if rayon >=0:
            self._rayon = rayon
        else:
            print("Le rayon ne peut pas être négatif")
    
    def getRayon(self):
        return self._rayon

    def setDiametre(self, diameter):
        if diameter >=0:
            self.setRayon(diameter/2)
        else:
            print("Le diamètre ne peut pas être négatif")

    def getDiametre(self):
        return self.getRayon()/2
    
    def aire(self):
        return self.getRayon()**2*math.pi
    
    def circonference(self):
        return self.getRayon()*2*math.pi
    

def main():
    cercle = Cercle()
    print(" - Calculs sur un cercle -")
    rayon = float(input("Entre le rayon : "))
    cercle.setRayon(rayon)
    print(f"diamètre = {cercle.getDiametre(): .2f}")
    print(f"circonférence = {cercle.circonference(): .2f}")
    print(f"aire = {cercle.aire(): .2f}")

if __name__ == "__main__":
    main()

