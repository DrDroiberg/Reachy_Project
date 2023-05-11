from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory import InterpolationMode
import time
import cv2 as cv
import mediapipe as mp
import math as m
import os

path = 'C:/Users/vince/PycharmProjects/Reachy_Project/recognised_images'
coordinates_file = open('C:/Users/vince/PycharmProjects/Reachy_Project/coordinates.txt')
reachy = ReachySDK(host='localhost')
angle_elbow = []


def offset_distance(x1, y1, x2, y2):
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return dist


def findAngle(x1, y1, x2, y2, x3, y3):
    # Caculate the angle between the left shoulder and the left elbow using the cosine rule
    a = offset_distance(x2, y2, x3, y3)
    b = offset_distance(x1, y1, x3, y3)
    c = offset_distance(x1, y1, x2, y2)

    theta = m.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
    degree = theta * int(180 / m.pi)
    return degree


def angle_calculation():
    # Open coordinates_file as a list
    coordinates = coordinates_file.readlines()

    for i in range(len(coordinates)-1):
        coordinates[i] = coordinates[i].strip('\n')
        # print(coordinates[i])
        img_to_treat = coordinates[i]
        # print(img_to_treat)
        # Caculate the angle between the left shoulder and the left elbow
        degree_elbow = findAngle(int(coordinates[i][0][0]), int(coordinates[i][0][1]), int(coordinates[i][2][4]),
                           int(coordinates[i][2][5]), int(coordinates[i][7][14]), int(coordinates[i][7][15]))

        print("Shoulder degree: " + degree_elbow)

#TODO : find a way to calculate the angle between the left shoulder and the left elbow, it return an invalid literal for int() with base 10: '['