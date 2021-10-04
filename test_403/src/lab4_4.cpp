#include <moveit/move_group_interface/move_group.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>
#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit_msgs/DisplayRobotState.h>
#include <moveit_msgs/DisplayTrajectory.h>
#include <moveit_msgs/AttachedCollisionObject.h>
#include <moveit_msgs/CollisionObject.h>
#include <moveit_visual_tools/moveit_visual_tools.h>
#include <math.h>
#include <stdio.h>

// Main moveit libraries are included
int main(int argc, char **argv)
{
  double PI = 3.1415;
  ros::init(argc, argv, "move_group_interface_tutorial");
  ros::NodeHandle node_handle;
  ros::AsyncSpinner spinner(0);
  spinner.start(); // For moveit implementation we need AsyncSpinner, we cant use ros::spinOnce()
  static const std::string PLANNING_GROUP = "joint_gr"; /* Now we specify with what group we want work,
  here group1 is the name of my group controller*/
  moveit::planning_interface::MoveGroupInterface move_group(PLANNING_GROUP); // loading move_group

  const robot_state::JointModelGroup *joint_model_group =
      move_group.getCurrentState()->getJointModelGroup(PLANNING_GROUP); //For joint control
  geometry_msgs::PoseStamped current_pose;
  geometry_msgs::PoseStamped target_pose; // Pose in ROS is implemented using geometry_msgs::PoseStamped, google what is the type of this msg
  current_pose = move_group.getCurrentPose(); /* Retrieving the information about the
  current position and orientation of the end effector*/
  target_pose = current_pose; /* Basically our target pose is the same as current,
  except that we want to move it a little bit along x-axis*/
  ros::Rate loop_rate(50); //Frequency
  while (ros::ok()){
	  
	  double radius = 0.5;
	  double angle = 10.0;
	  double sine_y = 0.0;
	  double cos_y = 0.0;
	  double change = 0.0;
	  double center_x = current_pose.pose.position.x - radius;
	  
	  while (angle <= 370){
			sine_y = sin(angle*PI/180);
			cos_y = cos(angle*PI/180);
			
			if (angle >= 370){
				break;
			}
			target_pose.pose.position.y = sine_y;
			target_pose.pose.position.x = center_x + cos_y;
			move_group.setApproximateJointValueTarget(target_pose); // To calculate the trajectory
			move_group.move(); // Move the robot
			current_pose = move_group.getCurrentPose();
			angle = angle + 30;
			printf("Position: [%f ; %f]; Angle: %f \n", target_pose.pose.position.y, target_pose.pose.position.x, angle);
	}
	break;
    loop_rate.sleep();
  }

  ROS_INFO("Done");
  ros::shutdown();
  return 0;
}
