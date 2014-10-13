#!/usr/bin/env python
# File 2: compare_histo.py
# Caleb Little, HRL, 6/13/2014

# This file preforms histogram analysis on files created by snap_node.py.
# It locates two files, expected.jpeg and snapshot.jpeg, in the directory
# CoHis, and preforms a deviation check using histograms. If the difference
# is greater than the expected value (10), the server returns 0, whereas if 
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
    b, g, r = cv2.split(img)
    mask = np.zeros(img.shape[:2], np.uint8)
    ## mask[300:375,250:350] = 225 # Use visual_feed.py to view this window
    mask[300:400,180:300] = 225 # Use visual_feed.py to view this window
    hist_norm_b = cv2.calcHist([b], [0], mask, [256], [0,256])
    hist_norm_g = cv2.calcHist([g], [0], mask, [256], [0,256])
    hist_norm_r = cv2.calcHist([r], [0], mask, [256], [0,256])
    if os.path.isfile('./CoHis/snapshot.jpeg') != True:
        print "Unable to locate snapshot.jpeg."
        return -1
    current = cv2.imread('./CoHis/snapshot.jpeg')
    b, g, r = cv2.split(current)
    hist_current_b = cv2.calcHist([b],[0],mask,[256],[0,256])
    hist_current_g = cv2.calcHist([g],[0],mask,[256],[0,256])
    hist_current_r = cv2.calcHist([r],[0],mask,[256],[0,256])
    max_norm_b = 0
    norm_loc_b = 0
    max_current_b = 0
    current_loc_b = 0
    max_norm_g = 0
    norm_loc_g = 0
    max_current_g = 0
    current_loc_g = 0
    max_norm_r = 0
    norm_loc_r = 0
    max_current_r = 0
    current_loc_r = 0

    for i in range(0,len(hist_norm_b)):
        if i > 5 and i < 200: 
           norm_loc_b = norm_loc_b + hist_norm_b[i] 
           norm_loc_g = norm_loc_g + hist_norm_g[i] 
           norm_loc_r = norm_loc_r + hist_norm_r[i] 
           
           current_loc_b = current_loc_b + hist_current_b[i] 
           current_loc_g = current_loc_g + hist_current_g[i] 
           current_loc_r = current_loc_r + hist_current_r[i]

    #Debug statements commented out
    #print norm_loc_b, norm_loc_g, norm_loc_r
    #print current_loc_b, current_loc_g, current_loc_r
    xb = abs(norm_loc_b - current_loc_b)
    xg = abs(norm_loc_g - current_loc_g)
    xr = abs(norm_loc_r - current_loc_r)
    print norm_loc_b, norm_loc_g, norm_loc_r, "-- ", current_loc_b, current_loc_g, current_loc_r 
    #print "#", xb, "#" , xg, "#", xr, "#"
    ## if xb > 20 or xg > 20 or xr > 20:    
    if xb > 10 or xg > 10 or xr > 10:
     return 0
    else:
     return 1

def compare_histo():
    print "I'm running - compare_histo"
    rospy.init_node('compare_histo')
    hisp = rospy.Service('compare_histo', CompareHisto, analyze_image)
    rospy.spin()

if __name__ == '__main__':
        compare_histo()
