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

    **Sorties** le plus proche voisin parmi les images de référence et son rang
    """
    pass

    # Préconditions
    # assert isinstance(code1,int),"le premier paramètre n'est pas un entier"
    # assert isinstance(code2,int),"le second paramètre n'est pas un entier"
    # if (code1 not in range(256) or code2 not in range(256)):
    #     raise ValueError("L'un des deux paramètres au moins n'est pas un code de dégradés de gris")
    # Préconditions

    nbRefs = len(imagesref) # nombre d'images de référence
    ppv = [imagesref[0],0] # on initialise avec la premiere image 
    # On teste toutes les images si on en trouve une plus proche on change ppv
    for i in range(nbRefs):
        if distance(image2test[1:],imagesref[i][1:])<distance(image2test[1:],ppv[0][1:]):
            ppv = [imagesref[i],i]
    
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
    test = open("ressources/testing","r")    

    l = train.readlines()
    listetraining = [ligne.split() for ligne in l] 
          
    l2 = test.readlines()
    listetesting = [ligne.split() for ligne in l2]      

    for j in range(len(listetesting)):
        #print(plusProcheVoisin(listetesting[j],listetraining))
        print("Selon le plus proche voisin, l'image "+str(j+1)+affichage3ou7(plusProcheVoisin(listetesting[j],listetraining)))
        print("Selon les 5 plus proches voisins, l'image "+str(j+1)+plusDe3ou7(cinqPlusProcheVoisin(listetesting[j],listetraining)))
    
