#! /usr/bin/env python
#
#    This node listens to the messages published by the PR2 accelerometer,
#    calculates the magnitude of acceleration, and compares it to a statistical model
#    of the magnitude of the acceleration of previous trials of teh PR2 completing the
#    yogurt feeding task. If the magnitude is greater than 2 standard deviations from 
#    the mean, this node publishes an alert message to the 'emergency' topic. Otherwise
#    it publishes the magnitude of the acceleration.
#

from __future__ import division
import roslib; roslib.load_manifest('pr2_msgs')
import numpy as np
import rospy
import pylab
from collections import deque
from geometry_msgs.msg import Vector3
from pr2_msgs.msg import AccelerometerState 
from std_msgs.msg import String
from matplotlib import pyplot as plt
from matplotlib import mlab
from scipy import stats
import math

hand='l'                   #which gripper is being tracked
mu=9.66                   #mean magnitude of force as calculated from previous trials in Newtons
sigma2=1.75
sigma=math.sqrt(sigma2)
dist= stats.norm(mu,sigma) #unit gaussian curve of amplitude of previous tests
stddev=2	           #number of standard deviations above mean to allow as threshhold




class accel_analysis ():
    def __init__(self):
        rospy.init_node('Accel_listener', anonymous=False)
        self.amag=deque([])
        self.accel_x=deque([])
        self.accel_y=deque([])
        self.accel_z=deque([])
        self.ignore=False
        self.pub=rospy.Publisher('emergency', String)
        self.pub2=rospy.Publisher('Accel_magnitude', String)
        rospy.Subscriber("/accelerometer/%s_gripper_motor"%hand, AccelerometerState, self.callback)
        rospy.Subscriber('Main_Control', String, self.listen)
        
        self.r=rospy.Rate(10) #in hz
        
 
    def callback(self, msg):
        x=[] 
        y=[]
        z=[]
        for i in range(len(msg.samples)):
            x.append(msg.samples[i].x)
            y.append(msg.samples[i].y)
            z.append(msg.samples[i].z)
        
        self.accel_x.append(np.average(x))
        self.accel_y.append(np.average(y))
        self.accel_z.append(np.average(z))
        self.worknstuff()
    
    def listen(self, msg):
        self.message=msg.data
        if "SwitchControllers" in self.message:
            self.ignore=True
        elif "FacePos1" in self.message: 
            self.ignore=False
        else:
            self.ignore=False
                   
            
    def worknstuff (self):
        #Calculate magnitude of the newest point and add to magnitude deque 
        self.amag.append(math.sqrt(self.accel_x[-1]**2+self.accel_y[-1]**2+self.accel_z[-1]**2))
        
        
               
        #Check magnitude   
        z=(np.array(self.amag)-mu)/sigma
       
        a=z>=stddev*sigma
        
        if a.any() and not self.ignore:   
            str1='STOP'                             
            self.pub.publish(str1)
        else:
            self.pub2.publish(str(self.amag[-1]))       
            
if __name__=='__main__':
    callthis=accel_analysis()
    callthis.__init__
    while not rospy.is_shutdown():
        rospy.spin()
