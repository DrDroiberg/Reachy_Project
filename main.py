# Description: This file is the main file of the project. It will call all the other files to make the robot move.
from reachy_sdk import ReachySDK
import numpy as np
from coordinate_transposition import coordinate_transposition_r_arm, coordinate_transposition_l_arm
from inverse_kinematic import inverse_kinematic_v2_r_arm, inverse_kinematic_v2_l_arm
from pose_detection import pose_recognition

reachy = ReachySDK(host='localhost')

path_txt = 'C:/Users/vince/PycharmProjects/Reachy_Project/data_list'

gamma = 0
beta = 0
alpha = 0
duration = 50

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
old_movement_r_arm = [0, 0, 0, 0, 0, 0, 0]
old_movement_l_arm = [0, 0, 0, 0, 0, 0, 0]
#####################
# distance_right_wrist_shoulder_center = []
# distance_left_wrist_shoulder_center = []
#####################
reachy.turn_on('r_arm')
reachy.turn_on('l_arm')
#####################

print("Start the camera")
# camera_capture()
print("Camera is done")
# time.sleep(2)
print("Start the arm recognition")
pose_recognition(duration)
print("Arm recognition is done")

print("Start transposition")
for i in range(0, duration):
    data = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/data_list/data_rlworld_img_' + str(i) + '.txt'
                      , delimiter=',')

    #####################
    # Transposition to the center of the robot
    distance_right_wrist_shoulder_center = coordinate_transposition_r_arm(data)
    distance_left_wrist_shoulder_center = coordinate_transposition_l_arm(data)
    #####################


    # print(distance_right_wrist_shoulder_center)
    # print(distance_left_wrist_shoulder_center)
print("Transposition is done")
# time.sleep(2)
print("Start the inverse kinematic")

# Inverse Kinematic of the right arm
for i in range(0, duration):
    # Right wrist
    x_r_arm = distance_right_wrist_shoulder_center[i][0]
    y_r_arm = distance_right_wrist_shoulder_center[i][1]
    z_r_arm = distance_right_wrist_shoulder_center[i][2]

    # print("X_r_arm: ", z_r_arm, "Y_r_arm: ", -x_r_arm, "Z_r_arm: ", y_r_arm) # z, x, y

    # right arm
    old_movement_r_arm = inverse_kinematic_v2_r_arm(gamma, beta, alpha, z_r_arm, -x_r_arm, y_r_arm, old_movement_r_arm) # z, x, y

# Inverse Kinematic of the left arm
for i in range(0, duration):
    # Left wrist
    x_l_arm = distance_right_wrist_shoulder_center[i][0]
    y_l_arm = distance_right_wrist_shoulder_center[i][1]
    z_l_arm = distance_right_wrist_shoulder_center[i][2]

    # print("X_l_arm: ", z_l_arm, "Y_l_arm: ", x_l_arm, "Z_l_arm: ", y_l_arm) # z, x, y

    # left arm
    old_movement_l_arm = inverse_kinematic_v2_l_arm(gamma, beta, alpha, z_l_arm, x_l_arm, y_l_arm, old_movement_l_arm) # z, x, y

print("Inverse kinematic is done")

reachy.turn_off_smoothly('r_arm')
reachy.turn_off_smoothly('l_arm')

# TODO: add the condition to move the arm
# TODO: resolve pb with the elbow