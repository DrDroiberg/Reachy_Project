import time

from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from Prog_cinematic_movement import Full_matrice_Rota

reachy = ReachySDK(host='localhost')


# def inverse_kinematic(gamma, beta, alpha, shoulder_coords, elbow_coords, wrist_coords):
#     for i in range(0, 10):
#         wrist_z = get_depth(i)
#         wrist_x = wrist_coords[i][0] * coeff
#         wrist_y = wrist_coords[i][1] * coeff
#         print("right_wrist : "," ", wrist_z, " ", wrist_x, " ", wrist_y)
#         mouvement = Full_matrice_Rota(gamma, beta, alpha, wrist_z, wrist_x, wrist_y)
#         final_position = reachy.r_arm.inverse_kinematics(mouvement)
#         time.sleep(0.5)
#         goto({joint: pos for joint, pos in zip(reachy.r_arm.joints.values(), final_position)}, duration=1.0)

def inverse_kinematic_v2(gamma, beta, alpha, x, y, z, old_movement):

    movement = Full_matrice_Rota(gamma, beta, alpha, x, y, z)

    final_position = reachy.r_arm.inverse_kinematics(movement, q0=old_movement)

    time.sleep(0.5)
    goto({joint: pos for joint, pos in zip(reachy.r_arm.joints.values(), final_position)}, duration=1.0)

    return final_position
