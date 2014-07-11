#! /usr/bin/env python
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
sigma=1
dist= stats.norm(mu,sigma) #unit gaussian curve of amplitude of previous tests
stddev=2	           #number of standard deviations above mean to allow as threshhold




class accel_analysis ():
    def __init__(self):
        rospy.init_node('Accel_listener', anonymous=False)
        rospy.Subscriber("/accelerometer/%s_gripper_motor"%hand, AccelerometerState, self.callback)
        self.pub=rospy.Publisher('emergency', String)
        self.pub2=rospy.Publisher('Accel_magnitude', String)
        self.r=rospy.Rate(10) #in hz
        self.amag=deque([])
        self.accel_x=deque([])
        self.accel_y=deque([])
        self.accel_z=deque([])
 
    def callback(self, msg):
        #Collect messages from accelerometer
        x=[] 
        y=[]
        z=[]
        for i in range(len(msg.samples)):
            x.append(msg.samples[i].x)
            y.append(msg.samples[i].y)
            z.append(msg.samples[i].z)
        #Average samples together (usually 3 per message) 
        self.accel_x.append(np.average(x))
        self.accel_y.append(np.average(y))
        self.accel_z.append(np.average(z))
        self.worknstuff()
        
    def worknstuff (self):
        #Calculate magnitude of the newest point and add to magnitude deque 
        self.amag.append(math.sqrt(self.accel_x[-1]**2+self.accel_y[-1]**2+self.accel_z[-1]**2))
        
        
               
        #Check magnitude   
        z=(np.array(self.amag)-mu)/sigma
       
        a=z>=stddev*sigma
        #Publish alert message if there is an anomaly, otherwise publish magnitude
        if a.any():   
            str1='STOP'                             
            self.pub.publish(str1)
        else:
            self.pub2.publish(str(self.amag[-1]))       
            
if __name__=='__main__':
    callthis=accel_analysis()
    callthis.__init__
    while not rospy.is_shutdown():
        rospy.spin()
