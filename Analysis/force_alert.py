#! /usr/bin/env python
#
#     This node will collect the force messages from the force-torque sensor at the gripper the PR2,
#     calculate the magnitude of the force, and--using a statistical model based on previous trials
#     of the PR2 performing this task--publish an alert message to the 'emergency' topic if the magnitude
#     of force is two standard deviations above the mean. Otherwise, it will publish the magnitude
#     of the force.
#

from __future__ import division
import numpy as np
import rospy
import pylab
from collections import deque
from geometry_msgs.msg import WrenchStamped, Wrench
from std_msgs.msg import String
from matplotlib import pyplot as plt
from matplotlib import mlab
from scipy import stats
import math

hand='l'                   #which gripper is being tracked
mu=16.97                   #mean magnitude of force as calculated from previous trials in Newtons
sigma2=0.1
sigma=math.sqrt(sigma2)
dist= stats.norm(mu,sigma) #unit gaussian curve of amplitude of previous tests
stddev=2	           #number of standard deviations above mean to allow as threshhold




class force_analysis ():
    def __init__(self):
        rospy.init_node('FT_listener', anonymous=False)
        rospy.Subscriber("ft/%s_gripper_motor"%hand, WrenchStamped, self.callback)
        self.pub=rospy.Publisher('emergency', String)
        self.pub2=rospy.Publisher('Force_magnitude', String)
        self.r=rospy.Rate(10) #in hz
        self.fmag=deque([])
        self.force_x=deque([])
        self.force_y=deque([])
        self.force_z=deque([])

    def callback(self, msg):
        #grab force messages from force-torque sensor
        self.fx=msg.wrench.force.x
        self.fy=msg.wrench.force.y
        self.fz=msg.wrench.force.z
        self.calculate()

    def calculate (self):
        self.force_x.append(self.fx)
        self.force_y.append(self.fy)
        self.force_z.append(self.fz)
         
        #Calculate magnitude of the newest point and add to magnitude deque 
        self.fmag.append(math.sqrt(self.force_x[-1]**2+self.force_y[-1]**2+self.force_z[-1]**2))
        
               
        #Check magnitude   
        z=(np.array(self.fmag)-mu)/sigma
        
        #If anomaly detected publish stop message, otherwise publish magnitude            
        a=z>=stddev*sigma
        if a.any():    
            str1='STOP'                             
            self.pub.publish(str1)
        else:
            self.pub2.publish(str(self.fmag[-1]))       
               
     

if __name__=='__main__':
    callthis=force_analysis()
    callthis.__init__
    while not rospy.is_shutdown():
        rospy.spin()
    
