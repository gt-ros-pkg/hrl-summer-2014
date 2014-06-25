#!/usr/bin/env python

import roslib
roslib.load_manifest('pr2_controllers_msgs')
roslib.load_manifest('actionlib')
roslib.load_manifest('geometry_msgs')
roslib.load_manifest('rospy')

import rospy
from actionlib_msgs.msg import *
import rospy
import actionlib
from pr2_controllers_msgs.msg import *
from geometry_msgs.msg import *

# This file demos the arm control system utilising the SimpleActionClient

if __name__ == '__main__':
    try:
        rospy.init_node('move_left_arm', anonymous=True)
        client = actionlib.SimpleActionClient('/l_arm_controller/joint_trajectory_action', JointTrajectoryAction)
        client.wait_for_server()

        goal = pr2_controllers_msgs.msg.JointTrajectoryGoal()
        goal.trajectory.joint_names.append("l_shoulder_pan_joint")
        goal.trajectory.joint_names.append("l_shoulder_lift_joint")
        goal.trajectory.joint_names.append("l_upper_arm_roll_joint")
        goal.trajectory.joint_names.append("l_elbow_flex_joint")
        goal.trajectory.joint_names.append("l_forearm_roll_joint")
        goal.trajectory.joint_names.append("l_wrist_flex_joint")
        goal.trajectory.joint_names.append("l_wrist_roll_joint")
        print goal.trajectory.joint_names

        point1 = trajectory_msgs.msg.JointTrajectoryPoint()
        point2 = trajectory_msgs.msg.JointTrajectoryPoint()
        point1.positions = [0.0, 0.0, 0.0,  0.0, 0.0, 0.0, 0.0]
        point2.positions = [-0.3, 0.2, -0.2, -1.2, 1.5, -0.3, 0.5]

        goal.trajectory.points = [point1, point2]

        goal.trajectory.points[0].time_from_start = rospy.Duration(2.0)
        goal.trajectory.points[1].time_from_start = rospy.Duration(4.0)

        goal.trajectory.header.stamp = rospy.Time.now()+rospy.Duration(1.0)
        
        client.send_goal(goal)
        print client.wait_for_result()
    except rospy.ROSInterruptException: pass
