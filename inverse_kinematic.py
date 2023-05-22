import time
from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from Prog_cinematic_movement import Full_matrice_Rota

reachy = ReachySDK(host='localhost')
def inverse_kinematic(gamma, beta, alpha, right_wrist, wrist_z):
    for i in range(0, 10):
        mouvement = Full_matrice_Rota(gamma, beta, alpha, right_wrist[i][1], right_wrist[i][0], wrist_z[i])
        final_position = reachy.r_arm.inverse_kinematics(mouvement)
        time.sleep(0.5)
        goto({joint: pos for joint, pos in zip(reachy.r_arm.joints.values(), final_position)}, duration=1.0)