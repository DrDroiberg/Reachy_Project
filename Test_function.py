import time

from reachy_sdk import ReachySDK
import numpy as np

from camera_control import camera_control
from arm_recognition import arm_recognition
from reachy_movements import right_arm_movement
from angle_calculation import angle_right_shoulder
from angle_calculation import angle_right_elbow
from angle_calculation import angle_right_arm_yam
from angle_calculation import angle_right_pitch


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
    angle_right_shoulder(i)
    angle_right_elbow(i)
    angle_right_arm_yam(i)
    angle_right_pitch(i)

print("Angle calculation is done")
time.sleep(2)

print("Start the arm movement")
for i in range(0, 10):
    right_arm_movement(shoulder_roll_angle[i], elbow_pitch_angle[i])

print("Arm movement is done")
