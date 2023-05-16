import time

from reachy_sdk import ReachySDK
import numpy as np

from camera_control import camera_control
from arm_recognition import arm_recognition
from angle_calculation import angle_left_shoulder
from angle_calculation import angle_left_elbow
from reachy_movements import left_arm_movement

reachy = ReachySDK(host='localhost')


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
    angle = angle_left_shoulder(i)

    # save the right shoulder angle in a file
    with open('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_shoulder_angle.txt', 'a') as f:
        f.write(str(angle) + '\n')

    angle = angle_left_elbow(i)

    # save the right elbow angle in a file
    with open('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_elbow_angle.txt', 'a') as f:
        f.write(str(angle) + '\n')

print("Angle calculation is done")
time.sleep(2)
shoulder_roll_angle = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/left_shoulder_angle.txt')
elbow_pitch_angle = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/left_elbow_angle.txt')
time.sleep(2)
print("Start the arm movement")
for i in range(0, 10):
    left_arm_movement(shoulder_roll_angle[i], elbow_pitch_angle[i])
print("Arm movement is done")
