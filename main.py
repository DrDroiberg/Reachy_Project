import time
from reachy_sdk import ReachySDK
import numpy as np
from arm_recognition import arm_recognition
from angle_calculation import angle_right_elbow, angle_right_arm_yam, angle_right_shoulder_pitch
from coordinate_transposition import coordinate_transposition
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

    with open(path_txt + 'right_arm_yam_angle.txt', 'a') as f:
        f.write(str(angle_right_arm_yam(i)) + '\n')

    with open(path_txt + 'right_shoulder_pitch_angle.txt', 'a') as f:
        f.write(str(angle_right_shoulder_pitch(i)) + '\n')

print("Angle calculation is done")
time.sleep(2)

print("Start the z coordinate calculation")
# Get z of the wrist
get_z()
print("Z coordinate calculation is done")

right_wrist = np.loadtxt(path_txt + 'right_wrist_coords.txt', delimiter=',')
right_wrist_z = np.loadtxt(path_txt + 'wrist_z.txt', delimiter=',')

print("Start the coordinate transposition")
# Transform the coordinates to be used by the robot
coordinate_transposition()
print("Coordinate transposition is done")

right_wrist_cm = np.loadtxt(path_txt + 'right_wrist_coords_cm.txt', delimiter=',')

print("Coeff px to cm: ", coeff_px_to_cm)
#
# print(right_wrist_z * coeff_px_to_cm)
print("Right wrist")
print(right_wrist_cm * coeff_px_to_cm)

print("Start the inverse kinematic")
# Inverse Kinematic
inverse_kinematic(gamma, beta, alpha, right_wrist_z, right_wrist_cm)
print("Inverse kinematic is done")


reachy.turn_off_smoothly('r_arm')