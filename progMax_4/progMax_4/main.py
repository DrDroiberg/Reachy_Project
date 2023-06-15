#commenter
#mes from a moi car pyzo fait chier
from os import path
import sys
sys.path.append(path.abspath('C:/Users/maxbu/Desktop/Projet_2A/progMax_4'))
#----------

import time
from reachy_sdk import ReachySDK
import numpy as np
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory import InterpolationMode
from arm_recognition_max4 import arm_recognition
from angle_calculation_max4 import angle_right_elbow
from coordinate_transposition_max4 import coordinate_transposition_right_xy
from coordinate_transposition_max4 import coordinate_transposition_left_xy
from z_coordinate_max4 import get_z
from inverse_kinematic_max4 import inverse_kinematic
from inverse_kinematic_max4 import mouvement_reachy
from conversion_px_cm_max4 import coeff_px_to_cm
from Prog_cinematic_movement_max4 import Full_matrice_Rota


reachy = ReachySDK(host='localhost')
#reachy = ReachySDK(host='10.117.68.17')

image_done = 0
path_txt = 'C:/Users/maxbu/dossPython/liste_Reachy/liste/'

gamma = 0
beta = 0
alpha = 0
compteur_image = 100

print("Start picture scaling")
coeff_px_to_cm = coeff_px_to_cm()
print("Picture scaling is done")



#les position pour les mouvement initiaux et finaux :
right_arm_starting = {

    reachy.r_arm.r_shoulder_pitch:0,
    reachy.r_arm.r_shoulder_roll: 0,
    reachy.r_arm.r_arm_yaw: 0,
    reachy.r_arm.r_elbow_pitch: - 90,
    reachy.r_arm.r_forearm_yaw:0,   #on fixe ces positions car peut utile
    reachy.r_arm.r_wrist_pitch: 0,
    reachy.r_arm.r_wrist_roll:0,
}






left_arm_starting = {

    reachy.l_arm.l_shoulder_pitch: 0,
    reachy.l_arm.l_shoulder_roll: 0,
    reachy.l_arm.l_arm_yaw: 0 ,
    reachy.l_arm.l_elbow_pitch: -90,
    reachy.l_arm.l_forearm_yaw:0,   #on fixe ces positions car peut utile
    reachy.l_arm.l_wrist_pitch: 0,
    reachy.l_arm.l_wrist_roll:0,
}

right_arm_middle = {

    reachy.r_arm.r_shoulder_pitch:0,
    reachy.r_arm.r_shoulder_roll: -45,
    reachy.r_arm.r_arm_yaw: 0,
    reachy.r_arm.r_elbow_pitch: - 130,
    reachy.r_arm.r_forearm_yaw:0,   #on fixe ces positions car peut utile
    reachy.r_arm.r_wrist_pitch: 0,
    reachy.r_arm.r_wrist_roll:0,
}






left_arm_middle = {

    reachy.l_arm.l_shoulder_pitch: 0,
    reachy.l_arm.l_shoulder_roll: 45,
    reachy.l_arm.l_arm_yaw: 0 ,
    reachy.l_arm.l_elbow_pitch: -130,
    reachy.l_arm.l_forearm_yaw:0,   #on fixe ces positions car peut utile
    reachy.l_arm.l_wrist_pitch: 0,
    reachy.l_arm.l_wrist_roll:0,
}


right_arm_droit = {

    reachy.r_arm.r_shoulder_pitch:0,
    reachy.r_arm.r_shoulder_roll: -90,
    reachy.r_arm.r_arm_yaw: 0,
    reachy.r_arm.r_elbow_pitch: 0,
    reachy.r_arm.r_forearm_yaw:0,   #on fixe ces positions car peut utile
    reachy.r_arm.r_wrist_pitch: 0,
    reachy.r_arm.r_wrist_roll:0,
}



left_arm_droit = {

    reachy.l_arm.l_shoulder_pitch: 0,
    reachy.l_arm.l_shoulder_roll: 90,
    reachy.l_arm.l_arm_yaw: 0 ,
    reachy.l_arm.l_elbow_pitch: 0,
    reachy.l_arm.l_forearm_yaw:0,   #on fixe ces positions car peut utile
    reachy.l_arm.l_wrist_pitch: 0,
    reachy.l_arm.l_wrist_roll:0,
}






