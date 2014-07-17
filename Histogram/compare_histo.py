#!/usr/bin/env python
# File 2: compare_histo.py
# Caleb Little, HRL, 6/13/2014

# This file preforms histogram analysis on files created by snap_node.py.
# It locates two files, expected.jpeg and snapshot.jpeg, in the directory
# CoHis, and preforms a centered deviation check via histograms. If the difference
# is greater than the expected value (20), the server returns 0, whereas if 
# the difference is acceptable, the server returns 1. Given a succesful 
# comparison, the server will update the stored image. If only one file was 
# located, the server returns a -1. Must be run in the same folder as 
# snap_node.py! (Taken care of by launch file.)
import roslib; roslib.load_manifest('snapshot')
from snapshot.srv import *
import rospy
import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

def analyze_image(num):
    print "I've been called - analyze_image"
    img = cv2.imread('./CoHis/expected.jpeg')
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[300:385,200:335] = 225
    hist_norm = cv2.calcHist([img], [0], mask, [256], [0,256])
    current = cv2.imread('./CoHis/snapshot.jpeg')
    hist_current = cv2.calcHist([current],[0],mask,[256],[0,256])
    current_masked = cv2.bitwise_and(current,current, mask = mask)
    max_norm = 0
    norm_loc = 0
    max_current = 0
    current_loc = 0
    for i in hist_current:
	if i != 0:
	   max_current = 1
    if max_current == 0:
	print "Unable to locate snapshot.jpeg."
        return -1
    else:
	max_current = 0
    
    #Uncomment below to see what images are being processed
    #cv2.imshow('compared to', img)
    #cv2.imshow('comparing', current_masked)
    #cv2.waitKey(4500)
    #cv2.destroyAllWindows()

    for i in range(0,len(hist_norm)): # will need to update this with appropriate area mask
        if i > 5 and i < 200: 
	   if hist_norm[i] > max_norm:
               max_norm = hist_norm[i] 
               norm_loc = i
           if hist_current[i] > max_current:
               max_current = hist_norm[i]
               current_loc = i
    print "#%d#"%abs(norm_loc - current_loc)
    if abs(norm_loc - current_loc) > 10:
     return 0
    else:
     os.rename('./CoHis/snapshot.jpeg','./CoHis/expected.jpeg')
     return 1

def compare_histo():
    print "I'm running - compare_histo"
    rospy.init_node('compare_histo')
    hisp = rospy.Service('compare_histo', CompareHisto, analyze_image)
    rospy.spin()

if __name__ == '__main__':
        compare_histo()
