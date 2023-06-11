import numpy as np
from picture_calculation import offset_3Ddistance

right_shoulder = 12
left_shoulder = 11

right_wrist = 16
left_wrist = 15

right_elbow = 14
left_elbow = 13

path_txt = 'C:/Users/vince/PycharmProjects/Reachy_Project/data_list/'
path_txt_save = 'C:/Users/vince/PycharmProjects/Reachy_Project/listes/'


lenght_arm = 0.5625

# data_rl = np.loadtxt(path_txt + 'data_rworld_img_0.txt', delimiter=',')

distance_right_wrist_shoulder_center = []

def coeff(data_rl):


    lenght_rl_arm = offset_3Ddistance(data_rl[0][right_shoulder], data_rl[0][right_elbow], data_rl[1][right_shoulder],
                                      data_rl[1][right_elbow], data_rl[2][right_shoulder], data_rl[2][right_elbow]) \
                    + offset_3Ddistance(data_rl[0][right_elbow], data_rl[0][right_wrist], data_rl[1][right_elbow],
                                        data_rl[1][right_wrist], data_rl[2][right_elbow], data_rl[2][right_wrist])

    # print("lenght_rl_arm : ", lenght_rl_arm)

    return lenght_arm / lenght_rl_arm

def coordinate_transpo_r_wrist(data):

    data_rl = np.loadtxt(path_txt + 'data_rlworld_img_0.txt', delimiter=',')
    coeff_transfo = coeff(data_rl)

    # Transform the coordinates to be used by the robot
    # Center of shoulders in cm
    x = data[0][right_shoulder] + (data[0][left_shoulder] - data[0][right_shoulder]) / 2
    y = min(data[1][right_shoulder], data[1][left_shoulder]) + (
                abs(data[1][right_shoulder] - data[1][left_shoulder]) / 2)
    z = data[2][right_shoulder]

    # print("x : ", x, " y : ", y, " z : ", z)

    distance_right_wrist_shoulder_center_x = (data[0][right_wrist] - x) * coeff_transfo
    distance_right_wrist_shoulder_center_y = (data[1][right_wrist] - y) * coeff_transfo
    distance_right_wrist_shoulder_center_z = (data[2][right_wrist] - z) * coeff_transfo

    distance_right_wrist_shoulder_center.append([distance_right_wrist_shoulder_center_x,
                                                 distance_right_wrist_shoulder_center_y,
                                                 distance_right_wrist_shoulder_center_z])

    # print("distance_right_wrist_shoulder_center : ", distance_right_wrist_shoulder_center)

    np.savetxt(path_txt_save + 'data_rworld.txt', distance_right_wrist_shoulder_center, delimiter=',')

    return distance_right_wrist_shoulder_center


data_rl = np.loadtxt(path_txt + 'data_rlworld_img_0.txt', delimiter=',')

# coeff(data_rl)
# print("coeff : ", coeff(data_rl))

# coordinate_transpo_r_wrist(data_rl)
# distance_right_wrist_shoulder_center :  [[-0.2485, 0.483, -0.05]]
# distance_right_wrist_shoulder_center :  [[-0.2725790942726991, 0.5298016198539786, -0.05484488818364167]]