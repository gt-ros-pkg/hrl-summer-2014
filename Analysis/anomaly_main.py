#!/usr/bin/env python

import rospy
import numpy as np
import os
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
        self.p_type = False
        self.sensitivity = 50 # Adjustable sensitivity. 0% -> 100%
        print "Anomaly Detection Node: Online"
        rospy.Subscriber('Force_Results', Float64, self.Force)
        rospy.Subscriber('Accel_Results', Float64, self.Accel)
        rospy.Subscriber('Torque_Results', Float64, self.Torque)
        rospy.Subscriber('Phase', Float64, self.Continue)
        rospy.Subscriber('Done', Float64, self.End)
	overwatch = rospy.Publisher('emergency', String)
        world_trigger = rospy.Publisher('begin', String)
        rospy.init_node('Anomaly_Control')
        world_trigger.publish("go")
        self.tp = 0
        self.fp = 0
        print "Message sent!"

        while (not rospy.is_shutdown()):
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
                    print "Anomaly Detected!"
		    #overwatch.publish("STOP")
                    if self.p_type == False:
                        self.fp = self.fp+1
                    else:
                        self.tp = self.tp+1
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

    def Continue(self,data):
        print "Entering Phase 2"
        self.p_type = True

    def End(self,data):
        print "We're done."
        print "True Positives  = ", self.tp
        print "False Positives = ", self.fp
        os._exit(0)

if __name__ == "__main__":
    ex = Investigator()
    ex.react()
