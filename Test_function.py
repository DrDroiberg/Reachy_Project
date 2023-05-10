from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory import InterpolationMode
import time
import cv2 as cv

from camera_control import camera_control
from arm_mouvement import dab

reachy = ReachySDK(host='localhost')

while True:
    dab()
    camera_control()
    time.sleep(1)

