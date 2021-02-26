#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
## écrire une fonction distance qui,

étant données deux images (sous forme de listes), donne la distance entre les deux.
On peut par exemple prendre la somme (pour tous les pixels) de l'écart entre les deux codes dégradés de gris,
"""
pass

def ecart(code1:int,code2:int)->int:
    """
    Fonction qui retourne l'écart entre deux codes dégradés de gris.

    **Paramètres** code1 et code2 deux entiers correspondants à des codes de dégradés de gris 
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

#def distance(image2test,imageref)

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
