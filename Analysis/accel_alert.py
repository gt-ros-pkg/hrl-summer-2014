#! /usr/bin/env python

from __future__ import division
import numpy as np
import rospy
import pylab
from collections import deque
from geometry_msgs.msg import Vector3Stamped, Vector3
from matplotlib import pyplot as plt
from matplotlib import mlab
from scipy import stats
import math

hand='l'		   #which gripper is being tracked
stop=True 
mu=9.66			   #mean magnitude of accelteration as calculated from previous trials in Nm
sigma2=1		   #variance		
sigma=math.sqrt(sigma2)  #standard deviation
dist= stats.norm(mu,sigma) #unit gaussian curve of amplitude of previous tests
stddevs=2	           #number of standard deviations above mean to allow as threshhold


def callback(msg):
    rospy.loginfo(data.vector3.x, data.vector3.y, data.vector3.z) 
def listener():
    rospy.init_node('Accel_listener', anonymous=False)
    rospy.Subscriber("/accelerometer/%s_gripper_motor"%hand, Vector3Stamped, callback)
    rospy.spin()

if __name__=='__main__':
    listener() 

accel_x=deque([])
accel_y=deque([])
accel_z=deque([])

amag=deque([])

try:
    while stop:
            
        accel_x.append(data.vector3.x)
        accel_y.append(data.vector3.y)
        accel_z.append(data.vector3.z)
       
        
        ax=np.array(accel_x)
        ay=np.array(accel_y)
        az=np.array(accel_z)
      
 
        #Calculate magnitude of the newest point and add to magnitude deque 
        amag.append(math.sqrt(ax[-1]**2+ay[-1]**2+az[-1]**2))
        
               
        #Check magnitude   
        z=(np.array(amag)-mu)/sigma
                   
            
        #Publish message and Report anomalies 
    	    
        def accel_analyzer(stop, z, stddev): 
            rospy.init_node('accel_talker', anonymous=False)
            r=rospy.Rate(10) #in hz
            a=z>=stddevs*sigma
            if a.any():
                stop=False
                pub=rospy.Publisher('emergency', String)
                str='STOP'                     
            if not a.any():
                pub=rospy.Publisher('Accel_magnitude', String)
                str=str(amag)
            
            pub.publish(str)
               
            try:
              while stop or not rospy.is_shutdown():
                  a=z>=stddevs*sigma
                  if a.any():
                      pub=rospy.Publisher('emergency', String)
                      str='STOP'
                  if not a.any():
                      pub=rospy.Publisher('Accel_magnitude', String)
                      str="%s"%rospy.get_time()+'\n'+ sx + sy +sH 
                        
                  pub.publish(str)
                  rospy.sleep(0.1)
            except KeyboardInterrupt:
                rospy.shutdown()

        if __name__=='__main__':
            try:
               accel_analyzer(stop, z, stddev)
            except rospy.ROSInterruptException: pass
               

except KeyboardInterrupt: 
    

