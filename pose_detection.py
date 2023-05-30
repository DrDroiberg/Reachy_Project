import cv2 as cv
import mediapipe as mp
# import urllib.request
# import numpy as np
# import pickle
# import matplotlib as mpl
# from matplotlib import animation
# import PyQt5
# from PIL import Image
# from IPython.display import Video
import nb_helpers
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
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
path_txt = 'C:/Users/vince/PycharmProjects/Reachy_Project/data_list'
folder  = 'camera_opencv'
def pose_recognition():
    for i in range(0, 10):

        with mp_pose.Pose(static_image_mode=True, model_complexity=2, enable_segmentation=True) as pose:
            body_image = cv.imread('C:/Users/vince/PycharmProjects/Reachy_Project/' + folder + '/img_' + str(i) + '.jpg')
            results = pose.process(cv.cvtColor(body_image, cv.COLOR_BGR2RGB))

        annotated_image = body_image.copy()

        mp_drawing.draw_landmarks(annotated_image, results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS,
                                landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

        cv.imwrite(os.path.join(path, 'body_recognise_' + str(i) + '.jpg'), body_image)

        data = np.empty((3, len(mp_holistic.PoseLandmark)))

        landmarks = results.pose_world_landmarks.landmark
        for k in range(len(mp_holistic.PoseLandmark)):
            data[0, k] = landmarks[k].x
            data[1, k] = landmarks[k].y
            data[2, k] = landmarks[k].z

        np.savetxt(os.path.join(path_txt, 'data_img_' + str(i) + '.txt'), data, delimiter=',', fmt='%1.3f') #

    fig = plt.figure(figsize=(10, 10)) # inches
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(data[0, :], data[1, :], data[2, :], zdir='z')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

pose_recognition()

