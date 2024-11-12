
class Prism():
    #Constructeur
    def __init__(self):
        self._height = 0
        self._aireBase = 0

    #definit l'aire
    def setAire(self, aire):
        self._aireBase = aire
    
    #Retourne l'aire
    def getAire(self):
        return self._aireBase

    #Définit la hauteur
    def setHauteur(self, height):
        self._height = height

    #retourne la hauteur
    def getHauteur(self):
        return self._height
    
    #définit le volume
    def getVolume(self):
        return self.getAire()*self.getHauteur()
    
    #Définit le côté (toujours formes régulier)
    def setSide(self, l):
        pass
    def getSide(self):
        pass




class PrismeCarree(Prism):
    #Définit l'aire avec un coté
    def setSide(self, l):
        self._aireBase = l**2 
    
    #Retourne le coté de l'aire
    def getSide(self):
        return self._aireBase**(1/2)

#Triangle équilatérale comme base
class PrismeTriangle(Prism):
    #Formule pour  l'aire d'un triangle équilatérale
    def setSide(self, l):
        self._aireBase = (l**2)*(3**(1/2))/4
    
    #Formule pour le coté de l'aire
    def getSide(self):
        return (self._aireBase**(1/2))*(3**(3/4))*(2/3)
