#commenter
import numpy as np
from picture_calculation_max4 import offset_distance

#fonction qui determine la conversion en cm
def coeff_px_to_cm():
#importe le bras droit
    right_wrist_coords = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_wrist_coords.txt', delimiter=',')
    right_elbow_coords = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_elbow_coords.txt', delimiter=',')

#a partir de la premiere image du bras droit, determine un coefficient de convertion
    pixel_L = offset_distance(right_elbow_coords[0][0], right_elbow_coords[0][1], right_wrist_coords[0][0],             right_wrist_coords[0][1])
    cm_L = 25 / pixel_L

#cette limite minimale est peut etre a modifier mais lors de nos test, elle permetait d'obtenir de meilleur resultat
    if cm_L < 0.255 :
        cm_L = 0.255
    return cm_L/100

    #return 0.26

