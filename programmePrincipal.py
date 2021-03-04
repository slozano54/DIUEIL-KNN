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
# Pour les commandes systeme
import os 

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
    os.system("clear")
    print("=============================================================================")    
    print("=========================== PROJET KNN BLOC2 ================================")    
    print("=============================================================================")    
    isOneShot = ''
    while isOneShot not in ['o','O','oui','Oui','OUI','n','N','non','Non','NON']:
        isOneShot = input("Voulez-vous tester toutes les images en une seule fois (o/n) ? ")
    
    print(".............................................................................")    

    if (isOneShot in ['o','O','oui','Oui','OUI']):
        print("=============================================================================")
        print("================================= TEST GLOBAL ===============================")    
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
    elif (isOneShot in ['n','N','non','Non','NON']):
        num = 0
        print("")    
        print("=============================================================================")
        print("================================ TEST PARTIEL ===============================")    
        print("=============================================================================")
        while num not in range(1,11):
            num = int(input("Il n'y a que 10 images, quelle image voulez-vous tester (entre 1 et 10) ? "))        

        print(".............................................................................")    

        print("Selon son plus proche voisin, l'image "+str(num)+affichage3ou7(plusProcheVoisin(listetesting[num-1],listetraining)))
        print("")
        print(".............................................................................")    
        print("Selon ses 5 plus proches voisins, l'image "+str(num)+plusDe3ou7(cinqPlusProchesVoisins(listetesting[num-1],listetraining)))    
        print("")
        print(".............................................................................")    

    # On évalue le temps de traitement
    end_time = datetime.now()
    print("=============================================================================")
    print("  Durée totale de traitement : ",end_time-start_time)        
    print("=============================================================================")
 
if __name__ == "__main__":
    main()    