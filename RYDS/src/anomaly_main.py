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
import os
import sys
from std_msgs.msg import Float64, String

class Investigator:
    def react(self):
        self.response = 0
        self.force_response = 0
        self.torque_response = 0
        self.accel_response = 0
        self.sensitivity = 25 #16.50 # Adjustable sensitivity. 0% -> 300% (adjusted at 265 based on test data)
        print "Anomaly Detection Node: Online"
        rospy.Subscriber('Force_result', Float64, self.Force)
        rospy.Subscriber('Accel_result', Float64, self.Accel)
        rospy.Subscriber('Torque_result', Float64, self.Torque)
        overwatch = rospy.Publisher('emergency', String)
	puppy = rospy.Publisher('pups', Float64)
        rospy.init_node('Anomaly_Control')
        k = 0

        while (not rospy.is_shutdown()):
            satisfaction = 0
            # This is not a good way. It should be replaced!!! - daehyung
	    summer = self.torque_response + self.force_response + self.accel_response
            print "Total: ", summer," Torque: ", self.torque_response, " Force: ", self.force_response, " Acc: ", self.accel_response
	    puppy.publish(summer)
            if (summer > self.sensitivity):
		
                rospy.loginfo("Anomaly Possible!")
                k = k + 1
                if k > 5: # Require 20 hits in a row to trigger alarm
                    print "Anomaly Detected!"
                    overwatch.publish("STOP")
                    overwatch.publish("STOP")
                    overwatch.publish("STOP")
                    overwatch.publish("STOP")
                    overwatch.publish("STOP")
                    sys.exit()
            else:
                k = 0

                #print "All good!"
            rospy.sleep(0.05) # added buffer delay (may need to adjust)
    
    def Force(self,data):
        #print "Force result Recieved"
        self.force_response = data.data


    def Accel(self,data):
        #print "Accelerometer result Recieved"
        self.accel_response = data.data

    
    def Torque(self,data):
        #print "Torque result Recieved"
        self.torque_response = data.data


if __name__ == "__main__":
    ex = Investigator()
    ex.react()
