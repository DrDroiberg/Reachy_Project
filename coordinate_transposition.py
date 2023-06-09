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

right_elbow = 14
left_elbow = 13

right_hip = 24
left_hip = 23

# 0,0 coordinates
# # For x
# centre_x = left_shoulder[0][0] + (right_shoulder[0][0] - left_shoulder[0][0]) / 2
# # For y
# centre_y = min(right_shoulder[0][1], left_shoulder[0][1]) + (abs(right_shoulder[0][1] - left_shoulder[0][1]) / 2)

# print(centre_x)
# print(centre_y)

distance_right_wrist_shoulder_center = []
distance_left_wrist_shoulder_center = []

distance_right_elbow_shoulder_center = []
distance_left_elbow_shoulder_center = []

distance_right_shoulder_shoulder_center = []
distance_left_shoulder_shoulder_center = []

distance_right_hip_shoulder_center = []
distance_left_hip_shoulder_center = []
def coordinate_transposition_r_arm(data):
    # Transform the coordinates to be used by the robot
    # Center of shoulders in cm
    x = data[0][right_shoulder] + (data[0][left_shoulder] - data[0][right_shoulder]) / 2
    y = min(data[1][right_shoulder], data[1][left_shoulder]) + (
                abs(data[1][right_shoulder] - data[1][left_shoulder]) / 2)
    z = data[2][right_shoulder]

    # print the soulder coordinates
    # print("right_shoulder : ", data[0][right_shoulder], " ", data[1][right_shoulder], " ", data[2][right_shoulder])
    # print("left_shoulder : ", data[0][left_shoulder], " ", data[1][left_shoulder], " ", data[2][left_shoulder])

    # x = (data[0][right_shoulder] + data[0][left_shoulder]) / 2
    # y = (data[1][right_shoulder] + data[1][left_shoulder]) / 2
    # z = (data[2][right_shoulder] + data[2][left_shoulder]) / 2

    # Distance between the right wrist and the center of the shoulders in cm
    distance_right_wrist_shoulder_center_x =data[0][right_wrist] - x
    distance_right_wrist_shoulder_center_y =data[1][right_wrist] - y
    distance_right_wrist_shoulder_center_z =data[2][right_wrist] - z

    distance_right_wrist_shoulder_center.append([distance_right_wrist_shoulder_center_x,
                                                 distance_right_wrist_shoulder_center_y,
                                                 distance_right_wrist_shoulder_center_z])

    np.savetxt(path_txt + 'distance_right_wrist_shoulder_center.txt', distance_right_wrist_shoulder_center, delimiter=',')

    return distance_right_wrist_shoulder_center


def coordinate_transposition_l_arm(data):

    x = data[0][right_shoulder] + (data[0][left_shoulder] - data[0][right_shoulder]) / 2
    y = min(data[1][right_shoulder], data[1][left_shoulder]) + (
                abs(data[1][right_shoulder] - data[1][left_shoulder]) / 2)
    z = data[2][right_shoulder]

    # Distance between the right wrist and the center of the shoulders in cm
    distance_left_wrist_shoulder_center_x =data[0][left_wrist] - x
    distance_left_wrist_shoulder_center_y =data[1][left_wrist] - y
    distance_left_wrist_shoulder_center_z =data[2][left_wrist] - z

    distance_left_wrist_shoulder_center.append([distance_left_wrist_shoulder_center_x,
                                                 distance_left_wrist_shoulder_center_y,
                                                 distance_left_wrist_shoulder_center_z])

    np.savetxt(path_txt + 'distance_left_wrist_shoulder_center.txt', distance_left_wrist_shoulder_center, delimiter=',')

    return distance_left_wrist_shoulder_center

def coordinate_transpo_elbow(data):

    x = data[0][right_shoulder] + (data[0][left_shoulder] - data[0][right_shoulder]) / 2
    y = min(data[1][right_shoulder], data[1][left_shoulder]) + (
                abs(data[1][right_shoulder] - data[1][left_shoulder]) / 2)
    z = data[2][right_shoulder]

    distance_right_elbow_shoulder_center_x =data[0][right_elbow] - x
    distance_right_elbow_shoulder_center_y =data[1][right_elbow] - y
    distance_right_elbow_shoulder_center_z =data[2][right_elbow] - z

    distance_right_elbow_shoulder_center.append([distance_right_elbow_shoulder_center_x,
                                                    distance_right_elbow_shoulder_center_y,
                                                    distance_right_elbow_shoulder_center_z])

    return distance_right_elbow_shoulder_center

