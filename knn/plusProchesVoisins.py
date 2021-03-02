#!/usr/bin/python3
#-*- coding: utf8 -*-
"""
## compléter le programme 

pour qu'il associe à une image de test la valeur (3 ou 7) du plus proche
voisin ; le programme doit au final afficher 'cette image est un 7' ou 'cette image est un 3'

## adaptez votre programme 
 
pour qu'il associe maintenant à une image de test la valeur majoritaire
parmi les 5 plus proches voisins. Attention à ne pas effacer le travail de la question précédente,
soit en créant une nouvelle fonction (une pour le plus proche, une pour les 5 plus proches), soit en
faisant les modifications dans un nouveau fichier.
"""
pass

import sys
import copy

if __name__=="__main__":
    from distance import *
else:
    from knn.distance import *

def isDistanceMin(image2test:list,imageMin:list,imagesref:list)->bool:
    """
    Fonction booléenne qui renvoie True si la distance entre image2test et imageMin
    est inférieure ou égale à toutes les distances entre image2test et les éléments de imagesref

    **Paramètres**

    - image2test est une liste d'entiers dont le premier élément est un ?
    - imageMin est une liste dont il faut tester si la distance à image2test est minimale
    - imagesref est l'échantillon d'images de référence

    **Préconditions**

    - image2test, imageMin et les éléments de imagesref sont les listes
    - image2test et les éléments de imagesref ont le même nombre de pixels
    - image2test et imagesref ont des pixels dont le code est compris entre 0 et 255 à partir du second élément

    **Postconditions**

    - la sortie est un booléen

    """
    pass
    #Préconditions
    assert isinstance(image2test,list),"l'image à tester n'est pas sous forme de liste"    
    assert isinstance(imageMin,list),"l'image candidate n'est pas sous forme de liste"
    assert len(image2test[1:])==len(imageMin[1:]),"image2test et imageMin n'ont pas le même nombre de pixels"
    for i in range(len(imagesref)):
        assert isinstance(imagesref[i],list),"l'image "+str(i+1)+" de l'échantillon de référence n'est pas sous forme de liste"
        assert len(image2test[1:])==len(imagesref[i][1:]),"image2test l'image "+str(i+1)+" de l'échantillon de référence n'ont pas le même nombre de pixels"
    for i in range(1,len(image2test)):    
        if (int(image2test[i]) not in range(256) or int(imageMin[i]) not in range(256)):
            raise ValueError("L'un des deux premiers paramètres au moins n'est pas un code de dégradés de gris")            
    for j in range(len(imagesref)):
        for i in range(1,len(imagesref[j])):
            if(int(imagesref[j][i]) not in range(256)):
                raise ValueError("L'un des codes des images de l'échantillon de référence n'est pas un code de dégradé de gris.")
    #Préconditions

    # a priori c'est la plus petite distance
    isTrue = True
    i = 0
    while (i<len(imagesref) and isTrue):
        if distance(image2test[1:],imageMin[1:])>distance(image2test[1:],imagesref[i][1:]):
            isTrue = False
        i = i+1

    #Postconditions
    assert isinstance(isTrue,bool),"isTrue n'est pas un booléen"
    #Postconditions

    return isTrue



