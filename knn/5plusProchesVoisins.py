#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
## écrire une fonction distance qui,

étant données deux images (sous forme de listes), donne la distance entre les deux.

On peut par exemple prendre la somme (pour tous les pixels) de l'écart entre les deux codes dégradés de gris.
"""
pass

import sys
import copy

from distance import *
from plusProcheVoisin import *

def cinqPlusProcheVoisin(image2test:list,imagesref:list)->list:
    """
    Fonction qui renvoie les 5 plus proches voisins d'une liste à tester

    **Paramètres** 
    
    - image2test une liste d'entiers, premier élément : ?
    - imagesref une liste de liste, premier élément  : 3 ou 7 

    **Préconditions** 

    - image2test et et les éléments de imagesref ont le même nombre de pixels
    - image2test et imagesref ont des pixels dont le code est compris entre 0 et 255 à partir du second élément

    **Invariant** ...

    **Postconsitions** ...

    **Sorties** le plus proche voisin parmi les images de référence
    """
    pass

    # Préconditions
    # assert isinstance(code1,int),"le premier paramètre n'est pas un entier"
    # assert isinstance(code2,int),"le second paramètre n'est pas un entier"
    # if (code1 not in range(256) or code2 not in range(256)):
    #     raise ValueError("L'un des deux paramètres au moins n'est pas un code de dégradés de gris")
    # Préconditions
    
    references = copy.deepcopy(imagesref)    
    i=0
    five_ppv = []    
    while i<5:        
        five_ppv.append(plusProcheVoisin(image2test,references))
        references.pop(five_ppv[i][1])        
        i +=1
    
    # Postconditions
    # assert isinstance(ecart,int),"l'écart n'est pas un entier"
    # if (ecart<0):
    #     raise ValueError("l'écart n'est pas positif")
    # Postconditions

    return five_ppv

def plusDe3ou7(tab:list)->str:
    """
    Fonction qui renvoie une chaine selon la valeur majoritaire parmi 5 plus proches voisins d'une liste à tester

    **Paramètres** 
    
    **Préconditions** ...

    **Invariant** ...

    **Postconsitions** ...

    **Sorties** Une chaine de caracteres
    """
    pass

    # Préconditions
    # assert isinstance(code1,int),"le premier paramètre n'est pas un entier"
    # assert isinstance(code2,int),"le second paramètre n'est pas un entier"
    # if (code1 not in range(256) or code2 not in range(256)):
    #     raise ValueError("L'un des deux paramètres au moins n'est pas un code de dégradés de gris")
    # Préconditions
    
    nb_3 = 0
    nb_7 = 0
    maxDe3ou7 = 'Selon les 5 plus proches voisins, cette images est un '
    for i in range(len(tab)):        
        if tab[i][0][0]=='3':
            nb_3 +=1
        if tab[i][0][0]=='7':
            nb_7 +=1            
    if (nb_3>nb_7):
        maxDe3ou7 +='3'
    else:
        maxDe3ou7 +='7'
          
    # Postconditions
    # assert isinstance(ecart,int),"l'écart n'est pas un entier"
    # if (ecart<0):
    #     raise ValueError("l'écart n'est pas positif")
    # Postconditions

    return maxDe3ou7

if __name__=="__main__":
    ##################################
    # juste pour tester
    # à supprimer ensuite du module
    ##################################
    train = open("ressources/training","r")
    test = open("ressources/testing","r")    

    l = train.readlines()
    listetraining = [ligne.split() for ligne in l] 
          
    l2 = test.readlines()
    listetesting = [ligne.split() for ligne in l2]      

    for j in range(len(listetesting)):
        #print(plusProcheVoisin(listetesting[j],listetraining))
        print(affichage3ou7(plusProcheVoisin(listetesting[j],listetraining)))
        print(plusDe3ou7(cinqPlusProcheVoisin(listetesting[j],listetraining)))
    
