import Livre as l
import tkinter as tk
import json
from AnswerField import AnswerField



# Fonction pour supprimer un livre de la liste et mettre à jour l'interface utilisateur
def suprimmerLivre(livres:list[l.Livre], livre:l.Livre, ft, ftlivres, livresobj):
    livres.remove(livre)  # Supprime le livre de la liste
    saufgarder(livres)  # Sauvegarde la liste mise à jour dans un fichier
    updateLivres(ft, livres, ftlivres, livresobj)  # Met à jour l'interface utilisateur avec la nouvelle liste
    return livres

# Fonction pour mettre à jour l'interface utilisateur avec la liste des livres
def updateLivres(master, livres:list[l.Livre], ftLivresOG=None, livresobjOG=None):
    ftLivres = tk.Frame(master)  # Crée un nouveau cadre pour les livres
    livresobj = []  # Liste pour contenir les widgets des livres
    i = 0
    for livre in livres:
        lblLivre = l.LivreFt(ftLivres, livre)  # Crée un widget pour chaque livre
        lblLivre.grid(row=i//2, column=i%2, padx=10, pady=10)  # Dispose les widgets dans une grille
        
        # Définit la commande pour le bouton de suppression pour supprimer le livre spécifique
        lblLivre.btn.configure(command=lambda livre=livre: suprimmerLivre(livres, livre, master, ftLivres, livresobj))
        livresobj.append(lblLivre)  # Ajoute le widget à la liste
        i += 1

    if ftLivresOG is not None:
        ftLivresOG.grid_forget()  # Cache l'ancien cadre
    ftLivres.grid(row=0, column=0)  # Affiche le nouveau cadre

    if livresobjOG is not None:
        livresobjOG.clear()  # Vide l'ancienne liste de widgets
        livresobjOG.extend(livresobj)  # Met à jour avec la nouvelle liste de widgets

    return ftLivres, livresobj

# Fonction pour sauvegarder la liste des livres dans un fichier
def saufgarder(livres:list[l.Livre]):
    data = []
    for livre in livres:
        data.append(livre.toJson())  # Convertit chaque livre en JSON
    with open("biblio.json", "w") as f:
        json.dump(data, f)  # Écrit les données JSON dans un fichier

def main():
    # Fonction pour ajouter un nouveau livre
    def addLivre():
        def soummettre():
            # Récupère les détails du livre à partir des champs de saisie
            titre = ansTitre.get()
            auteur = ansAuteur.get()
            annee = ansAnnee.get()
            genre = ansGenre.get()
            langues = ansLangue.get().split(",")
            livre = l.Livre(titre, auteur, annee, genre)  # Crée un nouvel objet livre
            for langue in langues:
                livre.ajouterLangue(langue)  # Ajoute les langues au livre
            livres.append(livre)  # Ajoute le livre à la liste
            ftLivres, livresobj = updateLivres(ft, livres)  # Met à jour l'interface utilisateur avec la nouvelle liste
            ftLivres.grid(row=0, column=0)  # Affiche la liste mise à jour
            ftAdd.destroy()  # Ferme la fenêtre d'ajout de livre
        
        # Crée une nouvelle fenêtre pour ajouter un livre
        ftAdd = tk.Toplevel(ft)
        lblInfo = tk.Label(ftAdd, text="Ajouter un livre \n Remplis toute les informations. \n Sépare les langues par des virgules.")
        lblInfo.grid(row=0, column=0)
        
        # Crée des champs de saisie pour les détails du livre
        ansTitre = AnswerField(ftAdd) 
        ansTitre.label = "Titre"
        ansTitre.grid(row=1, column=0)
        ansAuteur = AnswerField(ftAdd)
        ansAuteur.label = "Auteur"
        ansAuteur.grid(row=2, column=0)
        ansAnnee = AnswerField(ftAdd)
        ansAnnee.label = "Annee"
        ansAnnee.grid(row=3, column=0)
        ansGenre = AnswerField(ftAdd)
        ansGenre.label = "Genre"
        ansGenre.grid(row=4, column=0)
        ansLangue = AnswerField(ftAdd)
        ansLangue.label = "Langues"
        ansLangue.grid(row=5, column=0)

        # Crée un bouton de soumission pour ajouter le livre
        btnSoummettre = tk.Button(ftAdd, text="Soummettre", command=soummettre)
        btnSoummettre.grid(row=6, column=0)

        ftAdd.mainloop()  # Démarre la boucle d'événements pour la fenêtre d'ajout de livre

    # Charge les livres depuis le fichier JSON
    with open("biblio.json", "r") as f:
        data = json.load(f)
        livres = []
        for livre in data:
            livres.append(l.Livre(livre["titre"], livre["auteur"], livre["annee"], livre["genre"]))
            for langue in livre["langues"]:
                livres[-1].ajouterLangue(langue)

    # Crée la fenêtre principale de l'application
    ft = tk.Tk()
    ft.title("Bibliothèque")
    ft.geometry("400x400")
    
    # Met à jour l'interface utilisateur avec la liste des livres
    ftLivres, livresobj = updateLivres(ft, livres)

    # Crée un cadre pour les boutons d'ajout et de sauvegarde
    addFenetre = tk.Frame(ft)
    btnAdd = tk.Button(addFenetre, text="Ajouter un livre", command=addLivre)
    btnAdd.grid(row=0, column=0)
    btnSave = tk.Button(addFenetre, text="Sauvegarder", command=lambda: saufgarder(livres))
    btnSave.grid(row=0, column=1)
    addFenetre.grid(row=1, column=0)

    # Démarre la boucle d'événements pour la fenêtre principale
    ft.mainloop()

if __name__ == "__main__":
    main()  # Appelle la fonction principale pour démarrer l'application
