import cv2
import os

camera = cv2.VideoCapture(0)
i = 0
path = 'C:/Users/vince/PycharmProjects/Reachy_Project/camera_opencv'

duration = 50  # second

while i < duration:
    return_value, image = camera.read()

    cv2.imshow('Left Eye', image)
    cv2.waitKey(100)

    cv2.imwrite(os.path.join(path, 'img_'+str(i)+'.jpg'), image)
    i += 1
del(camera)

