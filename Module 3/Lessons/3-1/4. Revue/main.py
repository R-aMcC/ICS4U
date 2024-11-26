import Livre as l

def main():
    lstLivres = []
    lstLivres.append(l.Livre("Harry Potter", "J.K. Rowling", 1997))
    lstLivres[0].ajout_langage("Français")
    lstLivres[0].ajout_langage("Anglais")
    lstLivres.append(l.Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1954))
    lstLivres[1].ajout_langage("Français")
    lstLivres[1].ajout_langage("Anglais")
    lstLivres.append(l.Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943))
    lstLivres[2].ajout_langage("Français")
    lstLivres.append(l.Livre("Le Code Da Vinci", "Dan Brown", 2003))
    lstLivres[3].ajout_langage("Français")
    lstLivres[3].ajout_langage("Anglais")
    lstLivres.append(l.Livre("Le Journal d'Anne Frank", "Anne Frank", 1947))
    lstLivres[4].ajout_langage("Français")
    lstLivres[4].ajout_langage("Anglais")
    lstLivres[4].ajout_langage("Allemand")


    for livre in lstLivres:
        print(livre)
        for langage in livre:
            print(langage)


if __name__ == "__main__":
    main()