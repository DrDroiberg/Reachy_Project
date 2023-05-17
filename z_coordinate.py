from reachy_sdk import ReachySDK
import math as m
import numpy as np
import os
import cv2 as cv

right_elbow_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_elbow_coords.txt')

reachy = ReachySDK(host='localhost')

# Get the third coordinate of the right elbow from the coordinates in the list

