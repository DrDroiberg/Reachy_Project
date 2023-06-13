import numpy as np
from picture_calculation import offset_3Ddistance
import os


right_shoulder = 12
left_shoulder = 11

right_wrist = 16
left_wrist = 15

right_elbow = 14
left_elbow = 13

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_txt = os.path.join(ROOT_DIR, "data_list")
path_txt_save = os.path.join(ROOT_DIR, "listes")

global x, y, z

lenght_arm = 0.5625

# data_rl = np.loadtxt(path_txt + 'data_rworld_img_0.txt', delimiter=',')

distance_right_wrist_shoulder_center = []
distance_left_wrist_shoulder_center = []

def coeff(data_rl, wrist):

    x = (data_rl[0][right_shoulder] + data_rl[0][left_shoulder]) / 2
    y = (data_rl[1][right_shoulder] + data_rl[1][left_shoulder]) / 2
    z = (data_rl[2][right_shoulder] + data_rl[2][left_shoulder]) / 2

    lenght_rl_arm = offset_3Ddistance(x, data_rl[0][wrist], y,
                                      data_rl[1][wrist], z, data_rl[2][wrist])
                    # + offset_3Ddistance(data_rl[0][right_elbow], data_rl[0][right_wrist], data_rl[1][right_elbow],
                    #                     data_rl[1][right_wrist], data_rl[2][right_elbow], data_rl[2][right_wrist])

    print("cooeff : ", lenght_rl_arm / lenght_arm)

    return lenght_rl_arm / lenght_arm

def coordinate_transpo_r_wrist(data):

    data_rl = np.loadtxt(path_txt + '/data_rlworld_img_0.txt', delimiter=',')
    coeff_transfo = coeff(data_rl, right_wrist)

    # Transform the coordinates to be used by the robot
    # Center of shoulders in cm
    x = (data[0][right_shoulder] + data[0][left_shoulder]) / 2
    y = (data[1][right_shoulder] + data[1][left_shoulder]) / 2
    z = (data[2][right_shoulder] + data[2][left_shoulder]) / 2

    # print("x : ", x, " y : ", y, " z : ", z)

    distance_right_wrist_shoulder_center_x = (data[0][right_wrist] - x) * coeff_transfo
    distance_right_wrist_shoulder_center_y = (data[1][right_wrist] - y) * coeff_transfo
    distance_right_wrist_shoulder_center_z = (data[2][right_wrist] - z) * coeff_transfo

    # print("distance_right_wrist_shoulder_center_x : ", distance_right_wrist_shoulder_center_x)
    # print("data[0][right_wrist] - x : ", data[0][right_wrist] - x)

    distance_right_wrist_shoulder_center.append([distance_right_wrist_shoulder_center_x,
                                                 distance_right_wrist_shoulder_center_y,
                                                 distance_right_wrist_shoulder_center_z])

    # print("distance_right_wrist_shoulder_center : ", distance_right_wrist_shoulder_center)

    np.savetxt(path_txt_save + '/data_rworld_right.txt', distance_right_wrist_shoulder_center, delimiter=',')

    return distance_right_wrist_shoulder_center

def coordinate_transpo_l_wrist(data):

    data_rl = np.loadtxt(path_txt + '/data_rlworld_img_0.txt', delimiter=',')
    coeff_transfo = coeff(data_rl, left_wrist)

    # Transform the coordinates to be used by the robot
    # Center of shoulders in cm
    x = data[0][right_shoulder] + (data[0][left_shoulder] - data[0][right_shoulder]) / 2
    y = min(data[1][right_shoulder], data[1][left_shoulder]) + (
                abs(data[1][right_shoulder] - data[1][left_shoulder]) / 2)
    z = data[2][right_shoulder]

    # print("x : ", x, " y : ", y, " z : ", z)

    distance_left_wrist_shoulder_center_x = (data[0][left_wrist] - x) * coeff_transfo
    distance_left_wrist_shoulder_center_y = (data[1][left_wrist] - y) * coeff_transfo
    distance_left_wrist_shoulder_center_z = (data[2][left_wrist] - z) * coeff_transfo

    distance_left_wrist_shoulder_center.append([distance_left_wrist_shoulder_center_x,
                                                 distance_left_wrist_shoulder_center_y,
                                                 distance_left_wrist_shoulder_center_z])

    # print("distance_right_wrist_shoulder_center : ", distance_right_wrist_shoulder_center)

    np.savetxt(path_txt_save + '/data_rworld_left.txt', distance_right_wrist_shoulder_center, delimiter=',')

    return distance_left_wrist_shoulder_center


# data_rl = np.loadtxt(path_txt + 'data_rlworld_img_0.txt', delimiter=',')
#
# coeff(data_rl)
# print("coeff : ", coeff(data_rl))
# # [-0.26458493434027247, 0.5142636751965859, -0.019697469960945825]
# # [-0.26458493434027247, 0.5142636751965859, -0.05323640529985362]]
# print("coordinate_transpo_r_wrist : ", coordinate_transpo_r_wrist(data_rl))
