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
left_shoulder_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/left_shoulder_coords.txt', delimiter=',')
right_shoulder_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/right_shoulder_coords.txt', delimiter=',')
left_elbow_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/left_elbow_coords.txt', delimiter=',')
right_elbow_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/right_elbow_coords.txt', delimiter=',')
left_wrist_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/left_wrist_coords.txt', delimiter=',')
right_wrist_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/right_wrist_coords.txt', delimiter=',')
left_hip_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/left_hip_coords.txt', delimiter=',')
right_hip_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/right_hip_coords.txt', delimiter=',')

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


def angle_shoulder():
    #TODO : find a way to make the angle_shoulder function work with the coordinates_x.txt

    return angle_shoulder





angle_shoulder()

