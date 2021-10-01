#!/usr/bin/env python
import rospy
from time import sleep
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
import numpy as np

def commands():
    rospy.init_node('Joints_data')
    
    # Initiating variables
    out_v = 0.0
    rad = 0.0
    sine_val = 0.0
    
    ind = 0
    mt = 0
    
    # Main loop
    while not False:
		# Obtain variables from the user
		if ind == 0:
			ind = int(input("Enter mode: 1-for sine wave, 2-for step wave ---> "))
		if mt == 0:
			mt = int(input("Enter motor: 1-base, 2-end --->"))
		while not False:
			# Changing output function
			if ind == 1:
				rad += 0.1
				out_v = np.sin(rad)
				sleep(0.1)
			elif ind == 2:
				if out_v == 0:
					out_v = 1
					sleep(2)
				else:
					out_v = 0
					sleep(2)
			
			# Published values
			if mt == 1:
				pub_1 = out_v
				pub_5 = 0
			elif mt == 2:
				pub_5 = out_v
				pub_1 = 0
			
			# Initiate publishers
			pubmot1 = rospy.Publisher('/robot/joint1_position_controller/command', Float64, queue_size=5)
			pubmot5 = rospy.Publisher('/robot/joint5_position_controller/command', Float64, queue_size=5)
			
			# Publish prepared variables
			while not False:
				pubmot1.publish(Float64(pub_1))
				pubmot5.publish(Float64(pub_5))
				angles = rospy.wait_for_message('/robot/joint_states', JointState, timeout = 5)
				
				if (abs(angles.position[4] - pub_1) < 0.01 and abs(angles.position[0] - pub_5) < 0.01):
					break

if __name__ == '__main__':
    try:
        commands()
    except rospy.ROSInterruptException:
        pass

