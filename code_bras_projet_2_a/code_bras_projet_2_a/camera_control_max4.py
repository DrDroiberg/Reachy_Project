#commenter
from reachy_sdk import ReachySDK
import time
import cv2 as cv
import os

path = 'C:/Users/maxbu/dossPython/liste_Reachy/camera_images'

reachy = ReachySDK(host='10.117.255.255')

img_file = []


def camera_control(compteur_image):
    for i in range(0, compteur_image):
        img = reachy.right_camera.last_frame

        cv.imshow('Left Eye', img)
        cv.waitKey(500)
        cv.destroyAllWindows()
        img_file.append(img)

    # save the image from img_file in a folder
        cv.imwrite(os.path.join(path, 'img_'+str(i)+'.jpg'), img_file[i])

#time.sleep(2)
#camera_control(compteur_image)