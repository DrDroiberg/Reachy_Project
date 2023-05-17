from reachy_sdk import ReachySDK
import math as m
import numpy as np
import os

right_elbow_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_elbow_coords.txt')

reachy = ReachySDK(host='localhost')

# Get the third coordinate of the right elbow
right_elbow_z = right_elbow_coords[2]