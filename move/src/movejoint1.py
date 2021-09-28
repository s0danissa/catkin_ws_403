#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState

def commands():
    rospy.init_node('Joints_data')
    
    # Initiating variables
    old_m1, old_m2, old_m3, old_m4, old_m5 = 1, 1, 1, 1, 1 # values from the previous loop
    count = 0 # indicator for the first run
    motor1, motor2, motor3, motor4, motor5 = 0, 0, 0, 0, 0 # values for the current loop
    
    # Main loop
    while not False:
		# If the loop is not run for the first time update the old variables
		if count != 0:
			old_m1, old_m2, old_m3, old_m4, old_m5 = motor1, motor2, motor3, motor4, motor5
		
		# Obtain variables from the user
		motor1=float(input("Motor 1 new value: "))
		motor2=float(input("Motor 2 new value: "))
		motor3=float(input("Motor 3 new value: "))
		motor4=float(input("Motor 4 new value: "))
		motor5=float(input("Motor 5 new value: "))
		
		# If the new variables are smaller than old variables proceed to update publish variables
		if old_m1>=motor1 and old_m2>=motor2 and old_m3>=motor3 and old_m4>=motor4 and old_m5>=motor5:
			pub_1, pub_2, pub_3, pub_4, pub_5 = motor5,  motor2,  motor3, motor4, motor1
		# Else publish the same variables (no change)
		else:
			pub_1, pub_2, pub_3, pub_4, pub_5 = old_m5, old_m2, old_m3, old_m4, old_m1
		
		# Initiate publishers
		pubmot1 = rospy.Publisher('/robot/joint1_position_controller/command', Float64, queue_size=5)
		pubmot2 = rospy.Publisher('/robot/joint2_position_controller/command', Float64, queue_size=5)
		pubmot3 = rospy.Publisher('/robot/joint3_position_controller/command', Float64, queue_size=5)
		pubmot4 = rospy.Publisher('/robot/joint4_position_controller/command', Float64, queue_size=5)
		pubmot5 = rospy.Publisher('/robot/joint5_position_controller/command', Float64, queue_size=5)
		
		# Update indicator for the first run
		count = 1
		
		# Publish prepared variables
		while not False:
			pubmot1.publish(Float64(pub_1))
			pubmot2.publish(Float64(pub_2))
			pubmot3.publish(Float64(pub_3))
			pubmot4.publish(Float64(pub_4))
			pubmot5.publish(Float64(pub_5))
			angles = rospy.wait_for_message('/robot/joint_states', JointState, timeout = 5)
			
			if (abs(angles.position[4] - pub_1) < 0.01 and abs(angles.position[1] - pub_2) < 0.01 and \
			abs(angles.position[2] - pub_3) < 0.01 and abs(angles.position[3] - pub_4) < 0.01 and abs(angles.position[0] - pub_5) < 0.01):
				break

if __name__ == '__main__':
    try:
        commands()
    except rospy.ROSInterruptException:
        pass

