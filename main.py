# Description: This file is the main file of the project. It will call all the other files to make the robot move.
from reachy_sdk import ReachySDK
import numpy as np
from camera_control_webcam import camera_capture
from coords_transfo import coordinate_transpo_r_wrist, coordinate_transpo_l_wrist
from inverse_kinematic import inverse_kinematic_v2_r_arm, inverse_kinematic_v2_l_arm
from pose_detection import pose_recognition
import time
from reachy_sdk.trajectory import goto
import os

reachy = ReachySDK(host='localhost') # 10.117.68.17


#####################
# Path of the data
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_txt = os.path.join(ROOT_DIR, "data_list")
#####################
# Variables of the inverse kinematic
gamma = 0
beta = 0
alpha = 0
#####################
# Number of images to treat
nb_images = 50
#####################
# Defining the landmarks
# Right
right_hip = 24
right_shoulder = 12
right_elbow = 14
right_wrist = 16

# Left
left_hip = 23
left_shoulder = 11
left_elbow = 13
left_wrist = 15
#####################
old_movement_r_arm = [0, 0, 0, -90, 0, 0, 0]
old_movement_l_arm = [0, 0, 0, -90, 0, 0, 0]
start_position = [0, 0, 0, -90, 0, 0, 0]
#####################
reachy.turn_on('r_arm')
reachy.turn_on('l_arm')
#####################
# start position
goto({joint: pos for joint, pos in zip(reachy.r_arm.joints.values(), start_position)}, duration=2.0)
goto({joint: pos for joint, pos in zip(reachy.l_arm.joints.values(), start_position)}, duration=2.0)
#####################
time.sleep(5)
print("Start the camera")
camera_capture()
print("Camera is done")
print("Start the arm recognition")
pose_recognition(nb_images)
print("Arm recognition is done")

print("Start transposition")
for i in range(0, nb_images):
    data = np.loadtxt(path_txt + '/data_rlworld_img_' + str(i) + '.txt'
                      , delimiter=',')

    #####################
    # Transposition to the center of the robot
    distance_right_wrist_shoulder_center = coordinate_transpo_r_wrist(data)
    distance_left_wrist_shoulder_center = coordinate_transpo_l_wrist(data)
    #####################
print("Transposition is done")
print("Start the inverse kinematic")

for i in range(0, nb_images):
    # Right wrist
    x_r_arm = distance_right_wrist_shoulder_center[i][0]
    y_r_arm = distance_right_wrist_shoulder_center[i][1]
    z_r_arm = distance_right_wrist_shoulder_center[i][2]
#
#     # print("X_r_arm: ", z_r_arm, "Y_r_arm: ", -x_r_arm, "Z_r_arm: ", y_r_arm) # z, x, y
#
    # Condition to move the arm
    # Position of the wrist
    if z_r_arm < 0:
        print("x_negative: ", z_r_arm)
        z_r_arm = 0.12
    if x_r_arm > 0:
        print("y_negative: ", x_r_arm)
        x_r_arm = -0.15
    if -y_r_arm < -0.30:
        print("z_negative: ", y_r_arm)
        y_r_arm = 0.30

    print("image: ", i)

    old_movement_r_arm = inverse_kinematic_v2_r_arm(gamma, beta, alpha, z_r_arm, x_r_arm, -y_r_arm, old_movement_r_arm)
    # np.savetxt(path_txt + '/right_arm_position'+str(i)+'.txt', old_movement_r_arm, delimiter=',')

# Left arm, not working

for i in range(0, nb_images):
    # Left wrist
    x_l_arm = distance_left_wrist_shoulder_center[i][0]
    y_l_arm = distance_left_wrist_shoulder_center[i][1]
    z_l_arm = distance_left_wrist_shoulder_center[i][2]
    # z_l_arm = 0

    # Condition to move the arm
    # Position of the wrist
    if z_l_arm < 0:
        print("x_negative: ", z_l_arm)
        z_l_arm = 0.12
    if x_l_arm < 0:
        print("y_negative: ", x_l_arm)
        x_l_arm = 0.15
    if -y_l_arm < -0.30:
        print("z_negative: ", y_l_arm)
        y_l_arm = 0.30

    print("z_r_arm: ", -y_r_arm, "image: ", i)

    old_movement_l_arm = inverse_kinematic_v2_l_arm(gamma, beta, alpha, z_l_arm, x_l_arm, -y_l_arm, old_movement_l_arm)
    # np.savetxt(path_txt + '/right_arm_position'+str(i)+'.txt', old_movement_l_arm, delimiter=',')


# return to the start position
goto({joint: pos for joint, pos in zip(reachy.r_arm.joints.values(), start_position)}, duration=6)
goto({joint: pos for joint, pos in zip(reachy.l_arm.joints.values(), start_position)}, duration=6)

reachy.turn_off_smoothly('r_arm')
reachy.turn_off_smoothly('l_arm')
