#commenter
from reachy_sdk import ReachySDK
import math as m
import numpy as np
import os

from picture_calculation_max4 import findAngle
from picture_calculation_max4 import findRotation
from picture_calculation_max4 import findTheta

compteur_image = 100

path = 'C:/Users/maxbu/dossPython/liste_Reachy/recognised_images'
#reachy = ReachySDK(host='10.117.255.255')
angle_elbow = []

########################################################################################################################
# Extract the values from the coordinates_file.txt and put them in a 2D list
left_shoulder_coords = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/left_shoulder_coords.txt',
                                  delimiter=',')
right_shoulder_coords = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_shoulder_coords.txt',
                                   delimiter=',')
left_elbow_coords = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/left_elbow_coords.txt',
                               delimiter=',')
right_elbow_coords = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_elbow_coords.txt',
                                delimiter=',')
left_wrist_coords = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/left_wrist_coords.txt',
                               delimiter=',')
right_wrist_coords = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_wrist_coords.txt',
                                delimiter=',')
left_hip_coords = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/left_hip_coords.txt', delimiter=',')

right_hip_coords = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_hip_coords.txt',
                              delimiter=',')


########################################################################################################################

def angle_left_shoulder(i):
    angle_shoulder = findAngle(left_shoulder_coords[i][0], left_shoulder_coords[i][1], left_elbow_coords[i][0],
                               left_elbow_coords[i][1], left_hip_coords[i][0], left_hip_coords[i][1])
    return angle_shoulder


def angle_right_shoulder(i):
    angle_shoulder = findAngle(right_shoulder_coords[i][0], right_shoulder_coords[i][1], right_elbow_coords[i][0],
                               right_elbow_coords[i][1], right_hip_coords[i][0], right_hip_coords[i][1])
    return angle_shoulder


def angle_left_elbow(i):
    angle_elbow = findAngle(left_elbow_coords[i][0], left_elbow_coords[i][1], left_shoulder_coords[i][0],
                            left_shoulder_coords[i][1], left_wrist_coords[i][0], left_wrist_coords[i][1])
    return angle_elbow


def angle_right_elbow(i):
    angle_elbow = findAngle(right_elbow_coords[i][0], right_elbow_coords[i][1], right_shoulder_coords[i][0],
                            right_shoulder_coords[i][1], right_wrist_coords[i][0], right_wrist_coords[i][1])
    return angle_elbow


def angle_right_arm_yam(i):
    angle_yamn = findTheta(right_elbow_coords[i][0], right_elbow_coords[i][1], right_wrist_coords[i][0], right_wrist_coords[i][1])
    return angle_yamn


#def angle_right_shoulder_pitch(i):
#    angle_pitch = findTheta(right_shoulder_coords[i][0], right_shoulder_coords[i][1], right_elbow_coords[i][0], #right_elbow_coords[i][1])
  #  return angle_pitch


for i in range(0, compteur_image):
    angle = angle_left_shoulder(i)

    # save the left shoulder angle in a file
    with open('C:/Users/maxbu/dossPython/liste_Reachy/liste/left_shoulder_angle.txt', 'a') as f:
        f.write(str(angle) + '\n')

for i in range(0, compteur_image):
    angle = angle_right_shoulder(i)

    # save the right shoulder angle in a file
    with open('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_shoulder_angle.txt', 'a') as f:
        f.write(str(angle) + '\n')

for i in range(0, compteur_image):
    angle = angle_left_elbow(i)

    # save the left elbow angle in a file
    with open('C:/Users/maxbu/dossPython/liste_Reachy/liste/left_elbow_angle.txt', 'a') as f:
        f.write(str(angle) + '\n')

for i in range(0, compteur_image):
    angle = angle_right_elbow(i)

    # save the right elbow angle in a file
    with open('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_elbow_angle.txt', 'a') as f:
        f.write(str(angle) + '\n')

for i in range(0, compteur_image):
    # angle = angle_right_arm_yam(i)

    # save the right arm yam angle in a file
    with open('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_arm_yam_angle.txt', 'a') as f:
        f.write(str(angle) + '\n')

#for i in range(0, compteur_image):
#    angle = angle_right_shoulder_pitch(i)

    # save the right arm pitch angle in a file
    with open('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_pitch_shoulder_angle.txt', 'a') as f:
        f.write(str(angle) + '\n')