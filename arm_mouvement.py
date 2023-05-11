from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory import InterpolationMode
import time

time_movement = 2.5

reachy = ReachySDK(host='localhost')

def dab_arm():
    dab_left_arm_position = {
        reachy.l_arm.l_shoulder_pitch: -90,
        reachy.l_arm.l_shoulder_roll: 0,
        reachy.l_arm.l_arm_yaw: -75,
        reachy.l_arm.l_elbow_pitch: -120,
        reachy.l_arm.l_forearm_yaw: 0,
        reachy.l_arm.l_wrist_pitch: 0,
        reachy.l_arm.l_wrist_roll: 0,
    }
    dab_right_arm_position = {
        reachy.r_arm.r_shoulder_pitch: 0,
        reachy.r_arm.r_shoulder_roll: -120,
        reachy.r_arm.r_arm_yaw: 0,
        reachy.r_arm.r_elbow_pitch: 0,
        reachy.r_arm.r_forearm_yaw: 0,
        reachy.r_arm.r_wrist_pitch: 0,
        reachy.r_arm.r_wrist_roll: 0,
    }
    ####################################################
    dab_left_arm_base = {
        reachy.l_arm.l_shoulder_pitch: 0,
        reachy.l_arm.l_shoulder_roll: 0,
        reachy.l_arm.l_arm_yaw: 0,
        reachy.l_arm.l_elbow_pitch: 0,
        reachy.l_arm.l_forearm_yaw: 0,
        reachy.l_arm.l_wrist_pitch: 0,
        reachy.l_arm.l_wrist_roll: 0,
    }

    dab_right_arm_base = {
        reachy.r_arm.r_shoulder_pitch: 0,
        reachy.r_arm.r_shoulder_roll: 0,
        reachy.r_arm.r_arm_yaw: 0,
        reachy.r_arm.r_elbow_pitch: 0,
        reachy.r_arm.r_forearm_yaw: 0,
        reachy.r_arm.r_wrist_pitch: 0,
        reachy.r_arm.r_wrist_roll: 0,
    }
    ####################################################
    goto(
        goal_positions=dab_left_arm_position,
        duration=time_movement,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

    goto(
        goal_positions=dab_right_arm_position,
        duration=time_movement,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

    time.sleep(1.0)

    goto(
        goal_positions=dab_left_arm_base,
        duration=time_movement,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

    goto(
        goal_positions=dab_right_arm_base,
        duration=time_movement,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )


def head_movement():

    head_tilted = {
        reachy.head.neck_roll: 20,
        reachy.head.neck_pitch: 30,
        reachy.head.neck_yaw: 20,
    }

    head_base = {
        reachy.head.neck_roll: 0,
        reachy.head.neck_pitch: 0,
        reachy.head.neck_yaw: 0,
    }

    goto(
        goal_positions=head_tilted,
        duration=time_movement,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

    time.sleep(1.0)

    goto(
        goal_positions=head_base,
        duration=time_movement,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )


def dab():
    dab_arm()
    head_movement()


if __name__ == "__main__":
    reachy = ReachySDK(host='localhost')  # replace with correct IP if the simulation is not on your computer

    dab()
