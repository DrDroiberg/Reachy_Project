from reachy_sdk import ReachySDK
import numpy as np
from coordinate_transposition import coordinate_transposition_r_arm, \
    coordinate_transpo_elbow, coordinate_transpo_r_shoulder, coordinate_transpo_r_hip, \
    coordinate_transpo_l_shoulder, coordinate_transpo_l_hip, coordinate_transpo_l_elbow, \
    coordinate_transposition_l_arm
from Prog_cinematic_movement import Full_matrice_Rota
from picture_calculation import findAngle
import random
from reachy_sdk.trajectory import goto

reachy = ReachySDK(host='localhost')

reachy.turn_on('r_arm')

#################
duration = 50
#################
right_shoulder = 12
left_shoulder = 11

right_wrist = 16
left_wrist = 15

right_elbow = 14
left_elbow = 13

right_hip = 24
left_hip = 23
#################
ancient_mouvement_r = [0,0,0,0,0,0,0]
ancient_mouvement_l = [0,0,0,0,0,0,0]
#################

def kinematic_right_arm(gamma, beta, alpha):

    compteur = 0
    global x_r_arm, y_r_arm, z_r_arm, x_r_shoulder, y_r_shoulder, z_r_shoulder, x_r_elbow, y_r_elbow, z_r_elbow

    for i in range(0, duration):
        # Load the data from the camera, it's in meter
        data = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/data_list'
                          '/data_rlworld_img_' + str(i) + '.txt', delimiter=',')

        # Calculating to the center of the robot
        right_wrist_coords = coordinate_transposition_r_arm(data)
        right_elbow_coords = coordinate_transpo_elbow(data)
        right_shoulder_coords = coordinate_transpo_r_shoulder(data)
        right_hip_coords = coordinate_transpo_r_hip(data)

    for i in range(0, duration):
        # Right wrist
        x_r_arm = right_wrist_coords[i][0]
        y_r_arm = right_wrist_coords[i][1]
        z_r_arm = right_wrist_coords[i][2]


        # print("X_r_arm: ", z_r_arm, "Y_r_arm: ", -x_r_arm, "Z_r_arm: ", y_r_arm) # z, x, y

        # Condition to move the arm
        # Position of the wrist
        if z_r_arm < 0:
            print("x_negative: ", z_r_arm)
            z_r_arm = 0
        if x_r_arm < 0:
            print("y_negative: ", x_r_arm)
            x_r_arm = 0
        if y_r_arm < -0.30:
            print("z_negative: ", y_r_arm)
            y_r_arm = -0.30

        movement = Full_matrice_Rota(gamma, beta, alpha, z_r_arm, -x_r_arm, y_r_arm)
        final_position = reachy.r_arm.inverse_kinematics(movement, q0=ancient_mouvement_r)

        # Calculating the angle of the shoulder
        # Right shoulder
        x_r_shoulder = right_shoulder_coords[i][0]
        y_r_shoulder = right_shoulder_coords[i][1]
        z_r_shoulder = right_shoulder_coords[i][2]

        # Right elbow
        x_r_elbow = right_elbow_coords[i][0]
        y_r_elbow = right_elbow_coords[i][1]
        z_r_elbow = right_elbow_coords[i][2]

        # Right hip
        x_r_hip = right_hip_coords[i][0]
        y_r_hip = right_hip_coords[i][1]
        z_r_hip = right_hip_coords[i][2]


        shoulder_roll = findAngle(x_r_shoulder, y_r_shoulder, x_r_elbow, y_r_elbow, x_r_hip, y_r_hip)


        if (shoulder_roll < -90):
            shoulder_roll = 270 - shoulder_roll
        else:
            shoulder_roll = 90 - shoulder_roll

        # print("Reachy goal position: ", reachy.r_arm.r_shoulder_pitch.goal_position)
        # print("Reachy present position: ", reachy.r_arm.r_shoulder_pitch.present_position)
        # print("finale position: ", final_position[0])

        reachy_goal_position = reachy.r_arm.r_shoulder_pitch.goal_position
        reachy_goal_roll_position = reachy.r_arm.r_shoulder_roll.goal_position

        # Calculating the right movement
        if (y_r_arm >= -0.3):
            while ((reachy_goal_position + 10 < final_position[0]) or (final_position[0]
                < reachy_goal_position - 10)) and ((reachy_goal_roll_position + 10 < final_position[1]) or (final_position[1]
                < reachy_goal_roll_position - 10)) and (compteur < 200) and (z_r_arm >= 0) and (-x_r_arm >= 0):

                random_number = random.sample(range(0, 100), 7)

                # Random angles
                gamma_2 = random.randrange(-180, 180, 1)
                beta_2 = random.randrange(-180, 180, 1)
                alpha_2 = random.randrange(-180, 180, 1)

                # Condition to move the arm
                if compteur < 130:
                    movement = Full_matrice_Rota(gamma_2, beta_2, alpha_2, z_r_arm, -x_r_arm, y_r_arm)

                else:
                    movement = Full_matrice_Rota(gamma, beta, alpha, 0.15, -x_r_arm, y_r_arm)

                final_position = reachy.r_arm.inverse_kinematics(movement, q0=random_number)

                compteur += 1

                # Condition to stop the arm
                if compteur == 200:
                    final_position = reachy.r_arm.inverse_kinematics(movement, q0=ancient_mouvement_r)

        # elif(-x_r_arm > 0):
        #     x_r_arm = 0
        #
        # else:
        #     z_r_arm = 0

        compteur = 0



        goto({joint: pos for joint, pos in zip(reachy.r_arm.joints.values(), final_position)}, duration=1.0)

