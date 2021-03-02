#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
## Distance

écrire une fonction distance qui, étant données deux images (sous forme de listes), donne la distance entre les deux.

On peut par exemple prendre la somme (pour tous les pixels) de l'écart entre les deux codes dégradés de gris.
"""
pass

import sys

def ecart(code1:int,code2:int)->int:
    """
    Fonction qui retourne l'écart entre deux codes dégradés de gris.

    **Paramètres** code1 et code2 deux entiers 

    **Préconditions** code1 et code2 sont des codes de dégradés de gris compris entre 0 et 255    

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

    - image2test et imageref sont des listes
    - image2test et imageref ont le même nombre de pixels
    - image2test et imageref ont des pixels dont le code est compris entre 0 et 255


    **Postconsitions** la fonction retourne un nombre positif

    **Sorties** la distance qui vaut la somme des écarts positifs des pixels pris deux à deux
    """
    pass

    # Préconditions
    assert isinstance(image2test,list),"le premier paramètre n'est pas une liste"
    assert isinstance(imageref,list),"le second paramètre n'est pas une liste"
    # on ne compte pas le premier élément qui n'est pas la valeur d'un pixel !
    assert len(image2test[1:])==len(imageref[1:]),"les deux images n'ont pas le même nombre de pixels"
    for i in range(1,len(image2test)):    
        if (int(image2test[i]) not in range(256) or int(imageref[i]) not in range(256)):
            raise ValueError("L'un des deux paramètres au moins n'est pas un code de dégradés de gris")            
    # Préconditions

    distance = 0 #initialisation de la distance
    n = len(imageref) #la taille de l'image de référence pour la gestion de la boucle principale    
    for i in range(n):
        # ecart admet uniquement des entiers en parametre et les images sont des tableaux de string
        distance = distance + ecart(int(image2test[i]),int(imageref[i]))
    
    # Postconditions
    assert isinstance(distance,int),"la distance n'est pas un entier"
    if (distance<0):
        raise ValueError("la distance n'est pas positive")
    # Postconditions

    return distance

if __name__=="__main__":
    #Test de ecart()
    assert(ecart(245,15)==230)
    try:
        ecart('a',12)
        raise TypeError
    except: None
    try:
        ecart(257,12)
        raise ValueError
    except: None
    #Tests de distance()
    img_ref = ['3', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '38', '43', '105', '255', '253', '253', '253', '253', '253', '174', '6', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '43', '139', '224', '226', '252', '253', '252', '252', '252', '252', '252', '252', '158', '14', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '178', '252', '252', '252', '252', '253', '252', '252', '252', '252', '252', '252', '252', '59', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '109', '252', '252', '230', '132', '133', '132', '132', '189', '252', '252', '252', '252', '59', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4', '29', '29', '24', '0', '0', '0', '0', '14', '226', '252', '252', '172', '7', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '85', '243', '252', '252', '144', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '88', '189', '252', '252', '252', '14', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '91', '212', '247', '252', '252', '252', '204', '9', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '32', '125', '193', '193', '193', '253', '252', '252', '252', '238', '102', '28', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '45', '222', '252', '252', '252', '252', '253', '252', '252', '252', '177', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '45', '223', '253', '253', '253', '253', '255', '253', '253', '253', '253', '74', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '31', '123', '52', '44', '44', '44', '44', '143', '252', '252', '74', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '15', '252', '252', '74', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '86', '252', '252', '74', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '5', '75', '9', '0', '0', '0', '0', '0', '0', '98', '242', '252', '252', '74', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '61', '183', '252', '29', '0', '0', '0', '0', '18', '92', '239', '252', '252', '243', '65', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '208', '252', '252', '147', '134', '134', '134', '134', '203', '253', '252', '252', '188', '83', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '208', '252', '252', '252', '252', '252', '252', '252', '252', '253', '230', '153', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '49', '157', '252', '252', '252', '252', '252', '217', '207', '146', '45', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '7', '103', '235', '252', '172', '103', '24', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    img_2_test = ['?', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '84', '185', '159', '151', '60', '36', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '222', '254', '254', '254', '254', '241', '198', '198', '198', '198', '198', '198', '198', '198', '170', '52', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '67', '114', '72', '114', '163', '227', '254', '225', '254', '254', '254', '250', '229', '254', '254', '140', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '17', '66', '14', '67', '67', '67', '59', '21', '236', '254', '106', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '83', '253', '209', '18', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '22', '233', '255', '83', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '129', '254', '238', '44', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '59', '249', '254', '62', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '133', '254', '187', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '9', '205', '248', '58', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '126', '254', '182', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '75', '251', '240', '57', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '19', '221', '254', '166', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '3', '203', '254', '219', '35', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '38', '254', '254', '77', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '31', '224', '254', '115', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '133', '254', '254', '52', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '61', '242', '254', '254', '52', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '121', '254', '254', '219', '40', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '121', '254', '207', '18', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    #34017
    assert(distance(img_2_test[1:],img_ref[1:])==34017)

    img_ref = ['3', '257', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '38', '43', '105', '255', '253', '253', '253', '253', '253', '174', '6', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '43', '139', '224', '226', '252', '253', '252', '252', '252', '252', '252', '252', '158', '14', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '178', '252', '252', '252', '252', '253', '252', '252', '252', '252', '252', '252', '252', '59', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '109', '252', '252', '230', '132', '133', '132', '132', '189', '252', '252', '252', '252', '59', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4', '29', '29', '24', '0', '0', '0', '0', '14', '226', '252', '252', '172', '7', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '85', '243', '252', '252', '144', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '88', '189', '252', '252', '252', '14', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '91', '212', '247', '252', '252', '252', '204', '9', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '32', '125', '193', '193', '193', '253', '252', '252', '252', '238', '102', '28', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '45', '222', '252', '252', '252', '252', '253', '252', '252', '252', '177', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '45', '223', '253', '253', '253', '253', '255', '253', '253', '253', '253', '74', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '31', '123', '52', '44', '44', '44', '44', '143', '252', '252', '74', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '15', '252', '252', '74', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '86', '252', '252', '74', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '5', '75', '9', '0', '0', '0', '0', '0', '0', '98', '242', '252', '252', '74', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '61', '183', '252', '29', '0', '0', '0', '0', '18', '92', '239', '252', '252', '243', '65', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '208', '252', '252', '147', '134', '134', '134', '134', '203', '253', '252', '252', '188', '83', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '208', '252', '252', '252', '252', '252', '252', '252', '252', '253', '230', '153', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '49', '157', '252', '252', '252', '252', '252', '217', '207', '146', '45', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '7', '103', '235', '252', '172', '103', '24', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    img_2_test = ['?', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '84', '185', '159', '151', '60', '36', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '222', '254', '254', '254', '254', '241', '198', '198', '198', '198', '198', '198', '198', '198', '170', '52', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '67', '114', '72', '114', '163', '227', '254', '225', '254', '254', '254', '250', '229', '254', '254', '140', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '17', '66', '14', '67', '67', '67', '59', '21', '236', '254', '106', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '83', '253', '209', '18', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '22', '233', '255', '83', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '129', '254', '238', '44', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '59', '249', '254', '62', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '133', '254', '187', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '9', '205', '248', '58', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '126', '254', '182', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '75', '251', '240', '57', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '19', '221', '254', '166', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '3', '203', '254', '219', '35', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '38', '254', '254', '77', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '31', '224', '254', '115', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '133', '254', '254', '52', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '61', '242', '254', '254', '52', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '121', '254', '254', '219', '40', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '121', '254', '207', '18', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    try:
        distance(img_2_test[1:],img_ref[1:])
        raise ValueError
    except: None