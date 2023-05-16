from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory import InterpolationMode

############################################################################################################
# Path of the angle
# shoulder_roll_angle = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/left_shoulder_angle.txt')
# elbow_pitch_angle = np.loadtxt('C:/Users/vince/PycharmProjects/Reachy_Project/listes/left_elbow_angle.txt')

############################################################################################################

time_movement = 2.5

reachy = ReachySDK(host='localhost')

def left_arm_movement(shoulder_roll_angle, elbow_pitch_angle):
    left_arm_position = {
        reachy.l_arm.l_shoulder_pitch: 0,
        reachy.l_arm.l_shoulder_roll: shoulder_roll_angle,
        reachy.l_arm.l_arm_yaw: 90,
        reachy.l_arm.l_elbow_pitch: elbow_pitch_angle - 180,
        reachy.l_arm.l_forearm_yaw: 0,
        reachy.l_arm.l_wrist_pitch: 0,
        reachy.l_arm.l_wrist_roll: 0,
    }

    left_arm_base = {
        reachy.l_arm.l_shoulder_pitch: 0,
        reachy.l_arm.l_shoulder_roll: 0,
        reachy.l_arm.l_arm_yaw: 0,
        reachy.l_arm.l_elbow_pitch: 0,
        reachy.l_arm.l_forearm_yaw: 0,
        reachy.l_arm.l_wrist_pitch: 0,
        reachy.l_arm.l_wrist_roll: 0,
    }

    goto(
        goal_positions=left_arm_position,
        duration=time_movement,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )


# for i in range(0, 10):
#     left_arm_movement(shoulder_roll_angle[i], elbow_pitch_angle[i])