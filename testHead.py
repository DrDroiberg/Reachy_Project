" Here the robot will try to imitate some human mouvement. The code contains human'skeleton with mediaPipe pretrained model. Then le robot will try to calculate the angles of the diffrent joints and the he'll get a direct mapping with his own joints. "


import numpy as np
import time
import cv2 as cv
import mediapipe as mp
from math import cos, sin, radians
import rclpy
from rclpy.node import Node
from reachyAudio import reachyAudioTextToSpeech
from reachy_sdk import ReachySDK
from sensor_msgs.msg._compressed_image import CompressedImage
from sensor_msgs.msg import Image, CameraInfo
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
import math
reachy = ReachySDK(host='localhost')  # Replace with the actual IP
reachy_audio = reachyAudioTextToSpeech.ReachyAudioTextToSpeech()

class RosCameraSubscriber(
                Node,
                ):
    """ROS node subscribing to the image topics."""

    def __init__(self, node_name: str, side: str) -> None:
        """Set up the node.

        Subscribe to the requested image topic (either /left_image or /right_image).
        """
        super().__init__(node_name=node_name)

        self.camera_sub = self.create_subscription(
            CompressedImage,
            side+'_image',
            self.on_image_update,
            1,
        )

        self.cam_img = None

    def on_image_update(self, msg):
        """Get data from image. Callback for "/'side'_image "subscriber."""
        data = np.frombuffer(msg.data.tobytes(), dtype=np.uint8)
        self.cam_img = cv.imdecode(data, cv.IMREAD_COLOR)

    def update_image(self):
        """Get the last image by spinning the node."""
        rclpy.spin_once(self)

