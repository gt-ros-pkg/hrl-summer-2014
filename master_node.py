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
import sys
import rospy
from snapshot.srv import *

def spotcheck():
    rospy.wait_for_service('compare_histo')	 
    print "histogram connected"
    rospy.wait_for_service('snap_node')
    print "snap connected"
    try:
	pic = rospy.ServiceProxy('snap_node', CompareHisto)
	pit = 0
	pit = pic(0)
	while (1==1):
	   if pit != 0:
	     break
	if pit == -1:
	  print "timeout error occured"
          return -1
        rec = rospy.ServiceProxy('compare_histo', CompareHisto)
        ret = rec(0)
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
