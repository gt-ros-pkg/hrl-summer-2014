#!/usr/bin/env python

# File: anomaly_main.py
# Caleb Little, GATech HRL summer project 2014, 7-25-14
# This file is used as an overhead coordinator for the 
# Guassian RV nodes of acceleration, force, and torque
# for TEAM RYDS robot feeding robot.

# Please use the following estimated target thresholds:
# Acceleration: 1.1
# Force: 0.4
# Torque: 2.5
# Master: 265

import rospy
import numpy as np
from std_msgs.msg import Float64, String

class Investigator:
    def react(self):
        self.response = 0
        self.force_response = 0
        self.torque_response = 0
        self.accel_response = 0
        self.sensitivity = 265 # Adjustable sensitivity. 0% -> 300% (adjusted at 265 based on test data)
        print "Anomaly Detection Node: Online"
        rospy.Subscriber('Force_Results', Float64, self.Force)
        rospy.Subscriber('Accel_Results', Float64, self.Accel)
        rospy.Subscriber('Torque_Results', Float64, self.Torque)
	overwatch = rospy.Publisher('emergency', String)
        rospy.init_node('Anomaly_Control')
        k = 0

        while (not rospy.is_shutdown()):
            satisfaction = 0
            if (self.torque_response + self.force_response + self.accel_response)*100 > self.sensitivity:
                satisfaction = 1
            if satisfaction == 1:
                print "Anomaly Possible!"
                k = k + 1
                if k > 20: # Require 20 hits in a row to trigger alarm
                    print "Anomaly Detected!"
                    overwatch.publish("STOP")
                    overwatch.publish("STOP")
                    overwatch.publish("STOP")
                    overwatch.publish("STOP")
                    overwatch.publish("STOP")
                else:
                    k = 0
            else:
                print "All good!"
            rospy.sleep(0.01) # added buffer delay (may need to adjust)
    
    def Force(self,data):
        print "Force result Recieved"
        self.force_response = data.data

    def Accel(self,data):
        print "Accelerometer result Recieved"
        self.accel_response = data.data
    
    def Torque(self,data):
        print "Torque result Recieved"
        self.torque_response = data.data

if __name__ == "__main__":
    ex = Investigator()
    ex.react()
