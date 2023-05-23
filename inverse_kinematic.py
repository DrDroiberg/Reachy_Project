import time
from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from Prog_cinematic_movement import Full_matrice_Rota
from conversion_px_cm import coeff_px_to_cm
import numpy as np

coeff = coeff_px_to_cm()

reachy = ReachySDK(host='localhost')
def inverse_kinematic(gamma, beta, alpha, wrist_z, right_wrist):
    for i in range(0, 10):
        print(coeff)
        wrist_x = right_wrist[i][0] * coeff
        wrist_y = right_wrist[i][1] * coeff
        print("right_wrist * coeff: ", wrist_x, " ", wrist_y)
        mouvement = Full_matrice_Rota(gamma, beta, alpha, 0 * coeff, wrist_x, wrist_y)
        final_position = reachy.r_arm.inverse_kinematics(mouvement)
        time.sleep(0.5)
        goto({joint: pos for joint, pos in zip(reachy.r_arm.joints.values(), final_position)}, duration=1.0)