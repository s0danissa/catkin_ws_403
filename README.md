# ROBT 403 Lab Assignment 3 - Part 1 & 2
## Part 1 - Joint movement of the planar robot
**TASK:** Create a rosnode that will “listen” for std_msgs/Float64 type data and “publish” this data to the joint of the planar robot. The node should send the command to move if the any new incoming value is lower than the previous one.
## Video Demo 1



https://user-images.githubusercontent.com/52815976/135121698-a484a2d1-5b12-42b4-84dc-bbe4429f0d98.mp4

## Part 2 - Step and sine wave response of the planar robot
**TASK:** 

II) Get the step response of (you can create a node that will send a square-wave function): 
  1.the joint at the base of the robot
  2.the joint at the end-effector of the robot
  
III) Get the sine-wave response of (you can create a node that will send a sine-wave function): 
  3.the joint at the base of the robot
  4.the joint at the end-effector of the robot
  
## Video Demo 2


https://user-images.githubusercontent.com/52815976/135628921-3c76a758-85ec-49fc-86f1-319f04e6b99a.mp4

## RQT sine wave and step response Screenshots
### Sine-wave end-effector response graph
![sine_e](sine_endj.png)
### Sine-wave base joint response graph
![sine_b](sine_basej.png)
### Step end-effector response graph
![step_e](step_endj.png)
### Step base joint response graph
![step_b](step_endj.png)
