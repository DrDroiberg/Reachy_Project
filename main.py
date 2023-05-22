import time
from reachy_sdk import ReachySDK
import numpy as np
from camera_control import camera_control
from arm_recognition import arm_recognition
from angle_calculation import angle_right_shoulder
from angle_calculation import angle_right_elbow
from angle_calculation import angle_right_arm_yam
from angle_calculation import angle_right_shoulder_pitch
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
    # with open(path_txt + 'right_shoulder_angle.txt', 'a') as f:
    #     f.write(str(angle_right_shoulder(i)) + '\n')

    with open(path_txt + 'right_elbow_angle.txt', 'a') as f:
        f.write(str(angle_right_elbow(i)) + '\n')

    with open(path_txt + 'right_arm_yam_angle.txt', 'a') as f:
        f.write(str(angle_right_arm_yam(i)) + '\n')

    # with open(path_txt + 'right_pitch_shoulder_angle.txt', 'a') as f:
    #     f.write(str(angle_right_shoulder_pitch(i)) + '\n')

print("Angle calculation is done")
time.sleep(2)
# shoulder_pitch = np.loadtxt(path_txt + 'right_pitch_shoulder_angle.txt')
# elbow_pitch = np.loadtxt(path_txt + 'right_elbow_angle.txt')
# shoulder_roll = np.loadtxt(path_txt + 'right_shoulder_angle.txt')
# arm_yaw = np.loadtxt(path_txt + 'right_arm_yam_angle.txt')

############################################################################################################
# print("Start the arm movement")
# for i in range(0, 10):
#     right_arm_movement(shoulder_pitch[i], shoulder_roll[i], arm_yaw[i], elbow_pitch[i])
# print("Arm movement is done")
############################################################################################################
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

# print(coeff_px_to_cm)
#
print(right_wrist_z * coeff_px_to_cm)
print(right_wrist * coeff_px_to_cm)

print("Start the inverse kinematic")
# Inverse Kinematic
inverse_kinematic(gamma, beta, alpha, right_wrist_z * coeff_px_to_cm, right_wrist * coeff_px_to_cm)
print("Inverse kinematic is done")

reachy.turn_off_smoothly('r_arm')