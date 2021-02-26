<!-- 
    Source pour l'écriture d'un REAMDE en mardown : https://www.makeareadme.com/ 
-->
# DIU EIL 2020/2022 
## BLOC2 - Projet KNN 
Récupérer sur la page du cours les fichiers suivants :
* training contient 200 images, avec pour chacune le chire représenté (3 ou 7) et le codage en
dégradé de gris de chaque pixel
* testing contient toutes les images que l'on veut tester
* knn.py contient un début de programme, qui réalise l'ouverture des chiers
* image.py permet de convertir une image en format pgm

### écrire une fonction
distance
qui, étant données deux images (sous forme de listes), donne la
distance entre les deux. On peut par exemple prendre la somme (pour tous les pixels) de l'écart
entre les deux codes dégradés de gris,
### compléter le programme pour qu'il associe à une image de test la valeur (3 ou 7) du plus proche
voisin ; le programme doit au nal acher cette image est un 7) ou cette image est un 3
### adaptez votre programme pour qu'il associe maintenant à une image de test la valeur majoritaire
parmi les 5 plus proches voisins. Attention à ne pas eacer le travail de la question précédente,
soit en créant une nouvelle fonction (une pour le plus proche, une pour les 5 plus proches), soit en
faisant les modications dans un nouveau chier.

## Auteur
Sébastien LOZANO

## Installation - Utilisation
Pour générer la documentation il faut installer le paquet python [pdoc3](https://pdoc3.github.io/pdoc/)

```bash
pip3 install pdoc
```
Cloner [le dépot](https://github.com/slozano54/DIUEIL-KNN) ou télécharger l'[archive zip](https://github.com/slozano54/DIUEIL-KNN/archive/master.zip).

À la racine du projet, lancer le script python **...**

```bash
python3 ....py
```

## Notes
Les fichiers de la documentation sont générés dans le dossier **./...**

Les résultats des tests sont générés dans le dossier **./rapports_de_tests**

## License
[MIT](https://choosealicense.com/licenses/mit/)