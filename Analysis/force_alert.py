#! /usr/bin/env python

from __future__ import division
import numpy as np
import rospy
import pylab
from collections import deque
from geometry_msgs.msg import WrenchStamped, Wrench
from matplotlib import pyplot as plt
from matplotlib import mlab
from scipy import stats
import math

hand='l'                   #which gripper is being tracked
stop=True 
mu=16.97                   #mean magnitude of force as calculated from previous trials in Newtons
sigma=1                    #standard deviation

dist= stats.norm(mu,sigma) #unit gaussian curve of amplitude of previous tests
stddev=2	           #number of standard deviations above mean to allow as threshhold


def callback(msg):
    rospy.loginfo(data.wrench.force.x, data.wrench.force.y, data.wrench.force.z
                  data.wrench.torque.x, data.wrench.torque.y, data.wrench.torque.z) 
def listener():
    rospy.init_node('FT_listener', anonymous=False)
    rospy.Subscriber("ft/%s_gripper_motor"%hand, WrenchStamped, callback)
    rospy.spin()

if __name__=='__main__':
    listener() 

force_x=deque([])
force_y=deque([])
force_z=deque([])
torque_x=deque([])
torque_y=deque([])
torque_z=deque([])

fmag=deque([])
tmag=deque([])


try:
    while stop:
            
        force_x.append(data.wrench.force.x)
        force_y.append(data.wrench.force.y)
        force_z.append(data.wrench.force.z)
        torque_x.append(data.wrench.torque.x)
        torque_y.append(data.wrench.torque.y)
        torque_z.append(data.wrench.torque.z)
        
        fx=np.array(force_x)
        fy=np.array(force_y)
        fz=np.array(force_z)
        
        tx=np.array(torque_x)
        ty=np.array(torque_y)
        tz=np.array(torque_z)
 
        #Calculate magnitude of the newest point and add to magnitude deque 
        fmag.append(math.sqrt(fx[-1]**2+fy[-1]**2+fz[-1]**2))
        tmag.append(math.sqrt(tx[-1]**2+ty[-1]**2+tz[-1]**2))
               
        #Check magnitude   
        z=(np.array(fmag)-mu)/sigma
                   
            
        #Publish message and Report anomalies 
    	    
        def force_analyzer(stop, z, stddev): 
            rospy.init_node('force_talker', anonymous=False)
            r=rospy.Rate(10) #in hz
            a=z>=stddev*sigma
            print(a.any())
            if a.any():
                stop=False
                pub=rospy.Publisher('emergency', String)
                str='STOP'                     
            else:
                pub=rospy.Publisher('Force_magnitude', String)
                str=str(fmag)
            
                pub.publish(str)
               
            try:
              while stop or not rospy.is_shutdown():
                    if a.any:
                        str='STOP'
                    else:
                        str="%s"%rospy.get_time()+'\n'+ sx + sy +sH 
                        
                    pub.publish(str)
                    rospy.sleep(0.1)
            except KeyboardInterrupt:
                return

        if __name__=='__main__':
            try:
               force_analyzer(stop, z, stddev)
            except rospy.ROSInterruptException: pass
               

except KeyboardInterrupt: 
    

