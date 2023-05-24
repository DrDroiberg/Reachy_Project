from reachy_sdk import ReachySDK
from math import cos, sin
import numpy as np
from conversion_px_cm import coeff_px_to_cm
from picture_calculation import offset_distance

from picture_calculation import offset_distance
path_txt = 'C:/Users/vince/PycharmProjects/Reachy_Project/listes/'
coeff = coeff_px_to_cm()

def get_z():
    right_elbow_angle = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_elbow_angle.txt',
                                   delimiter=',')
    right_arm_yaw = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_arm_yam_angle.txt',
                               delimiter=',')

    right_elbow_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_elbow_coords.txt',
                                    delimiter=',')
    right_wrist_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_wrist_coords.txt',
                                    delimiter=',')

    right_pitch_shoulder = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_shoulder_pitch_angle.txt',
                                        delimiter=',')

    reachy = ReachySDK(host='localhost')
    for i in range(0, 10):

        L = offset_distance(right_elbow_coords[0][0], right_elbow_coords[0][1], right_wrist_coords[0][0],
                            right_wrist_coords[0][1])
        r = L * cos(right_elbow_angle[i] - 180 + right_pitch_shoulder[i])
        z = r * cos(right_arm_yaw[i])

        with open(path_txt + 'wrist_z.txt', 'a') as f:
            f.write(str(z) + '\n')


def get_depth(i, shoulder_coords, elbow_coords, wrist_coords):

    arm_lenght = offset_distance(shoulder_coords[i][0], shoulder_coords[i][1], elbow_coords[i][0], elbow_coords[i][1])
    forearm_lenght = offset_distance(elbow_coords[i][0], elbow_coords[i][1], wrist_coords[i][0], wrist_coords[i][1])

    depth = (0.25 - forearm_lenght * coeff) + (0.28 - arm_lenght * coeff)
    return depth