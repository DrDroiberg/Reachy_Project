import time
from reachy_sdk import ReachySDK
import numpy as np
from arm_recognition import arm_recognition
from angle_calculation import angle_right_elbow, angle_right_shoulder_pitch
from coordinate_transposition import coordinate_transposition_xy
from z_coordinate import get_z
from inverse_kinematic import inverse_kinematic
from conversion_px_cm import coeff_px_to_cm

reachy = ReachySDK(host='localhost')

path_txt = 'C:/Users/vince/PycharmProjects/Reachy_Project/listes/'

gamma = 0
beta = 0
alpha = 0
coeff_px_to_cm = coeff_px_to_cm()

reachy.turn_on('r_arm')

print("Start the camera")
# camera_capture()
print("Camera is done")
time.sleep(2)
print("Start the arm recognition")
arm_recognition()
print("Arm recognition is done")
time.sleep(2)
print("Start the angle calculation")
for i in range(0, 10):

    with open(path_txt + 'right_elbow_angle.txt', 'a') as f:
        f.write(str(angle_right_elbow(i)) + '\n')

    # with open(path_txt + 'right_arm_yam_angle.txt', 'a') as f:
    #     f.write(str(angle_right_arm_yam(i)) + '\n')

    with open(path_txt + 'right_shoulder_pitch_angle.txt', 'a') as f:
        f.write(str(angle_right_shoulder_pitch(i)) + '\n')

print("Angle calculation is done")
time.sleep(2)

# print("Start the z coordinate calculation")
# # Get z of the wrist
# get_z()
# print("Z coordinate calculation is done")

right_wrist_not_centered = np.loadtxt(path_txt + 'right_wrist_coords.txt', delimiter=',')
shoulder_coords_not_centered = np.loadtxt(path_txt + 'right_shoulder_coords.txt', delimiter=',')
elbow_coords_not_centered = np.loadtxt(path_txt + 'right_elbow_coords.txt', delimiter=',')


print("Start the coordinate transposition")
# Transform the coordinates to be used by the robot
coordinate_transposition_xy(right_wrist_not_centered, 'wrist_coords_centered')
coordinate_transposition_xy(shoulder_coords_not_centered,'shoulder_not_centered')
coordinate_transposition_xy(elbow_coords_not_centered, 'elbow_coords_not_centered')
print("Coordinate transposition is done")

wrist_coords = np.loadtxt(path_txt + 'wrist_coords_centered.txt', delimiter=',')
shoulder_coords = np.loadtxt(path_txt + 'shoulder_not_centered.txt', delimiter=',')
elbow_coords = np.loadtxt(path_txt + 'elbow_coords_not_centered.txt', delimiter=',')

print("Coeff px to cm: ", coeff_px_to_cm)

# print(right_wrist_z * coeff_px_to_cm)
print("Right wrist")
print('Wrist: ', wrist_coords * coeff_px_to_cm, '\nShoulder: ', shoulder_coords * coeff_px_to_cm, '\nElbow: ', elbow_coords * coeff_px_to_cm)

print("Start the inverse kinematic")
# Inverse Kinematic
inverse_kinematic(gamma, beta, alpha, shoulder_coords, elbow_coords, wrist_coords)
print("Inverse kinematic is done")


reachy.turn_off_smoothly('r_arm')