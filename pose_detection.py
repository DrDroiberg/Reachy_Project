import cv2 as cv
import mediapipe as mp
import numpy as np
import os

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic
mp_pose = mp.solutions.pose
mp_face_mesh = mp.solutions.face_mesh

########################################################################################################################
# Read the image file
path = 'C:/Users/vince/PycharmProjects/Reachy_Project/recognised_images'
folder = 'camera_opencv'

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_images = os.path.join(ROOT_DIR, "recognised_images")
path_txt = os.path.join(ROOT_DIR, "data_list")

def pose_recognition(duration):
    for i in range(0, duration):

        file = "camera_opencv/img_" + str(i) + ".jpg"

        with mp_pose.Pose(static_image_mode=True,
                          model_complexity=2,
                          enable_segmentation=True) as pose:

            body_image = cv.imread(file)

            results = pose.process(cv.cvtColor(body_image, cv.COLOR_BGR2RGB))

        annotated_image = body_image.copy()

        mp_drawing.draw_landmarks(annotated_image,
                                  results.pose_landmarks,
                                  mp_pose.POSE_CONNECTIONS,
                                  landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

        filename = "recognised_images/body_recognise_" + str(i) + ".png"
        cv.imwrite(filename, annotated_image)

        data_rlworld = np.empty((3, len(mp_holistic.PoseLandmark)))
        data_xyz = np.empty((3, len(mp_holistic.PoseLandmark)))

        landmarks = results.pose_world_landmarks.landmark
        for k in range(len(mp_holistic.PoseLandmark)):
            data_rlworld[0, k] = landmarks[k].x
            data_rlworld[1, k] = landmarks[k].y
            data_rlworld[2, k] = landmarks[k].z

        np.savetxt(os.path.join(path_txt, '/data_rlworld_img_' + str(i) + '.txt'), data_rlworld, delimiter=',',
                   fmt='%1.3f')  #

        landmarks = results.pose_landmarks.landmark
        for k in range(len(mp_holistic.PoseLandmark)):
            data_xyz[0, k] = landmarks[k].x
            data_xyz[1, k] = landmarks[k].y
            data_xyz[2, k] = landmarks[k].z

        np.savetxt(os.path.join(path_txt, '/data_xyz_img_' + str(i) + '.txt'), data_xyz, delimiter=',', fmt='%1.3f')  #
