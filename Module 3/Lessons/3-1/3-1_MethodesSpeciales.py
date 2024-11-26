class Personne:

    def __init__(self, prenom, age):
        self._prenom = prenom
        self._age = age
        self._passeTemps = []
              
    def __str__(self):
        return f"{self._prenom} est agé de {self._age} ans."
              
    def __len__(self):
        return len(self._passeTemps)
              
    def __getitem__(self, position):
        return (self._passeTemps[position])
              
    def ajout_PasseT(self, passetemps) :
        self._passeTemps.append(passetemps)
              
# programme principal
personne1 = Personne("Michel", 15)
              
# ajouter des passetemps à Michel
personne1.ajout_PasseT("Jeux vidéo")
personne1.ajout_PasseT("Soccer")
print(personne1)
print(f"Nombre de passe-temps : {len(personne1)}")
for passetemps in personne1 :
    print(passetemps)