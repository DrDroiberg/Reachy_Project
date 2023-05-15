from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory import InterpolationMode
import time
import cv2 as cv
import mediapipe as mp
import math as m
import os
import pandas as pd
import numpy as np

path = 'C:/Users/vince/PycharmProjects/Reachy_Project/recognised_images'
reachy = ReachySDK(host='localhost')
left_shoulder_coords = []
right_shoulder_coords = []
left_elbow_coords = []
right_elbow_coords = []
left_wrist_coords = []
right_wrist_coords = []
left_hip_coords = []
right_hip_coords = []


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
        left_shoulder_coords.append([left_shoulder_x, left_shoulder_y])
        np.savetxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/left_shoulder_coords.txt', left_shoulder_coords,delimiter=", ", fmt='%s')

        # right shoulder
        right_shoulder_x = int(lm.landmark[lmPose.RIGHT_SHOULDER].x * body_image.shape[1])
        right_shoulder_y = int(lm.landmark[lmPose.RIGHT_SHOULDER].y * body_image.shape[0])
        right_shoulder_coords.append([right_shoulder_x, right_shoulder_y])
        np.savetxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_shoulder_coords.txt', right_shoulder_coords,delimiter=", ", fmt='%s')

        # left elbow
        left_elbow_x = int(lm.landmark[lmPose.LEFT_ELBOW].x * body_image.shape[1])
        left_elbow_y = int(lm.landmark[lmPose.LEFT_ELBOW].y * body_image.shape[0])
        left_elbow_coords.append([left_elbow_x, left_elbow_y])
        np.savetxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/left_elbow_coords.txt', left_elbow_coords,delimiter=", ", fmt='%s')

        # right elbow
        right_elbow_x = int(lm.landmark[lmPose.RIGHT_ELBOW].x * body_image.shape[1])
        right_elbow_y = int(lm.landmark[lmPose.RIGHT_ELBOW].y * body_image.shape[0])
        right_elbow_coords.append([right_elbow_x, right_elbow_y])
        np.savetxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_elbow_coords.txt', right_elbow_coords,delimiter=", ", fmt='%s')

        # left wrist
        left_wrist_x = int(lm.landmark[lmPose.LEFT_WRIST].x * body_image.shape[1])
        left_wrist_y = int(lm.landmark[lmPose.LEFT_WRIST].y * body_image.shape[0])
        left_wrist_coords.append([left_wrist_x, left_wrist_y])
        np.savetxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/left_wrist_coords.txt', left_wrist_coords,delimiter=", ", fmt='%s')

        # right wrist
        right_wrist_x = int(lm.landmark[lmPose.RIGHT_WRIST].x * body_image.shape[1])
        right_wrist_y = int(lm.landmark[lmPose.RIGHT_WRIST].y * body_image.shape[0])
        right_wrist_coords.append([right_wrist_x, right_wrist_y])
        np.savetxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_wrist_coords.txt', right_wrist_coords,delimiter=", ", fmt='%s')

        # left hip
        left_hip_x = int(lm.landmark[lmPose.LEFT_HIP].x * body_image.shape[1])
        left_hip_y = int(lm.landmark[lmPose.LEFT_HIP].y * body_image.shape[0])
        left_hip_coords.append([left_hip_x, left_hip_y])
        np.savetxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/left_hip_coords.txt', left_hip_coords,delimiter=", ", fmt='%s')

        # right hip
        right_hip_x = int(lm.landmark[lmPose.RIGHT_HIP].x * body_image.shape[1])
        right_hip_y = int(lm.landmark[lmPose.RIGHT_HIP].y * body_image.shape[0])
        right_hip_coords.append([right_hip_x, right_hip_y])
        np.savetxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/right_hip_coords.txt', right_hip_coords,delimiter=", ", fmt='%s')


##############################################################################################################
        # Drawing the landmarks on the images
        mpDraw.draw_landmarks(body_image, lm, mp_pose.POSE_CONNECTIONS)
        cv.imwrite(os.path.join(path, 'body_recognise_'+str(i)+'.jpg'), body_image)
        cv.waitKey(1)

##############################################################################################################





arm_recognition()

