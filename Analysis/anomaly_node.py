#!/usr/bin/env python

import rospy
import numpy as np
from std_msgs.msg import Float64

class Investigator:
    def react(self):
        rospy.init_node('Anomaly_Control')
        self.response = 0
        self.ft_response = 0
        self.accel_response = 0
        self.audio_response = 0
        self.current_state = -1
        self.sensitivity = 50 # Adjustable sensitivity. 0% -> 100%
        print "Anomaly Detection Node: Online"
        rospy.Subscriber("FT_Results", Float64, self.FT)
        rospy.Subscriber("Accel_Results", Float64, self.Accel)
        rospy.Subscriber("Audio_Results", Float64, self.Audio)
        rospy.Subscriber("Current_State", Float64, self.Status)
	overwatch = rospy.Publisher("Anomaly_Topic", Float64)

        while (1 == 1) :
            satisfaction = 0
            if self.response > 2:
                self.response = self.response - 3
                print "Making Decision"
                if self.current_state == 0:
                    print "Currently in state 0: Insert Description Here"
                    satisfaction = 50*self.audio_response + 25*self.ft_response + 25*accel_response
                elif self.current_state == 1:
                    print "Currently in state 1: Insert Description Here"
                    satisfaction = 25*self.audio_response + 50*self.ft_response + 25*accel_response
                elif self.current_state == 2:
                    print "Currently in state 2: Insert Description Here"
                    satisfaction = 25*self.audio_response + 25*self.ft_response + 50*accel_response
                elif self.current_state == 3:
                    print "Currently in state 3: Insert Description Here"
                    satisfaction = 10*self.audio_response + 10*self.ft_response + 80*accel_response
                elif self.current_state == 4:
                    print "Currently in state 4: Insert Description Here"
                    satisfaction = 10*self.audio_response + 80*self.ft_response + 10*accel_response
                elif self.current_state == 5:
                    print "Currently in state 5: Insert Description Here"
                    satisfaction = 80*self.audio_response + 10*self.ft_response + 10*accel_response
                elif self.current_state == 6:
                    print "Currently in state 6: Insert Description Here"
                    satisfaction = 60*self.audio_response + 20*self.ft_response + 20*accel_response
                elif self.current_state == 7:
                    print "Currently in state 7: Insert Description Here"
                    satisfaction = 20*self.audio_response + 60*self.ft_response + 20*accel_response
                elif self.current_state == 8:
                    print "Currently in state 8: Insert Description Here"
                    satisfaction = 20*self.audio_response + 20*self.ft_response + 60*accel_response
                elif self.current_state == 9:
                    print "Currently in state 9: Insert Description Here"
                    satisfaction = 30*self.audio_response + 40*self.ft_response + 30*accel_response
            
                print "Decision Made (I AM THE LAW)"
                if 100-self.sensitivity > satisfaction:
                    print "Anonmaly Detected!"
		    overwatch.publish(1)
                else:
                    print "All good!"
		    overwatch.publish(0)
        rospy.spin()
    
    def FT(self,data):
        print "Force result Recieved"
        self.response = self.response + 1
        self.ft_response = data.data # need to set this up?

    def Accel(self,data):
        print "Accelerometer result Recieved"
        self.response = self.response + 1
        self.accel_response = data.data
    
    def Audio(self,data):
        print "Audio result Recieved"
        self.response = self.response + 1
        self.audio_response = data.data
        
    def Status(self,data):
        print "New State entered!"
        self.current_state = data.data

if __name__ == "__main__":
    ex = Investigator()
    ex.react()
