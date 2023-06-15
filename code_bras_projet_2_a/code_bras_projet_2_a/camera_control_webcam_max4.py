#commenter
import cv2
import os

camera = cv2.VideoCapture(0)
i = 0
path = 'C:/Users/maxbu/dossPython/liste_Reachy/camera_opencv'

compteur_image = 100


while i < compteur_image:
    return_value, image = camera.read()

    cv2.imshow('Left Eye', image)
    cv2.waitKey(125)

    cv2.imwrite(os.path.join(path, 'img_'+str(i)+'.jpg'), image)
    i += 1
del(camera)

