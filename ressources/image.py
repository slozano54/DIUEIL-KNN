#!/usr/bin/env python


import sys

image = input("Donnez le nom du fichier source : ")
img = int(input("Quel numero d image vous interesse ? "))
cible = input("Donnez le nom du fichier cible (avec extension .pgm) : ")

f = open(image, "r")
g = open(cible, "w")
img = int(img)

l = f.readlines()
line = l[img]

g.write("""P2
28 28
255
""")


for i in line.split(" ")[1:]:
        g.write("{} ".format(int(i)))
	
g.close()	
