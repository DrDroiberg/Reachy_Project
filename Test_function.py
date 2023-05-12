from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory import InterpolationMode
import time
import cv2 as cv

from camera_control import camera_control
from arm_recognition import arm_recognition
from angle_calculation import angle_shoulder

reachy = ReachySDK(host='localhost')

camera_control()