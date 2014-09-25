#! /usr/bin/env python
#
#    This node listens to messages published by the force-torque sensor of the PR2, calculates
#    the magnitude of the torque, and--using a statistical model based on previous trials of the
#    PR2 performing this task--publishes an alert message to the 'emergency' topic if the magnitude
#    is greater than two standard deviations above the mean. Otherwise it publishes the magnitude
#    of the torque. 
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
mu=0.54                   #mean magnitude of force as calculated from previous trials in Newtons
sigma2=0.023
sigma=math.sqrt(sigma2)
dist= stats.norm(mu,sigma) #unit gaussian curve of amplitude of previous tests
stddev=2	           #number of standard deviations above mean to allow as threshhold




class torque_analysis ():
    def __init__(self):
        rospy.init_node('Torque_listener', anonymous=False)
        rospy.Subscriber("ft/%s_gripper_motor"%hand, WrenchStamped, self.callback)
        self.pub=rospy.Publisher('emergency', String)
        self.pub2=rospy.Publisher('Torque_magnitude', String)
        self.r=rospy.Rate(10) #in hz
        self.tmag=deque([])
        self.torque_x=deque([])
        self.torque_y=deque([])
        self.torque_z=deque([])

    def callback(self, msg):
        #grab torque from force-torque sensor messages
        self.tx=msg.wrench.torque.x
        self.ty=msg.wrench.torque.y
        self.tz=msg.wrench.torque.z
        self.calculate()

    def calculate (self):
        self.torque_x.append(self.tx)
        self.torque_y.append(self.ty)
        self.torque_z.append(self.tz)
         
        #Calculate magnitude of the newest point and add to magnitude deque 
        self.tmag.append(math.sqrt(self.torque_x[-1]**2+self.torque_y[-1]**2+self.torque_z[-1]**2))
        
               
        #Check magnitude   
        z=(np.array(self.tmag)-mu)/sigma

        #If anomaly detected, publish alert message, otherwise publish magnitude        
        a=z>=stddev*sigma
        if a.any():    
            str1='STOP'                             
            self.pub.publish(str1)
        else:
            self.pub2.publish(str(self.tmag[-1]))       
               
     

if __name__=='__main__':
    callthis=torque_analysis()
    callthis.__init__
    while not rospy.is_shutdown():
        rospy.spin()
    
