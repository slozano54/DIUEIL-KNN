#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
## Programme principal

Détermine le type de chaque image à tester selon :

* le plus proche voisin contenu dans un fichier de 200 images de références

* les 5 plus proches voisins contenus dans un fichier de 200 images de références
    
"""
pass

# Pour mesurer le temps de traitement du script
from datetime import datetime 
# Pour copier les variable
import copy 

# Module knn
from knn.distance import *
from knn.plusProchesVoisins import *

# Script principal
def main():    
    # On récupère la date au début du traitement
    start_time = datetime.now()

    # On ouvre le fichier avec les images de références    
    train = open("ressources/training","r")
    #On récupère chaque ligne du fichier sous forme d'un tableau de string
    l = train.readlines()
    listetraining = [ligne.split() for ligne in l] 

    # On ouvre le fichier avec les images à tester
    test = open("ressources/testing","r")    
    #On récupère chaque ligne du fichier sous forme d'un tableau de string
    l2 = test.readlines()
    listetesting = [ligne.split() for ligne in l2]

    # Affichages de sorties
    print("=============================================================================")    
    print("Type de chaque image selon son plus proche voisin")    
    print("-------------------------------------------------")    
    print("")
    for j in range(len(listetesting)):
        print("Selon son plus proche voisin, l'image "+str(j+1)+affichage3ou7(plusProcheVoisin(listetesting[j],listetraining)))
    print("=============================================================================")

    print(".............................................................................")    

    print("=============================================================================")    
    print("Type de chaque image selon ses 5 plus proches voisins")
    print("-----------------------------------------------------")    
    print("")
    for j in range(len(listetesting)):
        print("Selon ses 5 plus proches voisins, l'image "+str(j+1)+plusDe3ou7(cinqPlusProchesVoisins(listetesting[j],listetraining)))
    print("=============================================================================")    

    print(".............................................................................")    

    # On évalue le temps de traitement
    end_time = datetime.now()
    print("=============================================================================")
    print("  Durée totale de traitement : ",end_time-start_time)        
    print("=============================================================================")
 
if __name__ == "__main__":
    main()    