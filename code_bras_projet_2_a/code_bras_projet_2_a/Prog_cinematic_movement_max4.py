#commenter
from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory import InterpolationMode
from scipy.spatial.transform import Rotation as R
import numpy as np
from math import cos,sin,radians

#reachy = ReachySDK(host='10.117.255.255')


# reachy.turn_on('r_arm')


#Définition de la matrice de rotation avec les position x,y,z
#gama = rotation sur l'axe x
#beta = rotation sur l'axe y
#alpha = rotation sur l'axe z
#xyz, position de la main dans l'espace avec comme référence le centre du robot
def Full_matrice_Rota(gama,beta,alpha,x,y,z):
    full_matrix = np.array([[cos(alpha) * cos(beta), (cos(alpha) * sin(beta) * sin(gama)) - (sin(alpha) * cos(gama)), (cos(alpha) * sin(beta) * cos(gama)) + (sin(alpha) * sin(gama)),x],[sin(alpha) * cos(beta), (sin(alpha) * sin(beta) * sin(gama)) + (cos(alpha) * cos(gama)), (sin(alpha) * sin(beta) * cos(gama)) - (cos(alpha) * sin(gama)),y],[ -sin(beta), cos(beta) * sin(gama), cos(beta) * cos(gama) ,z],[0,0,0,1]])
    return full_matrix


##############Voici comment implémenter un mouvement
#
#   Bras droit
#
#   mouvement = Full_matrice_Rota(0,-90,-90,0.2,-1,0.5)  #ces valleurs sont un exemple de mouvement
#   final_position = reachy.r_arm.inverse_kinematics(mouvement)
#   time.sleep(0.5)
#   goto({joint: pos for joint,pos in zip(reachy.r_arm.joints.values(), final_position)}, duration=1.0)
#
#
#   Bras gauche
#
#   mouvement2 = Full_matrice_Rota(0,-90,-90,0.2,-1,0.5)  #ces valleurs sont un exemple de mouvement
#   final_position2 = reachy.l_arm.inverse_kinematics(mouvement2)
#   time.sleep(0.5)
#   goto({joint: pos for joint,pos in zip(reachy.l_arm.joints.values(), final_position2)}, duration=1.0)
#
##########Ici, il faut chaner uniquement 'final_position' ou 'r_arm' en 'l_arm'


# reachy.turn_off_smoothly('r_arm')


