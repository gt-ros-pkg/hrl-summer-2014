#! /usr/bin/env python
#
#    This node listens to the messages published by the PR2 accelerometer,
#    calculates the magnitude of acceleration, and compares it to a statistical model
#    of the magnitude of the acceleration of previous trials of the PR2 completing the
#    yogurt feeding task. This node publishes the difference between the z-scored magnitude
#    of the acceleration and threshold value of standard deviations from the mean.
#

from __future__ import division
import roslib; roslib.load_manifest('pr2_msgs')
import numpy as np
import rospy
import pylab
from collections import deque
from geometry_msgs.msg import Vector3
from pr2_msgs.msg import AccelerometerState 
from std_msgs.msg import Float64
from scipy import stats
import math

hand='l'                   #which gripper is being tracked
mus=np.array([9.85, 9.7, 9.16, 8.99, 8.97, 8.98, 9.05, 9.72, 10.13, 9.85, 9.66, 9.34]) 
#mean magnitudes of acceleration for each part of the task 
                                                 #as calculated from previous trials in Newtons
sigma2=np.array([0.052, 0.11, 0.039, 0.021, 0.021, 0.030, 0.058, 0.14, 0.040, 0.054, 0.022, 0.14])                     #variances
sigmas=sigma2**0.5        #standard deviation                       
stddev=1	               #number of standard deviations above mean to allow as threshhold




class accel_analysis ():
    def __init__(self):
        rospy.init_node('Accel_listener', anonymous=False)
        self.amag=deque([])
        self.accel_x=deque([])
        self.accel_y=deque([])
        self.accel_z=deque([])
        self.mu=mus[0]
        self.sigma=sigmas[0]
        self.dist= stats.norm(mus[0],sigma) #unit gaussian distribution of magnitude of acceleration of previous tests
        self.pub1=rospy.Publisher('Accel_result', Float64)
        rospy.Subscriber("/accelerometer/%s_gripper_motor"%hand, AccelerometerState, self.callback)
        rospy.Subscriber('Main_Control', String, self.listen)
        
        self.r=rospy.Rate(10) #in hz
        
 
    def callback(self, msg):
        x=[] 
        y=[]
        z=[]
        for i in range(len(msg.samples)):   #grab messages from accelerometer (usually publishes 3 samples per 
            x.append(msg.samples[i].x)      #ROS message)
            y.append(msg.samples[i].y)
            z.append(msg.samples[i].z)
        
        self.accel_x.append(np.average(x))  #average the samples from the message 
        self.accel_y.append(np.average(y))
        self.accel_z.append(np.average(z))
        self.worknstuff()
    
    def listen(self, msg):
        self.message=msg.data                     
        if self.message[-2] is 't':            #listen for which part of the task if being performed
            self.part=self.message[-1]
        else:
            if self.message[-1] is '0':                        
                self.part='10'
            elif self.message[-1] is '1':
                self.part='11' 					
        
        self.mu=mus[int(self.part)]         #grab the correct mean and standard deviation for the model of 
        self.sigma=sigmas[int(self.part)]   #subtask that is currently being performed
        self.worknstuff()           
            
    def worknstuff (self):
        #Calculate magnitude of the newest point and add to magnitude deque 
        self.amag.append(math.sqrt(self.accel_x[-1]**2+self.accel_y[-1]**2+self.accel_z[-1]**2)
               
        #Calculate the z-score of the magnitude   
        z=(np.array(self.amag[-1])-self.mu)/self.sigma
        score=abs(z)-(stddev*self.sigma) #find difference between z-score and threshold number of standard deviations
                
        self.pub1.publish(score)   #publish this difference
            
if __name__=='__main__':
    callthis=accel_analysis()
    while not rospy.is_shutdown():
        rospy.spin()
