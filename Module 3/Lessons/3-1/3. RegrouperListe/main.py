import ville as v

lstVilles = []

lstVilles.append(v.Ville("Ottawa", "Canada"))
lstVilles.append(v.Ville("Toronto", "Canada"))
lstVilles.append(v.Ville("Montréal", "Canada"))
lstVilles.append(v.Ville("Paris", "France"))
lstVilles.append(v.Ville("Londres", "Angleterre"))
lstVilles.append(v.Ville("Berlin", "Allemagne"))
lstVilles.append(v.Ville("Rome", "Italie"))
lstVilles.append(v.Ville("Tokyo", "Japon"))
lstVilles.append(v.Ville("Pékin", "Chine"))
lstVilles.append(v.Ville("Sydney", "Australie"))
lstVilles.append(v.Ville("Le Caire", "Égypte"))
lstVilles.append(v.Ville("Moscou", "Russie"))

for ville in lstVilles:
    print(ville)