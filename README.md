# Reachy_Project
Le but de ce projet est que le robot Reachy puisse imiter les mouvements de bras d'un être humain.
#
Pour ce faire, on capture des images avec soit une caméra extérieure, soit les caméras intégrées dans la tête de Reachy.
Il faut ensuite déterminer les positions des poignets du robot pour qu'il puisse déplacer ses bras.

Pour cela, nous avons décidé d'implémenter deux méthodes de récupérations des coordonées:
- La première est de récupérer les coordonées x, y et z grâce à la library Mediapipe
- La seconde est de récupérer la longueur des bras pour déterminer la profondeur z. On a déjà x et y sur l'image.

Ensuite on utilise la cinématique inverse grâce aux coordonées pour pouvoir déterminer les angles que les moteurs doivent prendre pour atteindre la dite position.
#
Sur la simulation et le robot:
- Actuellement, le robot n'imite pas parfaitement les mouvements humains. 
- Il y a des problèmes sur le positionnement des coudes qui ne sont pas à la bonne place.
- Le positionnement des poignets n'est pas totalement le même que la personne.

Sur le robot:
- Le robot ne veut pas aller jusqu'au bout des mouvements et s'arrête avant.
