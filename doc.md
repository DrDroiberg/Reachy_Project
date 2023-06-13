# Documentation for the project
## main
### pose_recognition(duration)
duration: nombre d'images de la séquence de capture
La fonction permet d'effectuer la reconnaissance des différentes articulations de la personne. Les coordonnées des points sont stockées dans un fichier texte.

### coordinate_transpo_r_wrist(data)
data: numpy list, liste des points trouvés par Mediapipe sur les photos
La fonction est utilisée pour transposer les coordonées pour qu'elles soient utilisées par le bras droit du robot

### coordinate_transpo_l_wrist(data)
data: numpy list, liste des points trouvés par Mediapipe sur les photos
La fonction est utilisée pour transposer les coordonées pour qu'elles soient utilisées par le bras gauche du robot

### inverse_kinematic_v2_r_arm(gamma, beta, alpha, x, y, z, old_movement)
gamma, beta, alpha : variables pour la rotation du poignet autour des axes x, y et z
x, y et z: coordonées à atteindre par le robot, en cm
old_movement: angles de la position N-1 qui servent de référence pour trouver les coordonées de la prochaine position

### inverse_kinematic_v2_l_arm(gamma, beta, alpha, x, y, z, old_movement)
gamma, beta, alpha : variables pour la rotation du poignet autour des axes x, y et z
x, y et z: coordonées à atteindre par le robot, en cm
old_movement: angles de la position N-1 qui servent de référence pour trouver les coordonées de la prochaine position
La fonction permet de calculer la cinématique inverse ainsi que de faire le déplacement du bras à la bonne position

## inverse_kinematic
### Full_matrice_Rota(gama,beta,alpha,x,y,z)
gamma, beta, alpha : variables pour la rotation du poignet autour des axes x, y et z
x, y et z: coordonées à atteindre par le robot, en cm
La fonction permet de calculer la matrice de rotation qui va être utilisée pour la cinématique inverse
