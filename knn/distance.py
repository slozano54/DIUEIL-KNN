#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
## écrire une fonction distance qui,

étant données deux images (sous forme de listes), donne la distance entre les deux.

On peut par exemple prendre la somme (pour tous les pixels) de l'écart entre les deux codes dégradés de gris.
"""
pass

import sys

def ecart(code1:int,code2:int)->int:
    """
    Fonction qui retourne l'écart entre deux codes dégradés de gris.

    **Paramètres** code1 et code2 deux entiers 

    **Préconditions** code1 et code2 sont des codes de dégradés de gris compris entre 0 et 255

    **Invariant** Il n'y a pas de boucle !

    **Postconsitions** la fonction retourne un nombre positif

    **Sorties** l'écart positif entre les codes de dégradés de gris    
    """
    pass

    # Préconditions
    assert isinstance(code1,int),"le premier paramètre n'est pas un entier"
    assert isinstance(code2,int),"le second paramètre n'est pas un entier"
    if (code1 not in range(256) or code2 not in range(256)):
        raise ValueError("L'un des deux paramètres au moins n'est pas un code de dégradés de gris")
    # Préconditions

    ecart = abs(code1 - code2)

    # Postconditions
    assert isinstance(ecart,int),"l'écart n'est pas un entier"
    if (ecart<0):
        raise ValueError("l'écart n'est pas positif")
    # Postconditions

    return ecart

def distance(image2test:list,imageref:list)->int:
    """
    Fonction qui retourne la somme des écarts (positifs) entre les pixels, pris deux à deux, de deux images en dégradés de gris.

    **Paramètres** image2test et imageref deux listes d'entiers

    **Préconditions** 

    - image2test et imageref ont le même nombre de pixels
    - image2test et imageref ont des pixels dont le code est compris entre 0 et 255

    **Invariant** ...

    **Postconsitions** la fonction retourne un nombre positif

    **Sorties** la distance qui vaut la somme des écarts positifs des pixels pris deux à deux
    """
    pass

    # Préconditions
    # assert isinstance(code1,int),"le premier paramètre n'est pas un entier"
    # assert isinstance(code2,int),"le second paramètre n'est pas un entier"
    # if (code1 not in range(256) or code2 not in range(256)):
    #     raise ValueError("L'un des deux paramètres au moins n'est pas un code de dégradés de gris")
    # Préconditions

    distance = 0 #initialisation de la distance
    n = len(imageref) #la taille de l'image de référence pour la gestion de la boucle principale    
    for i in range(n):
        # ecart admet uniquement des entiers en parametre
        distance = distance + ecart(int(image2test[i]),int(imageref[i]))
    
    # Postconditions
    # assert isinstance(ecart,int),"l'écart n'est pas un entier"
    # if (ecart<0):
    #     raise ValueError("l'écart n'est pas positif")
    # Postconditions

    return distance

if __name__=="__main__":
    #Test des ecarts    
    assert(ecart(245,15)==230)
    try:
        ecart('a',12)
        raise TypeError
    except: None
    try:
        ecart(257,12)
        raise ValueError
    except: None

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

    for j in range(len(listetraining)):
        print(distance(listetesting[0][1:],listetraining[j][1:]))
    
