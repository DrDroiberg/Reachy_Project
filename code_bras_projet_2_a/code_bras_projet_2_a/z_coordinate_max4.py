#commenter
from reachy_sdk import ReachySDK
from math import cos, sin
import numpy as np
from conversion_px_cm_max4 import coeff_px_to_cm
from picture_calculation_max4 import offset_distance

from picture_calculation_max4 import offset_distance
path_txt = 'C:/Users/maxbu/dossPython/liste_Reachy/liste/'
coeff = coeff_px_to_cm()


#fonction non utilisee qui devrait recuperer une information de profondeur
def get_z():

    right_arm_yaw = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_arm_yam_angle.txt',
                               delimiter=',')

    right_elbow_angle = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_elbow_angle.txt',
                                   delimiter=',')

    right_pitch_shoulder = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_shoulder_pitch_angle.txt',
                                        delimiter=',')


   # reachy = ReachySDK(host='10.117.255.255')
    for i in range(0, 10):

        L = offset_distance(right_elbow_coords[0][0], right_elbow_coords[0][1], right_wrist_coords[0][0],
                            right_wrist_coords[0][1])
        r = L * cos(right_elbow_angle[i] - 180 + right_pitch_shoulder[i])
        z = r * cos(right_arm_yaw[i])

        with open(path_txt + 'wrist_z.txt', 'a') as f:
            f.write(str(z) + '\n')


#fonction qui donne la donnee de profondeur par rapport au longueur des bras
def get_depth_r(i):

#charge ce qu'il faut
    right_elbow_coords = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_elbow_coords.txt',
                                    delimiter=',')
    right_wrist_coords = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_wrist_coords.txt',
                                    delimiter=',')
    right_shoulder_coords = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_shoulder_coords.txt', delimiter=',')

#determine la longueur des bras a partir de l'image de depart
    arm_lenght = offset_distance(right_shoulder_coords[i][0], right_shoulder_coords[i][1], right_elbow_coords[i][0], right_elbow_coords[i][1])
    forearm_lenght = offset_distance(right_elbow_coords[i][0], right_elbow_coords[i][1], right_wrist_coords[i][0], right_wrist_coords[i][1])

#calcule de la profondeur
    depth = ((0.17 - ((forearm_lenght * coeff)-0.1)) + (0.19 - ((arm_lenght * coeff)-0.1)))*1.5
    return depth


def get_depth_l(i):


    left_elbow_coords = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/left_elbow_coords.txt',
                                    delimiter=',')
    left_wrist_coords = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/left_wrist_coords.txt',
                                    delimiter=',')
    left_shoulder_coords = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/left_shoulder_coords.txt', delimiter=',')


    arm_lenght = offset_distance(left_shoulder_coords[i][0], left_shoulder_coords[i][1], left_elbow_coords[i][0], left_elbow_coords[i][1])
    forearm_lenght = offset_distance(left_elbow_coords[i][0], left_elbow_coords[i][1], left_wrist_coords[i][0], left_wrist_coords[i][1])
    depth = ((0.17 - ((forearm_lenght * coeff)-0.1)) + (0.19 - ((arm_lenght * coeff)-0.1)))*1.5
    return  depth