if image_done == 0:
    print("Start the camera")
    # camera_capture(compteur_image)
    print("Camera is done")

    print("Start the arm recognition")
    arm_recognition(compteur_image)
    print("Arm recognition is done")

    print("Start the angle calculation")
    for i in range(0, compteur_image):

        with open(path_txt + 'right_elbow_angle.txt', 'a') as f:
            f.write(str(angle_right_elbow(i)) + '\n')

    print("Angle calculation is done")


    print("Start the points cantering")
    left_wrist_not_centered = np.loadtxt(path_txt + 'left_wrist_coords.txt', delimiter=',')
    right_wrist_not_centered = np.loadtxt(path_txt + 'right_wrist_coords.txt', delimiter=',')
    shoulder_coords_not_centered = np.loadtxt(path_txt + 'right_shoulder_coords.txt', delimiter=',')
    elbow_coords_not_centered = np.loadtxt(path_txt + 'right_elbow_coords.txt', delimiter=',')
    print("Points centering is done")

    print("Start the coordinate transposition")
    # Transform the coordinates to be used by the robot
    coordinate_transposition_left_xy(left_wrist_not_centered, 'left_wrist_coords_centered',compteur_image)
    coordinate_transposition_right_xy(right_wrist_not_centered, 'right_wrist_coords_centered',compteur_image)
    print("Coordinate transposition is done")

    #charge les coords de certains membres
    left_wrist_coords = np.loadtxt(path_txt + 'left_wrist_coords_centered.txt', delimiter=',')
    right_wrist_coords = np.loadtxt(path_txt + 'right_wrist_coords_centered.txt', delimiter=',')
    shoulder_coords = np.loadtxt(path_txt + 'shoulder_not_centered.txt', delimiter=',')
    elbow_coords = np.loadtxt(path_txt + 'elbow_coords_not_centered.txt', delimiter=',')


    print("Start the inverse kinematic")
    # Inverse Kinematic
    inverse_kinematic(gamma, beta, alpha, right_wrist_coords, left_wrist_coords, compteur_image)
    print("Inverse kinematic is done")


reachy.turn_on('r_arm')
reachy.turn_on('l_arm')


print("Start the movement")
#les mouvement de départs
goto(
    goal_positions=right_arm_starting,
    duration=0.5,
    interpolation_mode=InterpolationMode.MINIMUM_JERK
)

time.sleep(0.5)

goto(
    goal_positions=left_arm_starting,
    duration=0.5,
    interpolation_mode=InterpolationMode.MINIMUM_JERK
)
time.sleep(0.5)

goto(
    goal_positions=right_arm_middle,
    duration=0.5,
    interpolation_mode=InterpolationMode.MINIMUM_JERK
)

time.sleep(0.5)

goto(
    goal_positions=left_arm_middle,
    duration=0.5,
    interpolation_mode=InterpolationMode.MINIMUM_JERK
)
time.sleep(0.5)

goto(
    goal_positions=right_arm_droit,
    duration=0.5,
    interpolation_mode=InterpolationMode.MINIMUM_JERK
)

time.sleep(0.5)

goto(
    goal_positions=left_arm_droit,
    duration=0.5,
    interpolation_mode=InterpolationMode.MINIMUM_JERK
)
time.sleep(0.5)

print("depart fini ///////////////////////")
mouvement_reachy(compteur_image)

#♠sequence de fin
goto(
    goal_positions=right_arm_middle,
    duration=0.5,
    interpolation_mode=InterpolationMode.MINIMUM_JERK
)

time.sleep(0.5)

goto(
    goal_positions=left_arm_middle,
    duration=0.5,
    interpolation_mode=InterpolationMode.MINIMUM_JERK
)
time.sleep(0.5)
goto(
    goal_positions=right_arm_starting,
    duration=0.5,
    interpolation_mode=InterpolationMode.MINIMUM_JERK
)

time.sleep(0.5)

goto(
    goal_positions=left_arm_starting,
    duration=0.5,
    interpolation_mode=InterpolationMode.MINIMUM_JERK
)
time.sleep(0.5)
print("Movement is done")

reachy.turn_off_smoothly('r_arm')
reachy.turn_off_smoothly('l_arm')