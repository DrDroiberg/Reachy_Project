from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory import InterpolationMode
import time
import cv2 as cv

reachy = ReachySDK(host='localhost')


def camera_control():
    while True:
        img = reachy.right_camera.last_frame

        cv.imshow('Left Eye', img)
        cv.waitKey(500)
        cv.destroyAllWindows()
