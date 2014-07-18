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
        self.rat = rospy.Rate(1)
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
            self.broadcaster.sendTransform((0.1357099766643028, 0.6168739287720804, 0.3945569233565368)
 (0.6803912143821126, 0.3711032463950152, -0.49364023693606407, 0.3945497337274748),
                            rospy.Time.now(),"/GoalPos", "/torso_lift_link")
            print "Broadcast transform for Pos11":
        elif position == "Part1":
            self.broadcaster.sendTransform((-0.22733258597247905, 0.8052452563702237, 0.3605831344920665) (0.2120643017871668, 0.7381721245674608, -0.09206398818798957, 0.6337624700927027),
                            rospy.Time.now(),"/GoalPos", "/torso_lift_link")
            print "Broadcast transform for Pos1":
        elif position == "Part2":
            self.broadcaster.sendTransform((0.17190764723544932, 0.5874078141053017, 0.28744989752967687) (0.6922241308754694, -0.2890145635782358, -0.36900127996411564, 0.5487571321251573),
                            rospy.Time.now(),"/GoalPos", "/torso_lift_link")
            print "Broadcast transform for Pos2":
        elif position == "Part3":
            self.broadcaster.sendTransform((-0.011490289433490288, 0.6765155326014904, 0.3136745100403138) (0.7337599964260816, 0.0411276537095596, -0.17015905336034867, 0.6564683391487004),
                            rospy.Time.now(),"/GoalPos", "/torso_lift_link")
            print "Broadcast transform for Pos3":
        elif position == "Part4":
            self.broadcaster.sendTransform((-0.011074156386051028, 0.6756694571469335, 0.31330856636884313) (0.7341639298013855, 0.041293630505020724, -0.17145500527434818, 0.6556686216563015),
                            rospy.Time.now(),"/GoalPos", "/torso_lift_link")
            print "Broadcast transform for Pos4":
        elif position == "Part5":
            self.broadcaster.sendTransform((0.061150022127563625, 0.6319014085480716, 0.27215534907702665) (0.5792358712581784, 0.3023069412223096, -0.22229237314995706, 0.7236590492600438),
                            rospy.Time.now(),"/GoalPos", "/torso_lift_link")
            print "Broadcast transform for Pos5":
        elif position == "Part6":
            self.broadcaster.sendTransform((0.22485082374466764, 0.6325992236289548, 0.31714736509743996) (0.3996848386728747, 0.5403402850150602, -0.27228542770568254, 0.6885819137793376),
                            rospy.Time.now(),"/GoalPos", "/torso_lift_link")
            print "Broadcast transform for Pos6":
        elif position == "Part7":
            self.broadcaster.sendTransform((0.22152175550676378, 0.6270056137834308, 0.27390231686327643) (0.42387113240313345, 0.5189409206009242, -0.20230160497465494, 0.7142182052187057),
                            rospy.Time.now(),"/GoalPos", "/torso_lift_link")
            print "Broadcast transform for Pos7":
        elif position == "Part8":
            self.broadcaster.sendTransform((0.15875875967708222, 0.5465725037479428, 0.3139556031487017) (0.4763815865776585, 0.5202642655845353, -0.2046747498551779, 0.6785970267377077),
                            rospy.Time.now(),"/GoalPos", "/torso_lift_link")
            print "Broadcast transform for Pos8":
        elif position == "Part9":
            self.broadcaster.sendTransform((-0.22733258597247905, 0.8052452563702237, 0.3605831344920665) (0.2120643017871668, 0.7381721245674608, -0.09206398818798957, 0.6337624700927027),
                            rospy.Time.now(),"/GoalPos", "/torso_lift_link")
            print "Broadcast transform for Pos9":
        elif position == "Part10":
            self.broadcaster.sendTransform((0.1357099766643028, 0.6168739287720804, 0.3945569233565368) (0.6803912143821126, 0.3711032463950152, -0.49364023693606407, 0.3945497337274748),
                            rospy.Time.now(),"/GoalPos", "/torso_lift_link")
            print "Broadcast transform for Pos10":
        elif position == "Part11":
            self.broadcaster.sendTransform((0.6, -0.1, -0.1),(3, 14, 13, -1),
                            rospy.Time.now(),"/GoalPos", "/head_frame")
            print "Broadcast transform for Pos11":
        elif position =="Part12":
            self.broadcaster.sendTransform((0.26, -0.0, -0.0),(3, 14, 13, -1),
                            rospy.Time.now(),"/GoalPos", "/head_frame")
            print "Broadcast transform for Pos12"
        elif position =="Part13":
            self.broadcaster.sendTransform((0.53, -0.0, -0.08),(3, 14, 13, -1),
                            rospy.Time.now(),"/GoalPos", "/head_frame")
            print "Broadcast transform for Pos13"

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
        while (not rospy.is_shutdown() and self.stop != "STOP"):
            self.broadcast(position)
            try:
                (trans, rot) = self.listener.lookupTransform('/l_wrist_roll_link', '/GoalPos', rospy.Time(0))
                print trans, rot
                if (trans[1] < .09 and trans[2] < .09 and trans[0] < .09):
                    check = raw_input("(r)epeat printout of transform or (c)ontinue to next task?")
                    if check == 'c':
                        msg = position + "Done"
                        task_set.publish(msg)
                        break
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                print "tf lookup exception"
                continue
            self.rat.sleep()

if __name__ == '__main__':
    a = transformer()
    while not rospy.is_shutdown():
        rospy.spin()




       
