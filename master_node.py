#!/usr/bin/env python
# File 3: master_node.py
# Caleb Little, HRL, 6/13/14

# This file manages the call sequence for the histogram check as part of
# Team RYDS' project. A return value of 0 indicates that the current image differers 
# somewhat significantly from the previous (recorded) image, whereas a return value
# of 1 indicates an acceptable change (<50)

# The CompareHisto srv form is as follows:
#
# int64 C
# ---
# int64 R

import roslib; roslib.load_manifest('snapshot')
roslib.load_manifest('rospy')
roslib.load_manifest('actionlib')
roslib.load_manifest('pr2_controllers_msgs')
roslib.load_manifest('geometry_msgs')
import actionlib
from actionlib_msgs.msg import *
from pr2_controllers_msgs.msg import *
from geometry_msgs.msg import *
import sys
import rospy
from snapshot.srv import *

def spotcheck():
    rospy.wait_for_service('compare_histo')	 
    print "histogram connected"
    rospy.wait_for_service('snap_node')
    print "snap connected"

rospy.init_node('Histogram', anonymous=True)

client = actionlib.SimpleActionClient('/head_traj_controller/point_head_action', PointHeadAction)
client.wait_for_server()

g = PointHeadGoal()
g.target.header.frame_id = 'l_gripper_tool_frame'
g.target.point.x = 0.0
g.target.point.y = -0.3
g.target.point.z = 0.1
g.min_duration = rospy.Duration(1.0)

client.send_goal(g)
client.wait_for_result()

if client.get_state() == GoalStatus.SUCCEEDED:
    print "Head Movement Succeeded"
else:
    print "Head Movement Failed"
print "stopped here"
try:
    pic = rospy.ServiceProxy('snap_node', CompareHisto)
    pit = 0
    pit = pic(0)
    while (1==1):
        if pit != 0:
            break
    if pit == -1:
        print "timeout error occured"
    rec = rospy.ServiceProxy('compare_histo', CompareHisto)
    ret = rec(0)
    print "made it this far"
    print "%d"%ret.R
    if ret.R == 1:
        print "No major change"
    elif ret.R == 0 :
        print "Changes occured"
    else :
        print "Image Loaded"
except rospy.ServiceException, e:
    print "Service call failed: %s"%e

if __name__ == "__main__":
    print "running"
    a = spotcheck()
