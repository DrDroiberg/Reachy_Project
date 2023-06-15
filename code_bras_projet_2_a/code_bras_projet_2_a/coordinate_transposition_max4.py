#commenter
import numpy as np
import os


path_txt = 'C:/Users/maxbu/dossPython/liste_Reachy/liste/'
aficher = 0


# Load the coordinates of the right wrist
right_wrist_coords = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_wrist_coords.txt', delimiter=',')
right_shoulder = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/right_shoulder_coords.txt', delimiter=',')
left_shoulder = np.loadtxt('C:/Users/maxbu/dossPython/liste_Reachy/liste/left_shoulder_coords.txt', delimiter=',')

# 0,0 coordinates
# For x
centre_x = left_shoulder[0][0] + (right_shoulder[0][0] - left_shoulder[0][0]) / 2
# For y
centre_y = min(right_shoulder[0][1], left_shoulder[0][1]) + (abs(right_shoulder[0][1] - left_shoulder[0][1]) / 2)
if aficher == 1:
    print(centre_x)
    print(centre_y)

right_wrist_coords_centered = []
left_wrist_coords_centered = []
def coordinate_transposition_right_xy(member, name, compteur_image):
# Transform the coordinates to be used by the robot
    for i in range(0, compteur_image):
        member[i][0] = member[i][0] - centre_x
        member[i][1] = member[i][1] - centre_y

        right_wrist_coords_centered.append([member[i][0], member[i][1]])
    if aficher == 1:
        print((type(member)))

    np.savetxt(path_txt + name + '.txt', right_wrist_coords_centered, delimiter=',', fmt='%1.3f')

def coordinate_transposition_left_xy(member, name, compteur_image):
# Transform the coordinates to be used by the robot
    for i in range(0, compteur_image):
        member[i][0] = member[i][0] - centre_x
        member[i][1] = member[i][1] - centre_y

        left_wrist_coords_centered.append([member[i][0], member[i][1]])
    if aficher == 1:
        print((type(member)))

    np.savetxt(path_txt + name + '.txt', left_wrist_coords_centered, delimiter=',', fmt='%1.3f')



# TODO centrer toutes les coordonées par rapport au centre du torse
# TODO remplacer les 'a' par des 'w' dans les fichiers txt