def plusProcheVoisin(image2test:list,imagesref:list)->list:
    """
    Fonction qui renvoie le plus proche voisin d'une liste à tester parmi un échantillon de référence

    **Paramètres** 
    
    - image2test est une liste d'entiers dont le premier élément est un ?
    - imagesref est une liste de listes dont le premier élément  vaut 3 ou 7 

    **Préconditions** 

    - image2test et les éléments de imagesref sont les listes
    - image2test et les éléments de imagesref ont le même nombre de pixels
    - image2test et imagesref ont des pixels dont le code est compris entre 0 et 255 à partir du second élément

    **Postconsitions** 
    
    - La sortie est un tableau de deux éléments
    - le premier est une liste dont tous les éléments sont des codes entre 0 et 255
    - le second un entier compris entre 0 et la taille de imagesref    
    - La distance avec image2test est minimale

    **Sorties** le plus proche voisin parmi les images de référence et son indice dans imageref
    """
    pass

    # Préconditions
    assert isinstance(image2test,list),"l'image à tester n'est pas sous forme de liste"    
    for i in range(len(imagesref)):
        assert isinstance(imagesref[i],list),"l'image "+str(i+1)+" de l'échantillon de référence n'est pas sous forme de liste"
        assert len(image2test[1:])==len(imagesref[i][1:]),"image2test l'image "+str(i+1)+" de l'échantillon de référence n'ont pas le même nombre de pixels"
    for i in range(1,len(image2test)):    
        if (int(image2test[i]) not in range(256)):
            raise ValueError("L'un des éléments de imge2test au moins n'est pas un code de dégradés de gris")            
    for j in range(len(imagesref)):
        for i in range(1,len(imagesref[j])):
            if(int(imagesref[j][i]) not in range(256)):
                raise ValueError("L'un des codes des images de l'échantillon de référence n'est pas un code de dégradé de gris.")
    # Préconditions

    nbRefs = len(imagesref) # nombre d'images de référence
    ppv = [imagesref[0],0] # on initialise avec la premiere image 
    # On teste toutes les images si on en trouve une plus proche on change ppv
    for i in range(nbRefs):
        if distance(image2test[1:],imagesref[i][1:])<distance(image2test[1:],ppv[0][1:]):
            ppv = [imagesref[i],i]
    
    # Postconditions
    assert len(ppv)==2,"la sortie n'a pas deux éléments"
    assert isinstance(ppv[0],list),"le premier élément de la sortie n'est pas une liste"
    for i in range(1,len(ppv[0])):
        assert (int(ppv[0][i]) in range(256)),"l'un des éléments de la liste de sortie n'est pas un code de gris"
    assert isinstance(ppv[1],int),"le second élément de la sortie n'est pas un entier"
    assert ppv[1] in range(len(imagesref))
    assert isDistanceMin(image2test,ppv[0],imagesref)
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
    
    is3ou7 = ' est un '+image[0][0]

    # Postconditions
    # assert isinstance(ecart,int),"l'écart n'est pas un entier"
    # if (ecart<0):
    #     raise ValueError("l'écart n'est pas positif")
    # Postconditions

    return is3ou7    

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
    maxDe3ou7 = ' est un '
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
    # test = open("ressources/testing","r")    

    l = train.readlines()
    listetraining = [ligne.split() for ligne in l] 
          
    # l2 = test.readlines()
    # listetesting = [ligne.split() for ligne in l2]      

    # for j in range(len(listetesting)):
    #     #print(plusProcheVoisin(listetesting[j],listetraining))
    #     print("Selon le plus proche voisin, l'image "+str(j+1)+affichage3ou7(plusProcheVoisin(listetesting[j],listetraining)))
    #     print("Selon les 5 plus proches voisins, l'image "+str(j+1)+plusDe3ou7(cinqPlusProcheVoisin(listetesting[j],listetraining)))
    img2test = ['3', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '38', '43', '105', '255', '253', '253', '253', '253', '253', '174', '6', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '43', '139', '224', '226', '252', '253', '252', '252', '252', '252', '252', '252', '158', '14', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '178', '252', '252', '252', '252', '253', '252', '252', '252', '252', '252', '252', '252', '59', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '109', '252', '252', '230', '132', '133', '132', '132', '189', '252', '252', '252', '252', '59', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4', '29', '29', '24', '0', '0', '0', '0', '14', '226', '252', '252', '172', '7', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '85', '243', '252', '252', '144', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '88', '189', '252', '252', '252', '14', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '91', '212', '247', '252', '252', '252', '204', '9', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '32', '125', '193', '193', '193', '253', '252', '252', '252', '238', '102', '28', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '45', '222', '252', '252', '252', '252', '253', '252', '252', '252', '177', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '45', '223', '253', '253', '253', '253', '255', '253', '253', '253', '253', '74', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '31', '123', '52', '44', '44', '44', '44', '143', '252', '252', '74', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '15', '252', '252', '74', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '86', '252', '252', '74', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '5', '75', '9', '0', '0', '0', '0', '0', '0', '98', '242', '252', '252', '74', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '61', '183', '252', '29', '0', '0', '0', '0', '18', '92', '239', '252', '252', '243', '65', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '208', '252', '252', '147', '134', '134', '134', '134', '203', '253', '252', '252', '188', '83', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '208', '252', '252', '252', '252', '252', '252', '252', '252', '253', '230', '153', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '49', '157', '252', '252', '252', '252', '252', '217', '207', '146', '45', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '7', '103', '235', '252', '172', '103', '24', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'] 
    imgMin = ['3', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '38', '43', '105', '255', '253', '253', '253', '253', '253', '174', '6', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '43', '139', '224', '226', '252', '253', '252', '252', '252', '252', '252', '252', '158', '14', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '178', '252', '252', '252', '252', '253', '252', '252', '252', '252', '252', '252', '252', '59', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '109', '252', '252', '230', '132', '133', '132', '132', '189', '252', '252', '252', '252', '59', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '4', '29', '29', '24', '0', '0', '0', '0', '14', '226', '252', '252', '172', '7', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '85', '243', '252', '252', '144', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '88', '189', '252', '252', '252', '14', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '91', '212', '247', '252', '252', '252', '204', '9', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '32', '125', '193', '193', '193', '253', '252', '252', '252', '238', '102', '28', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '45', '222', '252', '252', '252', '252', '253', '252', '252', '252', '177', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '45', '223', '253', '253', '253', '253', '255', '253', '253', '253', '253', '74', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '31', '123', '52', '44', '44', '44', '44', '143', '252', '252', '74', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '15', '252', '252', '74', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '86', '252', '252', '74', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '5', '75', '9', '0', '0', '0', '0', '0', '0', '98', '242', '252', '252', '74', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '61', '183', '252', '29', '0', '0', '0', '0', '18', '92', '239', '252', '252', '243', '65', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '208', '252', '252', '147', '134', '134', '134', '134', '203', '253', '252', '252', '188', '83', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '208', '252', '252', '252', '252', '252', '252', '252', '252', '253', '230', '153', '8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '49', '157', '252', '252', '252', '252', '252', '217', '207', '146', '45', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '7', '103', '235', '252', '172', '103', '24', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    #print(isDistanceMin(img2test,imgMin,listetraining))
    print(plusProcheVoisin(img2test,listetraining))
