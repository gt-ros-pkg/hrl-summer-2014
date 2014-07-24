#! /usr/bin/env python
#
#    This node listens to the messages published by the PR2 torque/torque sensor,
#    calculates the magnitude of the torque, and compares it to a statistical model
#    of the magnitude of the torque of previous trials of the PR2 completing the
#    yogurt feeding task. The node publishes the difference between the z-scored
#    magnitude of torque and threshold number of standard deviations from the mean.
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
mus=np.array([1.53, 1.58, 1.6, 1.08, 1.23, 1.09, 1.54, 1.58, 1.5, 1.56, 1.66, 1.59]) #mean magnitude of torque as calculated from previous trials in Newtons
sigma2=np.array([0.009, 0.003, 0.002, 0.038, 0.021, 0.0056, 0.026, 0.0041, 0.0021, 0.0069, 0.0035, 0.0018])                  #variance
sigmas=sigma2**0.5              #standard deviation
dist= stats.norm(mus[0],sigma) #unit gaussian distribution of magnitude of previous tests
stddev=1	               #number of standard deviations above mean to allow as threshhold


class torque_analysis ():
    def __init__(self):
        rospy.init_node('FT_listener', anonymous=False)
        self.tmag=deque([])
        self.torque_x=deque([])
        self.torque_y=deque([])
        self.torque_z=deque([])
        self.mu=mus[0]
        self.sigma=sigmas[0]
        self.pub1=rospy.Publisher('Torque_result', Float64)
        rospy.Subscriber("ft/%s_gripper_motor"%hand, WrenchStamped, self.callback)
        rospy.Subscriber('Main_Control', String, self.listen)
        
        self.r=rospy.Rate(10) #in hz

    def callback(self, msg):          #grab messages from the torque/torque sensor
        self.tx=msg.wrench.torque.x
        self.ty=msg.wrench.torque.y
        self.tz=msg.wrench.torque.z
        self.calculate()

    def listen(self, msg):           #listen to what part of the task is being performed
        self.message=msg.data        
        if self.message[-2] is 't':
            self.part=self.message[-1]
        else:
            if self.message[-1] is '0': 
                self.part='10'
            elif self.message[-1] is '1':
                self.part='11' 					
        
        self.mu=mus[int(self.part)]        #change mean and standard deviation to match model for subtask
        self.sigma=sigmas[int(self.part)]  #being performed
        self.calculate
        
    def calculate (self):
        self.torque_x.append(self.tx)
        self.torque_y.append(self.ty)
        self.torque_z.append(self.tz)
         
        #Calculate magnitude of the newest point and add to magnitude deque 
        self.tmag.append(math.sqrt(self.torque_x[-1]**2+self.torque_y[-1]**2+self.torque_z[-1]**2))
               
        #Calculate z-score   
        z=(np.array(self.tmag[-1])-self.mu)/self.sigma   
        score=abs(z)-(stddev*self.sigma) #find difference between z-score and threshold standard deviation
        self.pub1.publish(score) #pusblish this difference
               
     

if __name__=='__main__':
    callthis=torque_analysis()
    while not rospy.is_shutdown():
        rospy.spin()
