
#! /usr/bin/env python

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
sigma2=0.9
sigma=math.sqrt(sigma2)
dist= stats.norm(mu,sigma) #unit gaussian curve of amplitude of previous tests
stddev=2	           #number of standard deviations above mean to allow as threshhold




class force_analysis ():
    def __init__(self):
        rospy.init_node('FT_listener', anonymous=False)
        self.fmag=deque([])
        self.force_x=deque([])
        self.force_y=deque([])
        self.force_z=deque([])
        self.ignore=False
        self.pub=rospy.Publisher('emergency', String)
        self.pub2=rospy.Publisher('Force_magnitude', String)
        rospy.Subscriber("ft/%s_gripper_motor"%hand, WrenchStamped, self.callback)
        rospy.Subscriber('Main_Control', String, self.listen)
        
        self.r=rospy.Rate(10) #in hz

    def callback(self, msg):
        self.fx=msg.wrench.force.x
        self.fy=msg.wrench.force.y
        self.fz=msg.wrench.force.z
        self.calculate()

    def listen(self, msg):
        self.message=msg.data
        if "SwitchControllers" in self.message:
            self.ignore=True
        elif "FacePos1" in self.message: 
            self.ignore=False
        else:
            self.ignore=False
       
        
    def calculate (self):
        self.force_x.append(self.fx)
        self.force_y.append(self.fy)
        self.force_z.append(self.fz)
         
        #Calculate magnitude of the newest point and add to magnitude deque 
        self.fmag.append(math.sqrt(self.force_x[-1]**2+self.force_y[-1]**2+self.force_z[-1]**2))
        
               
        #Check magnitude   
        z=(np.array(self.fmag)-mu)/sigma
       
        a=z>=stddev*sigma
        if a.any() and not self.ignore:    
            str1='STOP'                             
            self.pub.publish(str1)
        else:
            self.pub2.publish(str(self.fmag[-1]))       
               
     

if __name__=='__main__':
    callthis=force_analysis()
    callthis.__init__
    while not rospy.is_shutdown():
        rospy.spin()
    