def kinematic_left_arm(gamma, beta, alpha):
    compteur = 0

    for i in range(0, duration):
        # Load the data from the camera, it's in meter
        data = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/data_list'
                          '/data_rlworld_img_' + str(i) + '.txt', delimiter=',')

        # Calculating to the center of the robot
        left_wrist_coords = coordinate_transposition_l_arm(data)
        left_elbow_coords = coordinate_transpo_l_elbow(data)
        left_shoulder_coords = coordinate_transpo_l_shoulder(data)
        left_hip_coords = coordinate_transpo_l_hip(data)

    for i in range(0, duration):
        # Right wrist
        x_l_arm = left_wrist_coords[i][0]
        y_l_arm = left_wrist_coords[i][1]
        z_l_arm = left_wrist_coords[i][2]

        # Condition to move the arm
        # Position of the wrist
        if z_l_arm > 0:
            print("x_negative: ", z_l_arm)
            z_l_arm = 0
        if x_l_arm < 0.1:
            print("y_negative: ", x_l_arm)
            x_l_arm = 0.1
        if y_l_arm > -0.30:
            print("z_negative: ", y_l_arm)
            y_l_arm = 0.30

        movement = Full_matrice_Rota(gamma, beta, alpha, -z_l_arm, x_l_arm, -y_l_arm)
        final_position = reachy.l_arm.inverse_kinematics(movement, q0=ancient_mouvement_r)

        # Calculating the angle of the shoulder
        # Right shoulder
        x_l_shoulder = left_shoulder_coords[i][0]
        y_l_shoulder = left_shoulder_coords[i][1]
        z_l_shoulder = left_shoulder_coords[i][2]

        # Right elbow
        x_l_elbow = left_elbow_coords[i][0]
        y_l_elbow = left_elbow_coords[i][1]
        z_l_elbow = left_elbow_coords[i][2]

        # Right hip
        x_l_hip = left_hip_coords[i][0]
        y_l_hip = left_hip_coords[i][1]
        z_l_hip = left_hip_coords[i][2]


        shoulder_roll = findAngle(x_l_shoulder, y_l_shoulder, x_l_elbow, y_l_elbow, x_l_hip, y_l_hip)


        if (shoulder_roll < -90):
            shoulder_roll = 270 - shoulder_roll
        else:
            shoulder_roll = 90 - shoulder_roll

        # print("Reachy goal position: ", reachy.l_arm.l_shoulder_pitch.goal_position)
        # print("Reachy present position: ", reachy.l_arm.l_shoulder_pitch.present_position)
        # print("finale position: ", final_position[0])

        reachy_goal_position = reachy.l_arm.l_shoulder_pitch.goal_position
        reachy_goal_roll_position = reachy.l_arm.l_shoulder_roll.goal_position

        # Calculating the right movement
        if (y_l_arm >= -0.3):
            while ((reachy_goal_position + 10 < final_position[0]) or (final_position[0]
                < reachy_goal_position - 10)) and ((reachy_goal_roll_position + 10 < final_position[1]) or (final_position[1]
                < reachy_goal_roll_position - 10)) and (compteur < 200):

                random_number = random.sample(range(0, 100), 7)

                # Random angles
                gamma_2 = random.randrange(-180, 180, 1)
                beta_2 = random.randrange(-180, 180, 1)
                alpha_2 = random.randrange(-180, 180, 1)

                print("x_l_arm: ", z_l_arm)
                # print("y_l_arm: ", x_l_arm)
                # print("z_l_arm: ", y_l_arm)

                # Condition to move the arm
                if compteur < 130:
                    movement = Full_matrice_Rota(gamma_2, beta_2, alpha_2, -z_l_arm, x_l_arm, -y_l_arm)

                else:
                    movement = Full_matrice_Rota(gamma, beta, alpha, 0.15, x_l_arm, -y_l_arm)

                final_position = reachy.l_arm.inverse_kinematics(movement, q0=random_number)

                compteur += 1

                # Condition to stop the arm
                if compteur == 200:
                    final_position = reachy.l_arm.inverse_kinematics(movement, q0=ancient_mouvement_r)

        compteur = 0



        goto({joint: pos for joint, pos in zip(reachy.l_arm.joints.values(), final_position)}, duration=1.0)
