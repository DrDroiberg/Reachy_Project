# Description: This file is the main file of the project. It will call all the other files to make the robot move.
from reachy_sdk import ReachySDK
import numpy as np
from coords_transfo import coordinate_transpo_r_wrist, coordinate_transpo_l_wrist
from inverse_kinematic import inverse_kinematic_v2_r_arm, inverse_kinematic_v2_l_arm, inverse_kinematic_v3_r_arm
from pose_detection import pose_recognition
import time
from reachy_sdk.trajectory import goto
import os

reachy = ReachySDK(host='localhost') # 10.117.68.17


#####################
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_txt = os.path.join(ROOT_DIR, "data_list")
#####################
gamma = 0
beta = 0
alpha = 0
#####################
nb_images = 15
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
# distance_right_wrist_shoulder_center = []
# distance_left_wrist_shoulder_center = []
#####################
reachy.turn_on('r_arm')
reachy.turn_on('l_arm')
#####################
goto({joint: pos for joint, pos in zip(reachy.r_arm.joints.values(), start_position)}, duration=2.0)
goto({joint: pos for joint, pos in zip(reachy.l_arm.joints.values(), start_position)}, duration=2.0)
#####################
time.sleep(5)
print("Start the camera")
# camera_capture()
print("Camera is done")
# time.sleep(2)
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
    # List of the right elbow position
    # right_elbow_position = coordinate_transpo_elbow(data)
    #####################
print("Transposition is done")
# print("Right elbow position: ", right_elbow_position)
# time.sleep(2)
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

    print("x_r_arm: ", x_r_arm, "image: ", i)

    old_movement_r_arm = inverse_kinematic_v2_r_arm(gamma, beta, alpha, z_r_arm, x_r_arm, -y_r_arm, old_movement_r_arm)
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

print('bloup')
goto({joint: pos for joint, pos in zip(reachy.r_arm.joints.values(), start_position)}, duration=6)
goto({joint: pos for joint, pos in zip(reachy.l_arm.joints.values(), start_position)}, duration=6)


#
#     # print("z_r_arm: ", z_r_arm, "right_elbow_position: ", right_elbow_position[i])
#
#     # right_elbow_present_position = right_elbow_position[i]
#     # if(z_r_arm < right_elbow_present_position):
#     #     print("check")
#     #     old_movement_r_arm = inverse_kinematic_v3_r_arm(gamma, beta, alpha, z_r_arm, -x_r_arm, y_r_arm, [random.random() * 100, random.random() * 100, random.random() * 100, random.random() * 100, random.random() * 100, random.random() * 100, random.random() * 100])
#
#     # print("Shoulder pitch", reachy.r_arm.r_shoulder_pitch.present_position)
#     # print("Wrist position", data[0][right_wrist])
#
#     # time.sleep(0.5)
#     # goto({joint: pos for joint, pos in zip(reachy.r_arm.joints.values(), old_movement_r_arm)}, duration=1.0)
#
#     # End of the condition
#
#     # right arm
#     # old_movement_r_arm = inverse_kinematic_v2_r_arm(gamma, beta, alpha, z_r_arm, -x_r_arm, y_r_arm, old_movement_r_arm) # z, x, y
# print("Right arm is done")
#
#
# # Inverse Kinematic of the left arm
# for i in range(0, duration):
#     # Left wrist
#     x_l_arm = distance_left_wrist_shoulder_center[i][0]
#     y_l_arm = distance_left_wrist_shoulder_center[i][1]
#     z_l_arm = distance_left_wrist_shoulder_center[i][2]
#
#     # print("X_l_arm: ", z_l_arm, "Y_l_arm: ", -x_l_arm, "Z_l_arm: ", y_l_arm) # z, x, y
#
#     # Condition to move the arm
#     # Position of the wrist
#     if z_l_arm < 0:
#         print("x_negative: ", z_l_arm)
#         z_l_arm = 0
#     if -x_l_arm < 0:
#         print("y_negative: ", -x_l_arm)
#         x_l_arm = 0
#     if y_l_arm < -0.30:
#         print("z_negative: ", y_l_arm)
#         y_l_arm = -0.30
#
#     # If the wrist is behind the elbow then the wrist is the elbow position
#     elbow_position = np.loadtxt('listes/distance_left_elbow_shoulder_center.txt', delimiter=',')
#     if z_l_arm < elbow_position[i][2]:
#         z_l_arm = elbow_position[i][2]
#
#
#     # End of the condition
#
#
#     # left arm
#     old_movement_l_arm = inverse_kinematic_v2_l_arm(gamma, beta, alpha, z_l_arm, -x_l_arm, y_l_arm, old_movement_l_arm) # z, x, y
# print("Left arm is done")
#
# print("Inverse kinematic is done")
#
reachy.turn_off_smoothly('r_arm')
reachy.turn_off_smoothly('l_arm')
