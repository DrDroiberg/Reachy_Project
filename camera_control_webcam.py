import cv2
import os
from reachy_sdk import ReachySDK

camera = cv2.VideoCapture(0)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_images = os.path.join(ROOT_DIR, "camera_opencv")

reachy = ReachySDK(host='localhost') # 10.117.68.17

compteur_image = 50

def camera_capture():
    i = 0

    while i < compteur_image:
        img = reachy.right_camera.last_frame

        cv2.imshow('Right Eye', img)
        cv2.waitKey(125)

        cv2.imwrite(os.path.join(path_images, 'img_' + str(i) + '.jpg'), img)
        i += 1
del (camera)
