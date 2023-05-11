from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory import InterpolationMode
import cv2 as cv
import mediapipe as mp
import os


reachy = ReachySDK(host='localhost')
path = 'C:/Users/vince/PycharmProjects/Reachy_Project/recognised_images'

def recognition():
    # img = cv.imread('C:/Users/vince/PycharmProjects/Reachy_Project/camera_images/img_0.jpg')
    mpHands = mp.solutions.hands
    hands = mpHands.Hands()
    mpDraw = mp.solutions.drawing_utils

    # Real time hand recognition
    # while True:
    #     img = reachy.right_camera.last_frame
    #     imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    #     results = hands.process(imgRGB)
    #
    #     if results.multi_hand_landmarks:
    #         for handLms in results.multi_hand_landmarks:
    #             for id, lm in enumerate(handLms.landmark):
    #                 print(id, lm)
    #                 h, w, c = img.shape
    #                 cx, cy = int(lm.x * w), int(lm.y * h)
    #                 print(id, cx, cy)
    #                 # if id == 4:
    #                 cv.circle(img, (cx, cy), 15, (255, 0, 255), cv.FILLED)
    #             cv.imshow("Image", img)
    #             cv.waitKey(1)

##############################################################################################################
    # Hand recognition on a picture
    for i in range(0, 10):
        image = cv.imread('C:/Users/vince/PycharmProjects/Reachy_Project/camera_images/img_'+str(i)+'.jpg')
        img = image
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    print(id, lm)
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    print(id, cx, cy)

                    cv.circle(img, (cx, cy), 15, (255, 0, 255), cv.FILLED)
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
                cv.imwrite(os.path.join(path, 'img_recognise_'+str(i)+'.jpg'), img)
                cv.waitKey(1)
##############################################################################################################
