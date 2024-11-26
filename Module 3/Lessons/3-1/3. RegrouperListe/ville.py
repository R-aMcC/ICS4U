class Ville:
    def __init__(self, nom, pays):
        self._nom = nom
        self._pays = pays
            
    def __str__(self):
        return f"Ville: {self._nom}, Pays : {self._pays}"
            
    @property
    def nom(self):
        return self._nom
            
    @nom.setter
    def nom(self, nom) :
        self._nom = nom
            
    @property
    def pays(self):
        return self._pays
            
    @pays.setter
    def pays(self, pays) :
        return self._pays