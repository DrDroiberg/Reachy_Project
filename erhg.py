import numpy as np
from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from Prog_cinematic_movement import Full_matrice_Rota
import time
from coords_transfo import coordinate_transpo_r_wrist, coordinate_transpo_l_wrist

i = 2
gamma = 0
beta = 0
alpha = 0

old_movement_r_arm = [0, 0, 0, 0, 0, 0, 0]
old_movement_l_arm = [0, 0, 0, 0, 0, 0, 0]

reachy = ReachySDK(host='10.117.68.17')

reachy.turn_on('r_arm')
reachy.turn_on('l_arm')

data = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/data_list/data_rlworld_img_' + str(i) + '.txt'
                  , delimiter=',')

distance_right_wrist_shoulder_center = coordinate_transpo_r_wrist(data)
distance_left_wrist_shoulder_center = coordinate_transpo_l_wrist(data)

print("distance_right_wrist_shoulder_center: ", distance_right_wrist_shoulder_center)

x_r_arm = distance_right_wrist_shoulder_center[0][0]
y_r_arm = distance_right_wrist_shoulder_center[0][1]
z_r_arm = distance_right_wrist_shoulder_center[0][2]

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

# print("X_r_arm: ", z_r_arm, "Y_r_arm: ", x_r_arm, "Z_r_arm: ", y_r_arm)  # z, x, y

movement = Full_matrice_Rota(gamma, beta, alpha, z_r_arm, x_r_arm, -y_r_arm)

final_position = reachy.r_arm.inverse_kinematics(movement, q0=old_movement_r_arm)

time.sleep(1)
goto({joint: pos for joint, pos in zip(reachy.r_arm.joints.values(), final_position)}, duration=1.0)

x_l_arm = distance_left_wrist_shoulder_center[0][0]
y_l_arm = distance_left_wrist_shoulder_center[0][1]
z_l_arm = distance_left_wrist_shoulder_center[0][2]

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

# print("X_l_arm: ", z_l_arm, "Y_l_arm: ", x_l_arm, "Z_l_arm: ", y_l_arm)  # z, x, y

movement = Full_matrice_Rota(gamma, beta, alpha, z_l_arm, x_l_arm, -y_l_arm)

final_position = reachy.l_arm.inverse_kinematics(movement, q0=old_movement_l_arm)

time.sleep(0.5)
goto({joint: pos for joint, pos in zip(reachy.l_arm.joints.values(), final_position)}, duration=1.0)

reachy.turn_off_smoothly('r_arm')
reachy.turn_off_smoothly('l_arm')