from utile import *
from algo_genetic import *
import tkinter as tk
import random



def go():

    # Action à effectuer lorsque le bouton "Go" est cliqué
    number = entry.get() # Récupérer le chiffre entré dans l'entry
    # Insérer ici le traitement à effectuer avec le chiffre entré
    print("Chiffre entré:", number)
    draw_villes(int(number)) # Appel de la fonction pour dessiner les points
    update_label(int(number)) # Mettre à jour l'étiquette avec le nombre de points
    
    AlgoG= AlgorithmeGenetique(10)#creer une instance d'algo genetique avec la taille de population souhaitée
    for indiv,coo in coordonnee.items():
         print(indiv,":", coo)
    AlgoG.initialize_population(int(number))#initialiser la population
    
    for indiv in AlgoG.population:
         print("premièere pop" ,indiv)
    children=AlgoG.SelectionRoulette(coordonnee)

    AlgoG.elitist_replacement(children)
    
   
    
    


def reset():
    # Action à effectuer lorsque le bouton "Reset" est cliqué
    entry.delete(0, tk.END) # Effacer le contenu de l'entry
    canvas.delete("all") # Effacer tous les points dessinés sur le canevas
    update_label(0) # Remettre à zéro l'étiquette

coordonnee={}
def draw_villes(num_villes):
    # Dessiner des points sur le canevas pour représenter les villes
    for i in range(num_villes):
        x = random.randint(10, 390) # Position x aléatoire
        y = random.randint(10, 90) # Position y aléatoire
        coordonnee[i]=[x,y]
        canvas.create_oval(x-2, y-2, x+2, y+2, fill="red") # Dessiner un point

def update_label(num_points):
    # Mettre à jour l'étiquette avec le nombre de points
    label.config(text="Nombre de villes: {}".format(num_points))

# Création de la fenêtre principale
root = tk.Tk()
root.title("Interface graphique")

# Création de l'entry pour entrer un chiffre
entry = tk.Entry(root)
entry.pack()


        

# Création du bouton "Go"
go_button = tk.Button(root, text="Go", command=go)
go_button.pack()

# Création du bouton "Reset"
reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack()

# Création du canevas pour dessiner les points
canvas = tk.Canvas(root, width=400, height=100)
canvas.pack()

# Création de l'étiquette pour afficher le nombre de points
label = tk.Label(root, text="Nombre de points: 0")
label.pack()

# Lancement de la boucle principale
root.mainloop()

