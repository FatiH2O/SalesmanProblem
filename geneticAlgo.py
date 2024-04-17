from utile import *  # Importe les fonctions utiles, peut-être des fonctions d'utilité pour le problème spécifique que tu traites
import random  # Importe la fonction randint pour générer des nombres aléatoires

class AlgorithmeGenetique:
    
    def __init__(self, taillePopulation):
        
        self.population =[]  # Liste des individus dans la population
        self.taillePopulation = taillePopulation  # Taille de la population
        
        
        self.fitness = {}
        self.distanceCourante = float('inf')  # Initialisation de la distance courante avec une valeur infinie
    
        self.tauxDePanne = 0.1  # Taux de mutation initialisé à 0.1 (10%)
    #algo de selectio par roulette
    def calculerFitness(self, coordonnee):
    # Calcule la fitness de chaque individu dans la population
        fitnessCumu = 0
        for individu in self.population:
                
            distance = sommeDistances(individu,coordonnee)  # Calcule la somme des distances pour cet individu
            fitness = 1 / (distance + 1)  # Calcule la fitness pour cet individu
            self.fitness[tuple(individu)]= fitness # Ajoute la fitness au dictionnaire des fitness pour chaque individu
            print("fitness de",individu,"est :", fitness)

        for individu, fit in self.fitness.items():
            fitnessCumu+= fit
        print("fitnesscumu = ",fitnessCumu) 
        return fitnessCumu

             
             
    
    def tombe_en_panne(self,villeA,villeB):
    
        for i in range(len(self.population[0])):
            if(randint(0, 100) / 100 < self.tauxDePanne):  # Vérifie si la mutation se produit
              return  Distance(villeA, villeB) + randint(1,50)


    #prend le nombre de ville entrée dans l'interface et une taile de population
    def initialize_population(self,nbVille): 
    
        for i in range(self.taillePopulation):#initialise la population avec des individu aléatoire,un individu un parcours représenté par une liste de ville
            individual = list(range(nbVille))#creer un individu
            random.shuffle(individual)#mélange la liste aléatoirement pour avoir des individu différents
            self.population.append(individual)#ajoute l'individu à la population
    
        


    def selectionNaturelle(self):
        # Effectue la sélection naturelle pour créer une nouvelle population
        nouvellePopulation = []
        for i in range(self.taillePopulation):
            parent1 = selectionnerParent(self.population, self.fitness)  # Sélectionne le premier parent
            parent2 = selectionnerParent(self.population, self.fitness)  # Sélectionne le deuxième parent
        
            self.muter(genes)  # Mutation des gènes
            nouvellePopulation.append(genes)  # Ajoute les gènes à la nouvelle population
        self.population = nouvellePopulation  # Met à jour la population avec la nouvelle population