def main():
	"""Instanciate the correct CameraViewer object for the requested side."""
	import argparse
	import pathlib
	parser = argparse.ArgumentParser()
	parser.add_argument('side')
	parser.add_argument('source')
	args = parser.parse_args()
	requested_side = args.side
	if requested_side not in ['left', 'right']:
		raise ValueError("side argument must either be 'left' or 'right'")
	viewing_source = args.source
	if viewing_source not in ['ros', 'opencv']:
		raise ValueError("source must either be 'ros' or 'opencv'")

	if viewing_source == 'ros':
		rclpy.init()
		time.sleep(1)
		image_getter = RosCameraSubscriber(node_name='image_viewer', side=requested_side)
	mp_pose = mp.solutions.pose
	mp_drawing = mp.solutions.drawing_utils
	mp_drawing_styles = mp.solutions.drawing_styles
	n=0
	while True:
		#images' update
		image_getter.update_image() 
		cv.imshow(args.side + ' camera', image_getter.cam_img)
		frame = image_getter.cam_img
		framergb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
	
		with mp_pose.Pose(
			static_image_mode = True, min_detection_confidence=0.5 , model_complexity=2) as pose :
			result = pose.process(framergb)
			annotated_image =frame.copy()
			mp_drawing.draw_landmarks(
				annotated_image,
				result.pose_landmarks,
				mp_pose.POSE_CONNECTIONS,
				landmark_drawing_spec= mp_drawing_styles.get_default_pose_landmarks_style() )
		#check patient's presence
		if not result.pose_landmarks:
			print ('none')
		else:
			#angles 'calculation
			#LEFT ARM
			angleLW = math.degrees(math.atan2(result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y-result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y , result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x-result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x) - math.atan2(result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_INDEX].y-result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y, result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_INDEX].x-result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x)) -180
			#print(angleLW)	
		
			angleLEL =- math.degrees(math.atan2(result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y-result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y , result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x-result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x) - math.atan2(result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y-result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y, result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x-result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x))
			
			if angleLEL < 0 :
				angleLEL += 360
			#print(angleLEL)
			angleLSH =- math.degrees(math.atan2(result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y-result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y , result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x-result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x) - math.atan2(result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y-result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y, result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].x-result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].x))
			
			if angleLSH < 0 :
				angleLSH += 360
			#print (angleLSH)
			angleLELP = math.degrees(math.atan2(result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].z-result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].z , result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].x-result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].x)) - 90
			#print (angleLELP)
			angleLSHP =- math.degrees(math.atan2(result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].z-result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].z , result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y-result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y))
			#print (angleLSHP)
			angleLWP =- math.degrees(math.atan2(result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].z-result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_INDEX].z , result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y-result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_INDEX].y))
			#print (angleLWP)
			#RIGHT ARM
			angleRW = math.degrees(math.atan2(result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y-result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y , result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x-result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x) - math.atan2(result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX].y-result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y, result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX].x-result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x)) -180
			#print(angleRW)	
		
			angleREL = math.degrees(math.atan2(result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y-result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y , result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x-result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x) - math.atan2(result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y-result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y, result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x-result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x))
			
			if angleREL < 0:
				angleREL += 360
			
			print(angleREL)
			angleRSH = math.degrees(math.atan2(result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y-result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y , result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x-result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x) - math.atan2(result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y-result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y, result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].x-result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x))
			
			if angleRSH < 0 :
				angleRSH += 360
			print (angleRSH)
			angleRSHP =- math.degrees(math.atan2(result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].z-result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].z , result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].y-result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].y))
			print (angleRSHP)
			angleRELP = math.degrees(math.atan2(result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].z-result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].z , result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x-result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x)) - 90
			print (angleRELP)
			angleRWP =- math.degrees(math.atan2(result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].z-result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX].z , result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].y-result.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_INDEX].y))
			#print (angleRWP)
			angleView= math.degrees(math.atan2(result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y-result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].y , result.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x-result.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP].x))
			#print (angleView)
			#if angleView <0:
				#angleView += 360
			if ((abs (angleView) - 180) <= 20):
				print('ok')
			#direct mapping between the patient and robot
			#condition to work without getting critical positions
			if (reachy.r_arm.r_shoulder_pitch > 20) and (reachy.r_arm.r_shoulder_pitch < 200) and (reachy.l_arm.l_shoulder_pitch > 20)  and (reachy.l_arm.l_shoulder_pitch < 200) :
				reachy.turn_on('r_arm')
				right_angled_position = {
						reachy.r_arm.r_shoulder_pitch : - angleRSHP,
						reachy.r_arm.r_shoulder_roll:-angleRSH,
						reachy.r_arm.r_arm_yaw: -angleRELP,
						reachy.r_arm.r_elbow_pitch :  -angleREL, #-150 
						reachy.r_arm.r_forearm_yaw : 0,
						reachy.r_arm.r_wrist_pitch : 0,#-angleRWP,
						reachy.r_arm.r_wrist_roll : angleRW,
						}
				goto (
        				goal_positions = right_angled_position,
    					duration = 1,
    					interpolation_mode = InterpolationMode.MINIMUM_JERK
					) 	
				reachy.turn_on('l_arm')
				right_angled_position = {
						reachy.l_arm.l_shoulder_pitch : 0, #angleLSHP
						reachy.l_arm.l_shoulder_roll:0, #angleLSH,
						reachy.l_arm.l_arm_yaw: angleLELP,
						reachy.l_arm.l_elbow_pitch : -90,#- angleLEL, #-150 
						reachy.l_arm.l_forearm_yaw : 0,
						reachy.l_arm.l_wrist_pitch : 0, #angleLWP,
						reachy.l_arm.l_wrist_roll : 0 ,#angleLW,
						}
				goto (
        				goal_positions = right_angled_position,
    					duration = 1,
    					interpolation_mode = InterpolationMode.MINIMUM_JERK
					)
				#reachy.turn_off_smoothly('r_arm')	
		cv.imshow("Result", annotated_image)	
		time.sleep(0.2)
		cv.waitKey(1)
			
			
			
cv.destroyAllWindows()
if __name__ == "__main__":
	main()	
			

