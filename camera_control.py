from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory import InterpolationMode
import time
import cv2 as cv
import os

path = 'C:/Users/vince/PycharmProjects/Reachy_Project/camera_images'

reachy = ReachySDK(host='localhost')

img_file = []


def camera_control():
    for i in range(0, 10):
        img = reachy.right_camera.last_frame

        cv.imshow('Left Eye', img)
        cv.waitKey(500)
        cv.destroyAllWindows()
        img_file.append(img)

    # save the image from img_file in a folder
        # cv.imwrite(os.path.join(path, 'img_'+str(i)+'.jpg'), img_file[i])