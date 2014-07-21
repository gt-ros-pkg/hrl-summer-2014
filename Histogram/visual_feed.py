#!/usr/bin/env python

# File 3: visual_feed.py
# Caleb Little, HRL, 7/10/2014

# This file is for debug purposes only. It will produce a 
# visual feed of what the compare histogram function will
# compute on, as long as the frame matches.

import os
from sensor_msgs.msg import CompressedImage
import rospy
import cv2
import roslib
roslib.load_manifest('rospy')
roslib.load_manifest('actionlib')
roslib.load_manifest('pr2_controllers_msgs')
roslib.load_manifest('geometry_msgs')
import actionlib
from actionlib_msgs.msg import *
from pr2_controllers_msgs.msg import *
from geometry_msgs.msg import *
import numpy as np
from matplotlib import pyplot as plt

# Two possible camera topics:
## /head_mount_kinect/rgb/image_color/compressed - More accurate, has auto-white issue
## /wide_stereo/right/image_color/compressed - Less accurate, set gain to cancel auto-white issue
class ActiveSubscription(object):
    def watcher(self, rospath='/wide_stereo/left/image_color/compressed'):
        self.done = False
        self.subscriber = rospy.Subscriber(rospath, CompressedImage, self.callback)
        print "Feed Enabled"
    
    def callback(self, ros_msg):
        with open('./data.jpeg', 'w') as f:
            f.write(ros_msg.data)
        img = cv2.imread('./data.jpeg')
        mask = np.zeros(img.shape[:2], np.uint8)
        mask[175:235,225:335] = 255 # Change this value to match mask
        img_masked = cv2.bitwise_and(img,img,mask = mask)
        img_b = cv2.Canny(img,100,200)
        cv2.imshow('ActiveFeed',img_masked) 
        # Above has three options:
        # img -> normal camera mode
        # img_masked -> filtered camera mode
        # img_b -> outlined version of full image
        cv2.waitKey(25) # Increase this number to increase
        # the number of seconds used per frame. Larger 
        # values will have some frame drop, but will run
        # on slower computers.

def video_feed():
    print "Booting Feed"
    rospy.init_node('visual_feed')
# Code up to line 59 below targets the spoon. Supress or modify as needed.
    client = actionlib.SimpleActionClient('/head_traj_controller/point_head_action', PointHeadAction)
    client.wait_for_server()

    g = PointHeadGoal()
    g.target.header.frame_id = 'l_gripper_tool_frame'
    g.target.point.x = 0.2
    g.target.point.y = -0.3
    g.target.point.z = -0.3
    g.min_duration = rospy.Duration(1.0)

    client.send_goal(g)
    client.wait_for_result()

#    if client.get_state() == GoalStatus.SUCCEEDED:
#        print "Head Movement Succeeded"
#    else:
#        print "Head Movement Failed"

    call = ActiveSubscription()
    call.watcher()
    rospy.spin()

if __name__ == '__main__':
    video_feed()
