**Le jeu de la vie :**  
Quel est le jeu de la vie ?  

Le Jeu de la vie est un « jeu à zéro joueur », puisqu'il ne nécessite aucune intervention du joueur lors de son déroulement. 
Il s'agit d'un automate cellulaire, un modèle où chaque état conduit mécaniquement à l'état suivant à partir de règles pré-établies.  

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
