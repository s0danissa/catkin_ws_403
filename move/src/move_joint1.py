#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState

def commands():
    rospy.init_node('Joints_data')
    oldmot1 = 1
    oldmot2 = 1
    oldmot3 = 1
    oldmot4 = 1
    oldmot5 = 1
    motor1 = 0
    motor2 = 0
    motor3 = 0
    motor4 = 0
    motor5 = 0
    while oldmot1>=motor1 and oldmot2>=motor2 and oldmot3>=motor3 and oldmot4>=motor4 and oldmot5>=motor5:
    #while 1>0:
        motor1=float(input("Enter value for motor 1 "))
        motor2=float(input("Enter value for motor 2 "))
        motor3=float(input("Enter value for motor 3 "))
        motor4=float(input("Enter value for motor 4 "))
        motor5=float(input("Enter value for motor 5 "))
        pubmot1 = rospy.Publisher('/robot/joint1_position_controller/command', Float64, queue_size=5)
        pubmot2 = rospy.Publisher('/robot/joint2_position_controller/command', Float64, queue_size=5)
        pubmot3 = rospy.Publisher('/robot/joint3_position_controller/command', Float64, queue_size=5)
        pubmot4 = rospy.Publisher('/robot/joint4_position_controller/command', Float64, queue_size=5)
        pubmot5 = rospy.Publisher('/robot/joint5_position_controller/command', Float64, queue_size=5)
        oldmot1 = motor1
        oldmot2 = motor2
        oldmot3 = motor3
        oldmot4 = motor4
        oldmot5 = motor5
    #rate = rospy.Rate(50)
        while not False:
            pubmot1.publish(Float64(motor5))
            pubmot2.publish(Float64(motor2))
            pubmot3.publish(Float64(motor3))
            pubmot4.publish(Float64(motor4))
            pubmot5.publish(Float64(motor1))
            angles = rospy.wait_for_message('/robot/joint_states', JointState, timeout = 5)

	    if (abs(angles.position[4] - motor5) < 0.01 and abs(angles.position[1] - motor2) < 0.01 and \
	    abs(angles.position[2] - motor3) < 0.01 and abs(angles.position[3] - motor4) < 0.01 and abs(angles.position[0] - motor1) < 0.01):
                break
    #rate.sleep()

if __name__ == '__main__':
    try:
        commands()
    except rospy.ROSInterruptException:
        pass

