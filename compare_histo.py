#!/usr/bin/env python
# File 2: compare_histo.py
# Caleb Little, HRL, 6/13/2014

# This file preforms histogram analysis on files created by snap_node.py.
# It locates two files, expected.jpeg and snapshot.jpeg, in the directory
# CoHis, and preforms a deviation check of their histograms. If the difference
# is greater than the expected value (50), the server returns 0, whereas if 
# the difference is acceptable, the server returns 1. If only one file was located,
# the server returns a -1.
import roslib; roslib.load_manifest('snapshot')
from snapshot.srv import *
import rospy
import cv2
import numpy as np
from matplotlib import pyplot as plt


def analyze_image(num):
    print "I've been Called"
    img = cv2.imread('./CoHis/expected.jpeg',0)
    hist_norm = cv2.calcHist([img], [0], None, [256], [0,256])
    current = cv2.imread('./CoHis/snapshot.jpeg',0)
    hist_current = cv2.calcHist([current],[0],None,[256],[0,256])
    sum_norm = 0
    sum_current = 0
    for i in hist_current:
	if i != 0:
	   sum_current = 1
    if sum_current == 0:
	return -1
    else:
	sum_current = 0

    for i in range(0,len(hist_norm)): # will need to update this with appropriate area
        if i > 1 and i < 255: 
	   sum_norm = sum_norm + hist_norm[i]
           sum_current = sum_current + hist_current[i]
    print "#%d#"%abs(sum_norm - sum_current)
    if abs(sum_norm - sum_current) > 50:
     return 0
    else:
     return 1
def compare_histo():
    print "Running"
    rospy.init_node('compare_histo')
    hisp = rospy.Service('compare_histo',CompareHisto, analyze_image)
    rospy.spin()

if __name__ == '__main__':
        compare_histo()
