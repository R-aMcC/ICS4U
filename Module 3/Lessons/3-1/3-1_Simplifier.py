class Ecole:
    def __init__(self, nom, population):
        self._nom = nom
        self._population = population

    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self, nom):
        self._nom = nom

    @property
    def population(self):
        return self._population
    
    @population.setter
    def population(self, population):
        if population < 0:
            print("La population ne peut pas être négative.")
        else:
            self._population = population

# programme principal
ecole1 = Ecole("Pierre-Savard", 1276)
print(f"L’école {ecole1.nom} a une population de {ecole1.population} élèves.")
ecole1.population = -100 