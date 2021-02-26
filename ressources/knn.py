#!/usr/bin/env python

# utilisation : knn training testing 4
#le dernier argument est le numero de l image de test qu on veut  etudier
import sys

train = open("training","r")
test = open("testing","r")
num = int(input("Quelle image voulez-vous tester ?"))

l = train.readlines()
listetraining = [ligne.split() for ligne in l] 

for image in listetraining:
    for numpixel in range(len(image)):
        image[numpixel] = int(image[numpixel])
        
l2 = test.readlines()
listetesting = [ligne.split() for ligne in l2] 

for image in listetesting:
    for numpixel in range(1,len(image)): # on enlève le '?' en début d'image
        image[numpixel] = int(image[numpixel])
        

# cree une liste de listes. Chaque element de listetraining est une liste contenant le chiffre represente sur l'image, puis codage de cette image (28 pixels sur 28

print(listetraining) # juste pour tester, on a bien une liste de listes d'entiers


