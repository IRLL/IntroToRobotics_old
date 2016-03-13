#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image #for recieving video feed
from geometry_msgs.msg import Twist # controlling the movements
from std_msgs.msg import Empty #send empty message for takeoff and landing
import numpy as np
import cv2
from image_converter import ToOpenCV

class QuadcopterController:
	def __init__(self):
		#create message subscriber for receiving images
		self.image_sub = rospy.Subscriber('/ardrone/image_raw', Image, self.image_callback)
		#create message publisher for sending drone movement commands
		self.movement_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
	
	def image_callback(self, image):
		image = ToOpenCV(image)
		cv2.imshow("camera", image)
		cv2.waitKey(1)
		#
		#do vision processing and control logic/commands here
		#


		#I'm just telling it to go straight up for now
		twist = Twist() #create new empty twist message
		twist.linear.z = 0.1
		self.movement_pub.publish(twist) #publish message



#callback function that gets run when node shuts down
def shutdown_callback():
	print "shutting down..."
	drone_land_pub.publish(Empty()) #make the drone land
	cv2.destroyAllWindows() #cleanup opencv windows
	print "done!"


if __name__ == "__main__":
	rospy.init_node("quadcopter_controller")
	#ardrone uses specialized topics for landing and taking off
	drone_takeoff_pub = rospy.Publisher('/ardrone/takeoff', Empty, queue_size=1)
	drone_land_pub = rospy.Publisher('/ardrone/land', Empty, queue_size=1)
	controller = QuadcopterController()

	#register callback function to land drone if we kill the program
	rospy.on_shutdown(shutdown_callback) 

	rospy.sleep(1) #wait for a second to wait for node to fully connect
	drone_takeoff_pub.publish(Empty()) #command drone to takeoff

	#this function loops and waits for node to shutdown
	#all logic happens in the image_callback function
	rospy.spin()

