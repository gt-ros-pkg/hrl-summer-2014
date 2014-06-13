#!/usr/bin/env python
# File 1: snap_node.py
# Caleb Little, HRL, 6/13/2014

# This file manages the image capture portion of the histogram check
# for Team RYDS' project. Once signaled from the master_node, this 
# function references the right wide_stereo color camera on a PR2
# and saves the files as either expected.jpeg or snapshot.jpeg in the 
# create directory CoHis. This service currently returns a -1 if a timeout
# occurs, and a 1 if a capture was succesful.
import os
from sensor_msgs.msg import CompressedImage
import rospy
import roslib; roslib.load_manifest('snapshot')
from snapshot.srv import *


class SingleSubscription(object):
    def snapshot(self, rospath='/wide_stereo/right/image_color/compressed', dest_path='./CoHis/snapshot.jpeg'):    
        self.done = False          
        self.path = os.path.abspath(dest_path)       
        self.subscriber = rospy.Subscriber(rospath, CompressedImage, self.callback)

    def callback(self, ros_msg):   
        self.subscriber.unregister()
        
        dest_dir = os.path.split(self.path)[0]    
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
	if not os.path.isfile('./CoHis/expected.jpeg'):
	    self.path = './CoHis/expected.jpeg'
        with open(self.path, 'w') as f:
            f.write(ros_msg.data)
        self.done = True

def bouncer(blarg):
  sub = SingleSubscription()
  sub.snapshot()
  print "I've been called"
  for i in range(15):
   if sub.done:
    return 1
    break
   rospy.rostime.wallsleep(0.5)
  return -1

def snapshot():
    print "running"
    rospy.init_node('snap_node')
    cheese = rospy.Service('snap_node', CompareHisto, bouncer)
    rospy.spin()

if __name__ == '__main__':
        snapshot()
