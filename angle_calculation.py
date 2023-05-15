from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory import InterpolationMode
import time
import cv2 as cv
import mediapipe as mp
import math as m
import os
import numpy as np
from arm_recognition import arm_recognition

path = 'C:/Users/vince/PycharmProjects/Reachy_Project/recognised_images'
reachy = ReachySDK(host='localhost')
angle_elbow = []

########################################################################################################################
# Extract the values from the coordinates_file.txt and put them in a 2D list
left_shoulder_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/left_shoulder_coords.txt', delimiter=',')
right_shoulder_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_shoulder_coords.txt', delimiter=',')
left_elbow_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/left_elbow_coords.txt', delimiter=',')
right_elbow_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_elbow_coords.txt', delimiter=',')
left_wrist_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/left_wrist_coords.txt', delimiter=',')
right_wrist_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_wrist_coords.txt', delimiter=',')
left_hip_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/left_hip_coords.txt', delimiter=',')
right_hip_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_hip_coords.txt', delimiter=',')

########################################################################################################################


def offset_distance(x1, y1, x2, y2):
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return dist


def findAngle(x1, y1, x2, y2, x3, y3):
    # Caculate the angle between the left shoulder and the left elbow using the cosine rule
    a = offset_distance(x2, y2, x3, y3)
    b = offset_distance(x1, y1, x3, y3)
    c = offset_distance(x1, y1, x2, y2)

    theta = m.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
    degree = theta * int(180 / m.pi) # + 90
    return round(degree, 2)


def angle_left_shoulder(i):
    angle_shoulder = findAngle(left_shoulder_coords[i][0], left_shoulder_coords[i][1], left_elbow_coords[i][0], left_elbow_coords[i][1], left_hip_coords[i][0], left_hip_coords[i][1])
    return angle_shoulder

def angle_right_shoulder(i):
    angle_shoulder = findAngle(right_shoulder_coords[i][0], right_shoulder_coords[i][1], right_elbow_coords[i][0], right_elbow_coords[i][1], right_hip_coords[i][0], right_hip_coords[i][1])
    return angle_shoulder

def angle_left_elbow(i):
    angle_elbow = findAngle(left_elbow_coords[i][0], left_elbow_coords[i][1], left_shoulder_coords[i][0], left_shoulder_coords[i][1], left_wrist_coords[i][0], left_wrist_coords[i][1])
    return angle_elbow

def angle_right_elbow(i):
    angle_elbow = findAngle(right_elbow_coords[i][0], right_elbow_coords[i][1], right_shoulder_coords[i][0], right_shoulder_coords[i][1], right_wrist_coords[i][0], right_wrist_coords[i][1])
    return angle_elbow

for i in range(0, 10):
    angle = angle_left_shoulder(i)

    # save the left shoulder angle in a file
    with open('C:/Users/vince/PycharmProjects/Reachy_Project/listes/left_shoulder_angle.txt', 'a') as f:
        f.write(str(angle) + '\n')


for i in range(0, 10):
    angle = angle_right_shoulder(i)

    # save the right shoulder angle in a file
    with open('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_shoulder_angle.txt', 'a') as f:
        f.write(str(angle) + '\n')

for i in range(0, 10):
    angle = angle_left_elbow(i)

    # save the left elbow angle in a file
    with open('C:/Users/vince/PycharmProjects/Reachy_Project/listes/left_elbow_angle.txt', 'a') as f:
        f.write(str(angle) + '\n')

for i in range(0, 10):
    angle = angle_right_elbow(i)

    # save the right elbow angle in a file
    with open('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_elbow_angle.txt', 'a') as f:
        f.write(str(angle) + '\n')

