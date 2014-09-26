#!/usr/bin/env python 
#
# Megan Rich, HRL, 8/25/14
# This node checks if the tf frame '/head_frame' obtained from 
# head registration is currently within reach of the PR2. If the
# head frame is not within reach of the PR2, it will move the PR2 base
# to within range of the subject's head. 

import roslib
roslib.load_manifest('tf')
roslib.load_manifest('actionlib')
roslib.load_manifest('move_base')
import actionlib
#from actionlib_msgs.msg import MoveBaseAction
from move_base_msgs.msg import MoveBaseAction, MoveBaseActionGoal
import rospy
import math
import tf
from geometry_msgs.msg import Twist, PointStamped, Pose, Quaternion, PoseStamped
from std_msgs.msg import String
import os

class check_head():

    def __init__(self):
        rospy.init_node('check_head')
        self.listener = tf.TransformListener()
        self.pub=rospy.Publisher('head_check', String)
        self.head=rospy.Publisher('head_check_confirm', String)
        self.move=rospy.Publisher('base_controller/command', Twist)
        rospy.Subscriber('head_check', String, self.head_check)
        rospy.sleep(1)
        self.cmd=Twist()
        self.l=0
        self.r=0
        self.t=0
        self.trans14=(0.13928415716177617, 0.6565833449408256, -1.357303916796)
        self.rot14=(0.2789777273842869, -0.05907426262263365, 0.8767308579569227, -0.3873301715916394)
        self.transh=(0.13895118715509372, 0.6563869581415823, -1.3570648116919164)
        self.roth=(0.2675468812908289, -0.052590910844725884, 0.8789907250153403, -0.39118814877892155)
        #precalculated values of the maximum length of both arms (form /(l or r)_shoulder_pan_link
        #to the the appropriate tool frame
        #assumes spoon tool is in left gripper
        self.l_arm_length=1.36
        self.r_arm_length=0.94
        #check if left and right arms are within reach of the registered head
        self.calc_left()
        self.calc_right() 
    
    #check if head check is complete
    def head_check(self, data):
        self.mess=data.data
        if self.mess == 'Ready':
            self.t=self.t+1
            if self.t==2:
                self.head.publish('Ready')
                print('Head check complete')
                os._exit(0)

    def calc_left (self):
     
        try:
            #look up transforms of /l_shoulder_pan_link and /head_frame 
            #with respect to same coordinate frame (/odom_combined)                                                	
            (trans1, rot1)=self.listener.lookupTransform('/l_shoulder_pan_link', '/odom_combined', rospy.Time(0))
            #(trans14, rot14)=self.listener.lookupTransform('/head_frame', '/odom_combined', rospy.Time(0)) 
            #calculate the distance between them (distance to head)
            self.l_dist2head=math.sqrt((self.trans14[0]-trans1[0])**2+(self.trans14[1]-trans1[1])**2+(self.trans14[2]-trans1[2])**2)
            print('Left distance: %s'%self.l_dist2head)
           
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException): #check for tf exceptions 
            print ('Error! Most likely cause: tf lookup Exception')
            self.l_dist2head=1.
        
        #check if the head is within reach    
        if self.l_dist2head >(self.l_arm_length):
            print('Head not reachable!')
            print('Left arm too short')
            #send message to master control, so it will not start yet
            self.pub.publish('Too far')
            #move base to be within reach of left arm
            self.base_mover('l')
        elif self.l_dist2head==1.:
            #if there was a tf exception try again 3 times before quitting
            print('calculation failed')
            self.l=self.l+1
            if self.l<=3:
                print('trying again')
                self.calc_left() 
            else:
                print('exiting')
                os._exit(0)           
        else:
            #if head within reach of left arm, publish a message to the master control node
            #this message allows it to begin
            print('Head within reach')
            self.pub.publish('Ready')
    def calc_right(self):
        try:  
            #look up transforms of /r_shoulder_pan_link and /head_frame 
            #with respect to same coordinate frame (/odom_combined)       
            (trans1, rot1)=self.listener.lookupTransform('/r_shoulder_pan_link', '/odom_combined', rospy.Time(0))
            #(trans14, rot14)=self.listener.lookupTransform('/head_frame', '/odom_combined', rospy.Time(0))
            #calculate the distance between them (distance to head)
            self.r_dist2head=math.sqrt((self.trans14[0]-trans1[0])**2+(self.trans14[1]-trans1[1])**2+(self.trans14[2]-trans1[2])**2)
            print('Right distance: %s'%self.r_dist2head)  
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException): #check for tf exceptions
            print ('Error! Most Likely a tf lookup exception')
            self.r_dist2head=1.

        #check if head is within reach of the right arm      
        if self.r_dist2head >(self.r_arm_length):
            print('Head not reachable')
            print('Right arm too short')
             #send message to master control, so it will not start yet
            self.pub.publish('Too far')
            #move base to be within reach of right arm
            self.base_mover('r')
        elif self.r_dist2head==1.:
            #if there was a tf exception try again 3 times before quitting
            print('calculation failed')
            self.r=self.r+1
            if self.r<=3:
                print('trying again')
                self.calc_right()
            else:
                print('exiting')
                os._exit(0)  
        else:
            print ('Head within reach')
            self.pub.publish('Ready')

    def base_mover(self, side):
        if side == 'l':
            #make sure it won't run over someone's foot
            #move base so left arm is within range of head
            print('moving better location for the left arm')
            while  not rospy.is_shutdown() and self.l_dist2head>self.l_arm_length:
                (trans1, rot1)=self.listener.lookupTransform('/l_shoulder_pan_link', '/odom_combined', rospy.Time(0))
                (trans2, rot2)=self.listener.lookupTransform('/base_footprint', '/odom_combined', rospy.Time(0))
                #(trans14, rot14)=self.listener.lookupTransform('/head_frame', '/odom_combined', rospy.Time(0))
                
                self.l_dist2head=math.sqrt((trans1[0]-self.trans14[0])**2+(trans1[1]-self.trans14[1])**2+(trans1[2]-self.trans14[2])**2)
                self.cmd.linear.x=trans2[0]-self.trans14[0]
                self.cmd.linear.y=trans2[1]-self.trans14[1]
                self.cmd.linear.z=0.
                self.cmd.angular.x=0.
                self.cmd.angular.y=0.
                self.cmd.angular.z=0.
                self.move.publish(self.cmd)
                rospy.sleep(1)
            #when done moving
            print('done moving')
            print('performing final head check')
            #check to make sure it worked and moving the base didn't mess up the other arm
            self.t=0
            self.calc_left()
            self.calc_right()
        if side == 'r':
            #make sure it won't run over someone's foot
            #move base so right arm is within range of head
            print('moving to better location for right arm')
            while not rospy.is_shutdown() and self.r_dist2head>self.r_arm_length:        
                (trans1, rot1)=self.listener.lookupTransform('/r_shoulder_pan_link', '/odom_combined', rospy.Time(0))
                (trans2, rot2)=self.listener.lookupTransform('/base_footprint', '/odom_combined', rospy.Time(0))
                #(trans14, rot14)=self.listener.lookupTransform('/head_frame', '/odom_combined', rospy.Time(0))
                self.r_dist2head=math.sqrt((trans1[0]-self.trans14[0])**2+(trans1[1]-self.trans14[1])**2+(trans1[2]-self.trans14[2])**2)
                self.cmd.linear.x=trans2[0]-self.trans14[0]
                self.cmd.linear.y=trans2[1]-self.trans14[1]
                self.cmd.linear.z=0.
                self.cmd.angular.x=0.
                self.cmd.angular.y=0.
                self.cmd.angular.z=0.
                self.move.publish(self.cmd)
                rospy.sleep(1)
            #when done moving
            print('done moving')
            print('performing final head check')
            #check to make sure it worked and that moving the base didn't mess up the other arm
            self.t=0
            self.calc_left()
            self.calc_right()

       


if __name__=='__main__':
    a = check_head()
    while not rospy.is_shutdown():
        rospy.spin()
