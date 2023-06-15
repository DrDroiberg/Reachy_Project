# Reachy_Project
Le but de ce projet est que le robot Reachy puisse imiter les mouvements de bras d'un être humain.
## Fonctionnement
Pour ce faire, on capture des images avec soit une caméra extérieure, soit les caméras intégrées dans la tête de Reachy.
Il faut ensuite déterminer les positions des poignets du robot pour qu'il puisse déplacer ses bras.

Pour cela, nous avons décidé d'implémenter deux méthodes de récupérations des coordonées:
- La première est de récupérer les coordonées x, y et z grâce à la library *Mediapipe*.
- La seconde est de récupérer la longueur des bras pour déterminer la profondeur z. On a déjà x et y sur l'image.

Ensuite on utilise la cinématique inverse grâce aux coordonées pour pouvoir déterminer les angles que les moteurs doivent prendre pour atteindre la dite position.
## Progression
### Déjà réalisé:
- Capture d'images par le robot ou une caméra externe.
- Récupération de la pose de la personne:
  - Grâce à *Mediapipe*.
  - Calcul de la longueur des bras sur l'image.
- Contrôle du robot avec des coordonnées calculées à partir des images.
- Avec la méthode de calcul de longueurs des bras:
  - Maintient du coude à une certaine position pour éviter qu'il n'aille à des positions bizarres.
### Problèmes restants
Sur la simulation et le robot: 
- Il y a des problèmes sur le positionnement des coudes qui ne sont pas à la bonne place avec la première méthode.
- Un léger décalage dans le positionnement des poignets du à une imprécision de mesure.

Sur le robot réel:
- Le robot ne veut pas aller jusqu'au bout des mouvements et s'arrête avant.

## Installation
- Télécharger le package unity de reachy en suivant le tutoriel ici: [Create your own virtual scene for Reachy](https://pollen-robotics.github.io/reachy-2019-docs/docs/simulation/create-your-own-scene/).
- Se connecter au robot: `localhost` ou l'IP de votre robot. *Ne pas oublier d'être sur le même réseau que ce dernier*.

## Exécution
- Pour utiliser la première méthode, exécuter le `main.py` de cette branche
- Pour utiliser la seconde méthode, exécuter le `main.py` de la branche `version_longueur_bras`
 
## Annexes
Les documentations sont disponibles ici:
- Première méthode: [Documentation](https://github.com/DrDroiberg/Reachy_Project/blob/master/doc.md)
- Seconde méthode: [Documentation](https://github.com/DrDroiberg/Reachy_Project/blob/master/Documentation_Code_version_longueurs_de_bras.pdf)
