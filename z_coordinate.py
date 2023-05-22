from reachy_sdk import ReachySDK
from math import cos
import numpy as np
import os
import cv2 as cv

from picture_calculation import offset_distance
path_txt = 'C:/Users/vince/PycharmProjects/Reachy_Project/listes/'
def get_z():
    right_elbow_angle = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_elbow_angle.txt',
                                   delimiter=',')
    right_arm_yaw = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_arm_yam_angle.txt',
                               delimiter=',')

    right_elbow_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_elbow_coords.txt',
                                    delimiter=',')
    right_wrist_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_wrist_coords.txt',
                                    delimiter=',')

    reachy = ReachySDK(host='localhost')
    for i in range(0, 10):

        L = offset_distance(right_elbow_coords[i][0], right_elbow_coords[i][1], right_wrist_coords[i][0],
                            right_wrist_coords[i][1])
        r = L * cos(right_elbow_angle[i] - 90)
        z = r * cos(right_arm_yaw[i])

        with open(path_txt + 'wrist_z.txt', 'a') as f:
            f.write(str(z) + '\n')