from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory import InterpolationMode
import time
import cv2 as cv

from camera_control import camera_control
from arm_mouvement import dab
from hand_recognition import recognition

reachy = ReachySDK(host='localhost')

print("Begin camera control")
camera_control()
print("Camera control done")
time.sleep(2)
print("Begin recognition")
recognition()
print("Recognition done")
