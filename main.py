import time

from reachy_sdk import ReachySDK
import numpy as np

from camera_control import camera_control
from arm_recognition import arm_recognition
from reachy_movements import right_arm_movement
from angle_calculation import angle_right_shoulder
from angle_calculation import angle_right_elbow
from angle_calculation import angle_right_arm_yam
from angle_calculation import angle_right_shoulder_pitch

reachy = ReachySDK(host='localhost')

path_txt = 'C:/Users/vince/PycharmProjects/Reachy_Project/listes/'

print("Start the camera")
camera_control()
print("Camera is done")
time.sleep(2)
print("Start the arm recognition")
arm_recognition()
print("Arm recognition is done")
time.sleep(2)
print("Start the angle calculation")
for i in range(0, 10):
    with open(path_txt + 'right_shoulder_angle.txt', 'a') as f:
        f.write(str(angle_right_shoulder(i)) + '\n')

    with open(path_txt + 'right_elbow_angle.txt', 'a') as f:
        f.write(str(angle_right_elbow(i)) + '\n')

    with open(path_txt + 'right_arm_yam_angle.txt', 'a') as f:
        f.write(str(angle_right_arm_yam(i)) + '\n')

    with open(path_txt + 'right_elbow_pitch_angle.txt', 'a') as f:
        f.write(str(angle_right_shoulder_pitch(i)) + '\n')

print("Angle calculation is done")
time.sleep(2)
shoulder_pitch = np.loadtxt(path_txt + 'right_pitch_shoulder_angle.txt')
elbow_pitch = np.loadtxt(path_txt + 'right_elbow_angle.txt')
shoulder_roll = np.loadtxt(path_txt + 'right_shoulder_angle.txt')
arm_yaw = np.loadtxt(path_txt + 'right_arm_yam_angle.txt')

print("Start the arm movement")
for i in range(0, 10):
    right_arm_movement(shoulder_pitch[i], shoulder_roll[i], arm_yaw[i], elbow_pitch[i])
print("Arm movement is done")