def coordinate_transpo_l_elbow(data):

    x = data[0][right_shoulder] + (data[0][left_shoulder] - data[0][right_shoulder]) / 2
    y = min(data[1][right_shoulder], data[1][left_shoulder]) + (
                abs(data[1][right_shoulder] - data[1][left_shoulder]) / 2)
    z = data[2][right_shoulder]

    distance_left_elbow_shoulder_center_x =data[0][left_elbow] - x
    distance_left_elbow_shoulder_center_y =data[1][left_elbow] - y
    distance_left_elbow_shoulder_center_z =data[2][left_elbow] - z

    distance_left_elbow_shoulder_center.append([distance_left_elbow_shoulder_center_x,
                                                    distance_left_elbow_shoulder_center_y,
                                                    distance_left_elbow_shoulder_center_z])

    return distance_left_elbow_shoulder_center
def coordinate_transpo_r_shoulder(data):

    x = data[0][right_shoulder] + (data[0][left_shoulder] - data[0][right_shoulder]) / 2
    y = min(data[1][right_shoulder], data[1][left_shoulder]) + (
                abs(data[1][right_shoulder] - data[1][left_shoulder]) / 2)
    z = data[2][right_shoulder]

    distance_right_shoulder_shoulder_center_x = data[0][right_shoulder] - x
    distance_right_shoulder_shoulder_center_y =data[1][right_shoulder] - y
    distance_right_shoulder_shoulder_center_z =data[2][right_shoulder] - z

    distance_right_shoulder_shoulder_center.append([distance_right_shoulder_shoulder_center_x,
                                                    distance_right_shoulder_shoulder_center_y,
                                                    distance_right_shoulder_shoulder_center_z])

    return distance_right_shoulder_shoulder_center

def coordinate_transpo_l_shoulder(data):

    x = data[0][right_shoulder] + (data[0][left_shoulder] - data[0][right_shoulder]) / 2
    y = min(data[1][right_shoulder], data[1][left_shoulder]) + (
                abs(data[1][right_shoulder] - data[1][left_shoulder]) / 2)
    z = data[2][right_shoulder]

    distance_left_shoulder_shoulder_center_x =data[0][left_shoulder] - x
    distance_left_shoulder_shoulder_center_y =data[1][left_shoulder] - y
    distance_left_shoulder_shoulder_center_z =data[2][left_shoulder] - z

    distance_left_shoulder_shoulder_center.append([distance_left_shoulder_shoulder_center_x,
                                                    distance_left_shoulder_shoulder_center_y,
                                                    distance_left_shoulder_shoulder_center_z])


    return distance_left_shoulder_shoulder_center

def coordinate_transpo_r_hip(data):

    x = data[0][right_shoulder] + (data[0][left_shoulder] - data[0][right_shoulder]) / 2
    y = min(data[1][right_shoulder], data[1][left_shoulder]) + (
                abs(data[1][right_shoulder] - data[1][left_shoulder]) / 2)
    z = data[2][right_shoulder]

    distance_right_hip_shoulder_center_x = x - data[0][right_hip]
    distance_right_hip_shoulder_center_y = y - data[1][right_hip]
    distance_right_hip_shoulder_center_z = z - data[2][right_hip]

    distance_right_hip_shoulder_center.append([distance_right_hip_shoulder_center_x,
                                                    distance_right_hip_shoulder_center_y,
                                                    distance_right_hip_shoulder_center_z])

    return distance_right_hip_shoulder_center

def coordinate_transpo_l_hip(data):

    x = data[0][right_shoulder] + (data[0][left_shoulder] - data[0][right_shoulder]) / 2
    y = min(data[1][right_shoulder], data[1][left_shoulder]) + (
                abs(data[1][right_shoulder] - data[1][left_shoulder]) / 2)
    z = data[2][right_shoulder]

    distance_left_hip_shoulder_center_x = data[0][left_hip] - x
    distance_left_hip_shoulder_center_y = data[1][left_hip] - y
    distance_left_hip_shoulder_center_z = data[2][left_hip] - z

    distance_left_hip_shoulder_center.append([distance_left_hip_shoulder_center_x,
                                                    distance_left_hip_shoulder_center_y,
                                                    distance_left_hip_shoulder_center_z])

    return distance_left_hip_shoulder_center