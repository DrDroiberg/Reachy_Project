import numpy as np
from picture_calculation import offset_distance

# Get the coordinates of the right wrist and right elbow
right_wrist_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_wrist_coords.txt', delimiter=',')
right_elbow_coords = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_elbow_coords.txt', delimiter=',')

# lenght of the arm of reachy = 250 mm


pixel_L = offset_distance(right_elbow_coords[0][0], right_elbow_coords[0][1], right_wrist_coords[0][0], right_wrist_coords[0][1])
cm_L = 25 / pixel_L
def coeff_px_to_cm():
    return cm_L/100

