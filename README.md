**Le jeu de la vie :**  
Qu'est ce que le jeu de la vie ?  

Le Jeu de la vie est un « jeu à zéro joueur », puisqu'il ne nécessite aucune intervention du joueur lors de son déroulement. 
Il s'agit d'un automate cellulaire imaginé par John Horton Conway en 1970, un modèle où chaque état conduit mécaniquement à l'état suivant à partir de règles pré-établies.  

REGLES DU JEU:  

Principe de naissance:  
Si une case est vide et que trois de ses voisines sont occupées, alors une naissance s’y
produit.

Principe de stase:
Si une case est occupée, la survie n’y est possible que si deux ou trois cases voisines sont
occupées.

Principe de mort:
Si une case est entourée de 0 ou 1 voisine occupée, la case est vide à la génération suivante
(mort par isolement).
Si une case est entourée de 3 voisines occupées et plus, la case est vide à la génération
suivante (mort par surpopulation)

Problèmes que je peux rencontrer :
- Je peux faire la grille facilement, mais je peux avoir du mal à programmer les règles du jeu
- je peux avoir du mal à programmer un compteur du nombre de la population.


MVP: Règles du jeu + grille + boutons Go! et Stop

Cahier journal:
7/04/22 : création de la grille + bouton Go! + Stop + Erase
14/04/2022 : nombreux problèmes d'indentations résolus + mise en place du cahier journal :)
16/04/2022 : création de la fonction "vitesse de l'animation en ms".
19/04/2022 : mise en place des règles (aide d'une vidéo)
24/04/2022 : fonction "taille des cellules" pour changer la forme du tableau et des cellules.

