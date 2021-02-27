#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
## écrire une fonction distance qui,

étant données deux images (sous forme de listes), donne la distance entre les deux.

On peut par exemple prendre la somme (pour tous les pixels) de l'écart entre les deux codes dégradés de gris.
"""
pass

import sys

from distance import *

def plusProcheVoisin(image2test:list,imagesref:list)->list:
    """
    Fonction qui renvoie le plus proche voisin d'une liste à tester

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

    nbRefs = len(imagesref) # nombre d'images de référence
    ppv = imagesref[0] # on initialise avec la premiere image 
    # On teste toutes les images si on en trouve une plus proche on change ppv
    for i in range(nbRefs):
        if distance(image2test[1:],imagesref[i][1:])<distance(image2test[1:],ppv[1:]):
            ppv = imagesref[i]
    
    # Postconditions
    # assert isinstance(ecart,int),"l'écart n'est pas un entier"
    # if (ecart<0):
    #     raise ValueError("l'écart n'est pas positif")
    # Postconditions

    return ppv

def affichage3ou7(image:list)->str:
    """
    Fonction qui renvoie une chaine de caractère selon le plus proche voisin

    **Paramètres** 
    
    - image le plus proche voisin d'une image à tester    

    **Préconditions** ...

    **Invariant** ...

    **Postconsitions** ...

    **Sorties** Une chaine de caractère indiquant ce qu'est l'image, un 3 ou un 7
    """
    pass

    # Préconditions
    # assert isinstance(code1,int),"le premier paramètre n'est pas un entier"
    # assert isinstance(code2,int),"le second paramètre n'est pas un entier"
    # if (code1 not in range(256) or code2 not in range(256)):
    #     raise ValueError("L'un des deux paramètres au moins n'est pas un code de dégradés de gris")
    # Préconditions
    
    is3ou7 = 'Cette image est un '+image[0]

    # Postconditions
    # assert isinstance(ecart,int),"l'écart n'est pas un entier"
    # if (ecart<0):
    #     raise ValueError("l'écart n'est pas positif")
    # Postconditions

    return is3ou7    

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
    
