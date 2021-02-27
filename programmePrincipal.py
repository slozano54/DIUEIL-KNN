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
    print("=============================================================================")    
    print("...")    
    print("")
    print("=============================================================================")    

    # On évalue le temps de traitement
    end_time = datetime.now()
    print("=============================================================================")
    print("  Durée totale de traitement : ",end_time-start_time)        
    print("=============================================================================")
 
if __name__ == "__main__":
    main()    