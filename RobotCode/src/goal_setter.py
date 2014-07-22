#!/usr/bin/env python  

#Chris Birmingham, HRL, 7/16/14
#This file takes predetermined tf transforms(relative to either the subjects
#head for feeding positions or the robots base for the bowl location)
#and broadcasts that transform. It then looks up the transform and converts
#it to a posed stamped message that the haptic mpc can use as a goal location.
#It acts upon recieving messages from the Main_Control and emergency topics.
#If STOP is recieved from the emergency topic it will dissable the Haptic mpc
#and exit.


import roslib
roslib.load_manifest('RobotCode')
roslib.load_manifest('hrl_haptic_mpc')
import rospy
import math
import time
import numpy as np
import tf
import std_msgs.msg
import sys
import os
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
from hrl_haptic_manipulation_in_clutter_srvs.srv import *
import geometry_msgs.msg
import tf_conversions.posemath as pm



class transformer():
    def __init__(self):
        rospy.init_node('goal_setter')
        rospy.Subscriber('Main_Control', String, self.run)
        rospy.Subscriber('emergency', String, self.e_check)
        self.haptic = rospy.ServiceProxy('haptic_mpc/enable_mpc', EnableHapticMPC)
        self.broadcaster = tf.TransformBroadcaster()
        self.listener = tf.TransformListener()
        self.pose_pub = rospy.Publisher('haptic_mpc/goal_pose', PoseStamped)
        self.rat = rospy.Rate(.5)
        self.stop = ""
        self.i = 0

    #Called if msg sent to emergency topic
    def e_check(self, data):
        self.stop = data.data
        if self.stop != "STOP":
            return
        self.haptic('False')
        print "Stopped haptic control!"
        os._exit(0)


    #Broadcasts a set transform as the desired position based on task section
    #In Rviz, note translation is: (red,green,blue)
    #                      quaternian is: (red,green,blue,rotation)
    def broadcast(self, position):
        if position == "Part0":
            self.broadcaster.sendTransform((0.5309877259429142, 0.4976163448816489, 0.16719537682372823),(0.7765742993649133, -0.37100605554316285, -0.27784851903166524, 0.42671660945891),
                            rospy.Time.now(),"/GoalPos", "/torso_lift_link")
            print "Broadcast transform for Pos0"
        elif position == "Part1":
            self.broadcaster.sendTransform((0.516341299985487, 0.8915608293219441, 0.1950343868326016),(0.6567058177198967, 0.16434420640210323, 0.0942917725129517, 0.7299571990406495),
                            rospy.Time.now(),"/GoalPos", "/torso_lift_link")
            print "Broadcast transform for Pos1"
        elif position == "Part2":
            self.broadcaster.sendTransform((0.5193456827844327, 0.900079836777675, -0.019204479089017762),(0.4954470843513707, 0.5023693425664104, -0.12672521702586453, 0.6972072501250012),
                            rospy.Time.now(),"/GoalPos", "/torso_lift_link")
            print "Broadcast transform for Pos2"
        elif position == "Part3":
            self.broadcaster.sendTransform((0.5098543997629579, 0.8806008953235813, -0.0974591835731535),(0.45253993336907683, 0.533997128372586, -0.17283744712356874, 0.6929515801756649),
                            rospy.Time.now(),"/GoalPos", "/torso_lift_link")
            print "Broadcast transform for Pos3"
        elif position == "Part4":
            self.broadcaster.sendTransform((0.5418855469129493, 0.9140635229546514, -0.10433053967271771),(0.4903488201115364, 0.49639824283005096, -0.1400581861447639, 0.7025172763884889),
                            rospy.Time.now(),"/GoalPos", "/torso_lift_link")
            print "Broadcast transform for Pos4"
        elif position == "Part5":
            self.broadcaster.sendTransform((0.5097778641738854, 0.8811538278444637, -0.07757980710747647),(0.3515887722286045, 0.6131005055762095, -0.07870017707244904, 0.7030642839980877),
                            rospy.Time.now(),"/GoalPos", "/torso_lift_link")
            print "Broadcast transform for Pos5"
        elif position == "Part6":
            self.broadcaster.sendTransform((0.516341299985487, 0.8915608293219441, 0.1950343868326016),(0.6567058177198967, 0.16434420640210323, 0.0942917725129517, 0.7299571990406495),
                            rospy.Time.now(),"/GoalPos", "/torso_lift_link")
            print "Broadcast transform for Pos6"
        elif position == "Part7":
            self.broadcaster.sendTransform((0.5309877259429142, 0.4976163448816489, 0.16719537682372823),(0.7765742993649133, -0.37100605554316285, -0.27784851903166524, 0.42671660945891),
                            rospy.Time.now(),"/GoalPos", "/torso_lift_link")
            print "Broadcast transform for Pos7"
        elif position == "Part8":
            self.broadcaster.sendTransform((0.2741387011303321, 0.05522571699560719, -0.011919598309888757),(-0.023580897114171894, 0.7483633417869068, 0.662774596931439, 0.011228696415565394),
                            rospy.Time.now(),"/GoalPos", "/head_frame")
            print "Broadcast transform for Pos8"
        elif position == "Part9":
            self.broadcaster.sendTransform((0.12608632401364894, 0.03540318703608347, 0.00607600258150498),(-0.015224467044577382, 0.7345761465214938, 0.6783020152473445, -0.008513323454022942),
                            rospy.Time.now(),"/GoalPos", "/head_frame")
            print "Broadcast transform for Pos9"
        elif position == "Part10":
            self.broadcaster.sendTransform((0.1526437596817016, 0.03715712909254376, 0.0136172136416570133),(-0.050599231123428158, 0.7586479615613725, 0.6342031296736002, 0.0013829359935748063),
                            rospy.Time.now(),"/GoalPos", "/head_frame")
            print "Broadcast transform for Pos10"
        elif position == "Part11":
            self.broadcaster.sendTransform((0.5309877259429142, 0.4976163448816489, 0.16719537682372823),(0.7765742993649133, -0.37100605554316285, -0.27784851903166524, 0.42671660945891),
                            rospy.Time.now(),"/GoalPos", "/torso_lift_link")
            print "Broadcast transform for Pos11"



    #Based on previously broadcast position, sends posed stamped msg to haptic mpc
    #Returns false if could not find the FeedPos frame, true if goal was successfully
    #   published to hmpc
    def send_to_hmpc(self, position):
        published = False
        try:
            (trans, rot) = self.listener.lookupTransform('/torso_lift_link', '/GoalPos', rospy.Time(0))
            hdr = std_msgs.msg.Header()
            hdr.frame_id = '/torso_lift_link'
            hdr.stamp = rospy.Time.now()
            hdr.seq = self.i
            transa = geometry_msgs.msg.Point()
            transa.x = trans[0]
            transa.y = trans[1]
            transa.z = trans[2]
            rota = geometry_msgs.msg.Quaternion()
            rota.x = rot[0]
            rota.y = rot[1]
            rota.z = rot[2]
            rota.w = rot[3]          
            pose_msg = PoseStamped(header = hdr, pose = Pose(transa, rota))
            self.pose_pub.publish(pose_msg)
            published = True
            print "goal pose published to hmpc"
            self.i = self.i+1

        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            print "tf Exception, please broadcast FeedPos transform again"
        return published




    def run(self, data):
        #Initialization upon callback
        position = data.data
        
        if position[0] != "P":
            print ("Converter heard: %s, will keep listening." % position)
            return
        else:
            print ("Converter heard: %s, Starting." % position)

        task_set = rospy.Publisher('task_check', String)
        task_set.publish("Converter starting: %s" % position)

        #Broadcast the transform of the position for the first time
        self.broadcast(position)

        #Send desired pose to hmpc, returns true when pose has been sent
        published = False
        while (not rospy.is_shutdown() and published == False):
            published = self.send_to_hmpc(position)
            self.rat.sleep()

        #check if close enough to goal pose, ask for for feedback
        #when close enough, broadcast current location as goal pose, send to hmpc 
        #and tell main program it is done moving
        timeout = 0
        while (not rospy.is_shutdown() and self.stop != "STOP"):
            self.broadcast(position)
            try:
                (trans, rot) = self.listener.lookupTransform('/l_gripper_spoon_frame', '/GoalPos', rospy.Time(0))
                print trans, rot
                if (trans[1] < .03 and trans[2] < .03 and trans[0] < .03 and rot[0] < .3 and rot[1] < .3 and rot[2] < .3):
                    #check = raw_input("(r)epeat printout of transform or (c)ontinue to next task?")
                    #if check == 'c':
                    #rospy.sleep(3)
                    msg = position + "Done"
                    task_set.publish(msg)
                    print "done"
                    break
                self.send_to_hmpc(position)
                timeout = timeout +1
                if timeout == 8:
                    msg = position + "Done"
                    task_set.publish(msg)
                    print "done"
                    break
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                print "tf lookup exception"
                continue
            self.rat.sleep()

if __name__ == '__main__':
    a = transformer()
    while not rospy.is_shutdown():
        rospy.spin()




       
