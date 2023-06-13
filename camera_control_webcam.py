import cv2
import os

camera = cv2.VideoCapture(0)
i = 0

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_images = os.path.join(ROOT_DIR, "camera_opencv")

compteur_image = 50


while i < compteur_image:
    return_value, image = camera.read()

    cv2.imshow('Left Eye', image)
    cv2.waitKey(125)

    cv2.imwrite(os.path.join(path_images, 'img_'+str(i)+'.jpg'), image)
    i += 1
del(camera)

