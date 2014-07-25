#! /usr/bin/env python
#
#    This node listens to the messages published by the PR2 force/torque sensor,
#    calculates the magnitude of the force, and compares it to a statistical model
#    of the magnitude of the force of previous trials of the PR2 completing the
#    yogurt feeding task. This node publishes the difference between the z-scored
#    magnitude of the force and the threshold number of standard deviations from 
#    the mean.
#

from __future__ import division
import numpy as np
import rospy
import pylab
from collections import deque
from geometry_msgs.msg import WrenchStamped, Wrench
from std_msgs.msg import Float64
from scipy import stats
import math

hand='l'                   #which gripper is being tracked
mus=np.array([11.1, 12.1, 15.78, 16.41, 16.29, 17.07, 16.83, 12.04, 9.52, 11.46, 12.67, 14.99]) #mean magnitude of force as calculated from previous trials in Newtons
sigma2=np.array([1.4, 3.59, 1.0, 0.11, 0.81, 1.49, 2.01, 4.82, 0.80, 1.27, 0.09, 5.18])                 #variances
sigmas=sigma2**0.5    #standard deviation
dist= stats.norm(mus[0],sigma) #unit gaussian distribution of magnitude of previous tests
stddev=0.4	               #number of standard deviations above mean to allow as threshhold


class force_analysis ():
    def __init__(self):
        rospy.init_node('FT_listener', anonymous=False)
        self.fmag=deque([])
        self.force_x=deque([])
        self.force_y=deque([])
        self.force_z=deque([])
        self.mu=mus[0]
        self.sigma=sigmas[0]
        self.pub1=rospy.Publisher('Force_result', Float64)
        rospy.Subscriber("ft/%s_gripper_motor"%hand, WrenchStamped, self.callback)
        rospy.Subscriber('Main_Control', String, self.listen)
        
        self.r=rospy.Rate(10) #in hz

    def callback(self, msg):          #grab messages from the force/torque sensor
        self.fx=msg.wrench.force.x
        self.fy=msg.wrench.force.y
        self.fz=msg.wrench.force.z
        self.calculate()

    def listen(self, msg):           #listen to which part of the task is being performed
        self.message=msg.data        
        if self.message[-2] is 't':
            self.part=self.message[-1]
        else:
            if self.message[-1] is '0': 
                self.part='10'
            elif self.message[-1] is '1':
                self.part='11' 					
        
        self.mu=mus[int(self.part)]        #change mean and standard deviation to those of the model for
        self.sigma=sigmas[int(self.part)]  #the subtask being performed
        self.calculate
        
    def calculate (self):
        self.force_x.append(self.fx)
        self.force_y.append(self.fy)
        self.force_z.append(self.fz)
         
        #Calculate magnitude of the newest point and add to magnitude deque 
        self.fmag.append(math.sqrt(self.force_x[-1]**2+self.force_y[-1]**2+self.force_z[-1]**2))
        
               
        #Calculate the z-score for the magnitude of the force  
        z=(np.array(self.fmag[-1])-self.mu)/self.sigma
        score=abs(z)-(stddev*self.sigma) #check the difference between z-score and set number of standard deviations
        self.pub1.publish(score) #pusblish this difference
               
     

if __name__=='__main__':
    callthis=force_analysis()
    while not rospy.is_shutdown():
        rospy.spin()
