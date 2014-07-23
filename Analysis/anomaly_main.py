#!/usr/bin/env python

import rospy
import numpy as np
from std_msgs.msg import Float64, String

class Investigator:
    def react(self):
        self.response = 0
        self.force_response = 0
        self.force_check = True
        self.torque_response = 0
        self.torque_check = True
        self.accel_response = 0
        self.accel_check = True
        self.sensitivity = 50 # Adjustable sensitivity. 0% -> 100%
        print "Anomaly Detection Node: Online"
        rospy.Subscriber('Force_Results', Float64, self.Force)
        rospy.Subscriber('Accel_Results', Float64, self.Accel)
        rospy.Subscriber('Torque_Results', Float64, self.Torque)
	overwatch = rospy.Publisher('emergency', String)
        rospy.init_node('Anomaly_Control')
        k = 0

        while (not rospy.is_shutdown()) :
            satisfaction = 0
            if self.response > 2:
                self.response = self.response - 3
                satisfaction = 0
                print "Making Decision"
                if (self.torque_response + self.force_response + self.accel_response)*100 > self.sensitivity:
                    satisfaction = 1

                self.torque_check = True
                self.force_check = True
                self.accel_check = True
                if satisfaction == 1:
                    print "Anomaly Possible!"
                    k = k + 1
                    if k > 10: # Require 10 hits in a row to trigger alarm
                        print "Anomaly Detected!"
                        overwatch.publish("STOP")
                    else:
                        k = 0
                else:
                    print "All good!"
    
    def Force(self,data):
        if self.force_check == True:
            print "Force result Recieved"
            self.response = self.response + 1
            self.force_response = data.data
            self.force_check = False

    def Accel(self,data):
        if self.accel_check == True:
            print "Accelerometer result Recieved"
            self.response = self.response + 1
            self.accel_response = data.data
            self.force_check = False
    
    def Torque(self,data):
        if self.torque_check == True:
            print "Torque result Recieved"
            self.response = self.response + 1
            self.torque_response = data.data
            self.torque_check = False

if __name__ == "__main__":
    ex = Investigator()
    ex.react()
