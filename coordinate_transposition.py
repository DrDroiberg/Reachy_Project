import numpy as np

# Load the coordinates of the right wrist
right_wrist_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_wrist_coords.txt', delimiter=',')
right_shoulder = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_shoulder_coords.txt', delimiter=',')
left_shoulder = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/left_shoulder_coords.txt', delimiter=',')

# 0,0 coordinates
# For x
centre_x = left_shoulder[0][0] + (right_shoulder[0][0] - left_shoulder[0][0]) / 2
# For y
centre_y = min(right_shoulder[0][1], left_shoulder[0][1]) + (abs(right_shoulder[0][1] - left_shoulder[0][1]) / 2)
def coordinate_transposition():
# Transform the coordinates to be used by the robot
    for i in range(0, 10):
        right_wrist_coords[i][0] = right_wrist_coords[i][0] - centre_x
        right_wrist_coords[i][1] = right_wrist_coords[i][1] - centre_y