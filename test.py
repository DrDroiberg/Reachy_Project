import cv2
import mediapipe as mp
import urllib.request
import numpy as np
import pickle
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import animation
# import PyQt5
from PIL import Image
from IPython.display import Video
import nb_helpers

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic
mp_pose = mp.solutions.pose
mp_face_mesh = mp.solutions.face_mesh

for i in range(0, 10):
# Specify the image filename
    file = 'C:/Users/vince/PycharmProjects/Reachy_Project/camera_opencv/img_'+str(i)+'.jpg'

# Create a MediaPipe `Pose` object
    with mp_pose.Pose(static_image_mode=True,
                    model_complexity=2,
                    enable_segmentation=True) as pose:
    # Read the file in and get dims
        image = cv2.imread(file)

    # Convert the BGR image to RGB and then process with the `Pose` object.
        results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

# Copy the iamge
    annotated_image = image.copy()

# Draw pose, left and right hands, and face landmarks on the image with drawing specification defaults.
    mp_drawing.draw_landmarks(annotated_image,
                          results.pose_landmarks,
                          mp_pose.POSE_CONNECTIONS,
                          landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

# Save image with drawing
    filename = "recognised_images/body_recognise_" + str(i) + ".png"
    cv2.imwrite(filename, annotated_image)
