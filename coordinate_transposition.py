import numpy as np
import os

path_txt = 'C:/Users/vince/PycharmProjects/Reachy_Project/listes/'

# Load the coordinates of the right wrist
right_wrist_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_wrist_coords.txt', delimiter=',')
right_shoulder = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_shoulder_coords.txt', delimiter=',')
left_shoulder = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/left_shoulder_coords.txt', delimiter=',')

# 0,0 coordinates
# For x
centre_x = left_shoulder[0][0] + (right_shoulder[0][0] - left_shoulder[0][0]) / 2
# For y
centre_y = min(right_shoulder[0][1], left_shoulder[0][1]) + (abs(right_shoulder[0][1] - left_shoulder[0][1]) / 2)

print(centre_x)
print(centre_y)

right_wrist_coords_centered = []
def coordinate_transposition_xy(member, name):
# Transform the coordinates to be used by the robot
    for i in range(0, 10):
        member[i][0] = member[i][0] - centre_x
        member[i][1] = member[i][1] - centre_y

        right_wrist_coords_centered.append([member[i][0], member[i][1]])

    print((type(member)))

    np.savetxt(path_txt + name + '.txt', right_wrist_coords_centered, delimiter=',', fmt='%1.3f')



# TODO centrer toutes les coordonées par rapport au centre du torse
# TODO remplacer les 'a' par des 'w' dans les fichiers txt