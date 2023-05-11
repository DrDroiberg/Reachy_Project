from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory import InterpolationMode
import time
import cv2 as cv
import mediapipe as mp
import math as m
import os

path = 'C:/Users/vince/PycharmProjects/Reachy_Project/recognised_images'
reachy = ReachySDK(host='localhost')
def offset_distance(x1, y1, x2, y2):
    dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return dist

def findAngle(x1, y1, x2, y2):
    theta = m.acos((x2 - x1) / offset_distance(x1, y1, x2, y2))
    degree = theta * int(180 / m.pi)
    return degree

def arm_recognition():
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    mpDraw = mp.solutions.drawing_utils

    for i in range(0, 10):
        body_image = cv.imread('C:/Users/vince/PycharmProjects/Reachy_Project/camera_images/img_'+str(i)+'.jpg')
        imgRGB = cv.cvtColor(body_image, cv.COLOR_BGR2RGB)
        results = pose.process(imgRGB)

        lm = results.pose_landmarks
        lmPose = mp_pose.PoseLandmark
##############################################################################################################
        #Acquiring the coordinates of the landmarks

        # left shoulder
        left_shoulder_x = int(lm.landmark[lmPose.LEFT_SHOULDER].x * body_image.shape[1])
        left_shoulder_y = int(lm.landmark[lmPose.LEFT_SHOULDER].y * body_image.shape[0])

        # right shoulder
        right_shoulder_x = int(lm.landmark[lmPose.RIGHT_SHOULDER].x * body_image.shape[1])
        right_shoulder_y = int(lm.landmark[lmPose.RIGHT_SHOULDER].y * body_image.shape[0])

        # left elbow
        left_elbow_x = int(lm.landmark[lmPose.LEFT_ELBOW].x * body_image.shape[1])
        left_elbow_y = int(lm.landmark[lmPose.LEFT_ELBOW].y * body_image.shape[0])

        # right elbow
        right_elbow_x = int(lm.landmark[lmPose.RIGHT_ELBOW].x * body_image.shape[1])
        right_elbow_y = int(lm.landmark[lmPose.RIGHT_ELBOW].y * body_image.shape[0])

        # left wrist
        left_wrist_x = int(lm.landmark[lmPose.LEFT_WRIST].x * body_image.shape[1])
        left_wrist_y = int(lm.landmark[lmPose.LEFT_WRIST].y * body_image.shape[0])

        # right wrist
        right_wrist_x = int(lm.landmark[lmPose.RIGHT_WRIST].x * body_image.shape[1])
        right_wrist_y = int(lm.landmark[lmPose.RIGHT_WRIST].y * body_image.shape[0])


##############################################################################################################
        # Drawing the landmarks
        mpDraw.draw_landmarks(body_image, lm, mp_pose.POSE_CONNECTIONS)
        cv.imwrite(os.path.join(path, 'body_recognise_'+str(i)+'.jpg'), body_image)
        cv.waitKey(1)

