class Livre:

    def __init__(self, titre, auteur, annee):
        self._titre = titre
        self._auteur = auteur
        self._anneePub = annee
        self._lstLangages = []
    
    def __str__(self):
        return f"Titre: {self._titre} Auteur : {self._auteur} Année de publication : {self._anneePub}"
    
    @property
    def titre(self):
        return self._titre
    
    @property
    def auteur(self):
        return self._auteur
    @property
    def anneePub(self):
        return self._anneePub
    @titre.setter
    def titre(self, titre):
        self._titre = titre
    @auteur.setter
    def auteur(self, auteur) :
        self._auteur = auteur
    @anneePub.setter
    def anneePub(self, annee):
        if annee < 0:
            print("L’année ne peut pas être négatif.")
        else:
            self._anneePub = annee

    def ajout_langage(self, langage) :
        self._lstLangages.append(langage)

    def __len__(self):
        return len(self._lstLangages)
    
    def __getitem__(self, index):
        return self._lstLangages[index]