#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
    
"""
pass

# On fait les imports nécessaires selon le contexte

# Pour mesurer le temps de traitement du script
from datetime import datetime 
# Pour copier les variable
import copy 

# Modules knn
from knn.distance import *
from knn.plusProchesVoisins import *

# Script principal
def main():    
    # On récupère la date au début du traitement
    start_time = datetime.now()    
    train = open("ressources/training","r")
    test = open("ressources/testing","r")    

    l = train.readlines()
    listetraining = [ligne.split() for ligne in l] 
          
    l2 = test.readlines()
    listetesting = [ligne.split() for ligne in l2]      

    print("=============================================================================")    
    print("Type de chaque image selon son plus proche voisin")    
    print("")
    for j in range(len(listetesting)):
        print("Selon le plus proche voisin, l'image "+str(j+1)+affichage3ou7(plusProcheVoisin(listetesting[j],listetraining)))
    print("=============================================================================")    
    print("=============================================================================")    
    print("Type de chaque image selon ses 5 plus proches voisins")    
    print("")
    for j in range(len(listetesting)):
        print("Selon les 5 plus proches voisins, l'image "+str(j+1)+plusDe3ou7(cinqPlusProcheVoisin(listetesting[j],listetraining)))
    print("=============================================================================")    

    # On évalue le temps de traitement
    end_time = datetime.now()
    print("=============================================================================")
    print("  Durée totale de traitement : ",end_time-start_time)        
    print("=============================================================================")
 
if __name__ == "__main__":
    main()    