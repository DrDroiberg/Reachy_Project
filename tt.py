import numpy as np

from coordinate_transposition import coordinate_transposition_r_arm

data = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/data_list/data_rlworld_img_13.txt', delimiter=',')

right_wrist_coords = coordinate_transposition_r_arm(data)

x_r_wrist = right_wrist_coords[0]

print(x_r_wrist)