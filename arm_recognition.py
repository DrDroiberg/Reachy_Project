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
coordinates = []

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

        # left hip
        left_hip_x = int(lm.landmark[lmPose.LEFT_HIP].x * body_image.shape[1])
        left_hip_y = int(lm.landmark[lmPose.LEFT_HIP].y * body_image.shape[0])

        # right hip
        right_hip_x = int(lm.landmark[lmPose.RIGHT_HIP].x * body_image.shape[1])
        right_hip_y = int(lm.landmark[lmPose.RIGHT_HIP].y * body_image.shape[0])


##############################################################################################################
        # Drawing the landmarks on the images
        mpDraw.draw_landmarks(body_image, lm, mp_pose.POSE_CONNECTIONS)
        cv.imwrite(os.path.join(path, 'body_recognise_'+str(i)+'.jpg'), body_image)
        cv.waitKey(1)

##############################################################################################################
        # Stocking the coordinates in a list, it's a 3D list
        coordinates.append([[left_shoulder_x, left_shoulder_y], [right_shoulder_x, right_shoulder_y],
                        [left_elbow_x, left_elbow_y], [right_elbow_x, right_elbow_y],
                        [left_wrist_x, left_wrist_y], [right_wrist_x, right_wrist_y],
                            [left_hip_x, left_hip_y], [right_hip_x, right_hip_y]])

    # Save the coordinates list in a file
    with open('C:/Users/vince/PycharmProjects/Reachy_Project/coordinates.txt', 'w') as f:
        for item in coordinates:
            f.write("%s\n" % item)
    f.close()

