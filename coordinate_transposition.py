import numpy as np
import os

path_txt = 'C:/Users/vince/PycharmProjects/Reachy_Project/listes/'

# Load the coordinates of the right wrist
# right_wrist_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_wrist_coords.txt', delimiter=',')
# right_shoulder = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_shoulder_coords.txt', delimiter=',')
# left_shoulder = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/left_shoulder_coords.txt', delimiter=',')

right_shoulder = 12
left_shoulder = 11

right_wrist = 16
left_wrist = 15

# 0,0 coordinates
# # For x
# centre_x = left_shoulder[0][0] + (right_shoulder[0][0] - left_shoulder[0][0]) / 2
# # For y
# centre_y = min(right_shoulder[0][1], left_shoulder[0][1]) + (abs(right_shoulder[0][1] - left_shoulder[0][1]) / 2)

# print(centre_x)
# print(centre_y)

distance_right_wrist_shoulder_center = []
distance_right_wrist_shoulder_center_x = []
distance_right_wrist_shoulder_center_y = []
distance_right_wrist_shoulder_center_z = []


def coordinate_transposition_xy(data):
    # Transform the coordinates to be used by the robot
    # distance_right_wrist_shoulder_center.append(['Y', 'Z', 'X'])
    # Center of shoulders in cm
    x = data[0][right_shoulder] + (data[0][left_shoulder] - data[0][right_shoulder]) / 2
    y = min(data[1][right_shoulder], data[1][left_shoulder]) + (
                abs(data[1][right_shoulder] - data[1][left_shoulder]) / 2)
    z = data[2][right_shoulder]

    # Distance between the right wrist and the center of the shoulders in cm
    distance_right_wrist_shoulder_center_x = x - data[0][right_wrist]

    distance_right_wrist_shoulder_center_y = y - data[1][right_wrist]

    distance_right_wrist_shoulder_center_z = z - data[2][right_wrist]

    distance_right_wrist_shoulder_center.append([distance_right_wrist_shoulder_center_x,
                                                 distance_right_wrist_shoulder_center_y,
                                                 distance_right_wrist_shoulder_center_z])

    np.savetxt(path_txt + 'distance_right_wrist_shoulder_center.txt',
               distance_right_wrist_shoulder_center, delimiter=',')

    return distance_right_wrist_shoulder_center
