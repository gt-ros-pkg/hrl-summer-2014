#! /usr/bin/python

#Chris Birmingham, HRL, 7/16/14
#This file controls the state the robot is in and what actions 
#it performs. It broadcasts the robot state to the Main_Control topic
#and listens to the task_check topic to know when action nodes are done
#performing an action and listens to emergency to know when an anomaly has 
#occured. 

from RobotCode.srv import *
import roslib; roslib.load_manifest('RobotCode')
roslib.load_manifest('snapshot')
roslib.load_manifest('rospy')
roslib.load_manifest('actionlib')
roslib.load_manifest('pr2_controllers_msgs')
roslib.load_manifest('geometry_msgs')
roslib.load_manifest('hrl_haptic_mpc')
from std_msgs.msg import String
import actionlib
from actionlib_msgs.msg import *
from pr2_controllers_msgs.msg import *
from geometry_msgs.msg import *
from hrl_haptic_manipulation_in_clutter_srvs.srv import *
import sys
import os
import rospy
from snapshot.srv import *


###Initializations###
#starts publishers, subscribers, and services

rospy.init_node('master_control')

globev_task_check = ""
globev_emergency = ""
globev_main_ctrl = ""
r = rospy.Rate(10)

stopcheck = rospy.Publisher('emergency', String)
stopcheck.publish("GO")

send = rospy.Publisher('Main_Control', String)
send.publish("Wait")

task_set = rospy.Publisher('task_check', String)
task_set.publish("no")

#print "waiting for compare_histo and snap_node and haptic mpc"
rospy.wait_for_service('haptic_mpc/enable_mpc')
haptic = rospy.ServiceProxy('haptic_mpc/enable_mpc', EnableHapticMPC)
haptic('False')
#rospy.wait_for_service('compare_histo')
#rospy.wait_for_service('snap_node')
#print "compare_histo and snap_node and haptic mpc found"
#pic = rospy.ServiceProxy('snap_node', CompareHisto)
#haptic('False')


###Subscribers set global variables used by all functions

def check_task(word): #Checking if the task is complete
    global globev_task_check 
    globev_task_check = word.data

def check_emerg(word): #Checking if anomaly detected
    global globev_emergency 
    globev_emergency = word.data
    #sys.exit("STOP recieved. Exiting.")
    print "Stop recieved!"
    os._exit(0)

def check_mctrl(word): #Checking what state the robot is in
    global globev_main_ctrl 
    globe_main_ctrl = word.data

def usr_input(words):
    reciever = raw_input('%s' % words)
    return reciever


###Task Control
#Publish msgs to control topic and wait for action node to tell when done while
#checking for anomaly on emergency topic. When finished will reset task done variable
def task_control(task):
    global globev_emergency
    if globev_emergency == "STOP":
        return
    print ("Main ctrl in %s task." % task)
    send.publish(task)
    global globev_task_check
    while (globev_emergency != "STOP" and globev_task_check != (task+"Done") and not rospy.is_shutdown()):
        r.sleep()
    task_set.publish("no")
    print ("Main ctrl done with %s" % task)

#Moves head to take picture of target frame
def move_to_pic(frame):
    global globev_emergency
    if globev_emergency == "STOP":
        return
    if frame == 'head_frame':
        client = actionlib.SimpleActionClient('/head_traj_controller/point_head_action', PointHeadAction)
        client.wait_for_server()
        g = PointHeadGoal()
        g.target.header.frame_id = frame
        g.min_duration = rospy.Duration(1.0)
        client.send_goal(g)
        client.wait_for_result()
    else:    
        client = actionlib.SimpleActionClient('/head_traj_controller/point_head_action', PointHeadAction)
        client.wait_for_server()

        g = PointHeadGoal()
        g.target.header.frame_id = frame
        g.target.point.x = 0.3
        g.target.point.y = -0.2
        g.target.point.z = 0
        g.min_duration = rospy.Duration(1.0)

        client.send_goal(g)
        client.wait_for_result()


###Histogram Nodes Control
def take_pic():
    global globev_emergency
    if globev_emergency == "STOP":
        return
    print "taking first picture"
    pit = 0
    pit = pic(0)
    got_yogurt = "no"

def compare_pic():
    global globev_emergency
    if globev_emergency == "STOP":
        return
    print "comparing picture"
    pit = 0
    pit = pic(0)
    rec = rospy.ServiceProxy('compare_histo', CompareHisto)
    ret = rec(0)
    print "made it this far"
    print "%d"%ret.R
    got_yogurt = False
    if ret.R == 1:
        print "No major change, scoop again."
        got_yogurt = False
    elif ret.R == 0 :
        print "Changes occured, proceeding"
        got_yogurt = True
    else :
        print "Image Loaded for first time"
    return got_yogurt

def run_task():
    #move_to_pic('head_frame')
    #rospy.Subscriber('emergency', String, check_emerg)
    rospy.Subscriber('task_check', String, check_task)
    #rospy.Subscriber('Main_Control', String, check_mctrl)
    raw_input("Press enter when ready to begin")
    task_control("GoToHome")
    rospy.sleep(0.5)
    #move_to_pic('l_gripper_tool_frame')
    rospy.sleep(0.5)
    test = False
    while not (rospy.is_shutdown() and globev_emergency != "STOP"):
        while (not test and not rospy.is_shutdown() and globev_emergency != "STOP"):
            rospy.sleep(1.)
            #print "TAKING PICTURE"
            #take_pic()
            #print "PICTURE TAKEN"
            rospy.sleep(.2)
            task_control("HomeToBowl")
            rospy.sleep(.2)
            task_control("ScoopYogurt")
            rospy.sleep(.2)
            task_control("MoveToCheck")
            rospy.sleep(.2)
            task_control("GoToHome")
            rospy.sleep(1.)
            #print "TAKING SECOND PICTURE AND COMPARING"
            #test = compare_pic()
            #if test:
            #    print "Yogurt registered. Continuing."
            #else:
            #    check = usr_input("Yogurt not registered. (c)ontinue or (r)epeat?")
            #    if check == 'c':
            #        test = True
        test = False
        rospy.sleep(1.)
        haptic('Enabled')
        print "haptic control enabled"
        task_control("SwitchControllers")
        print "Controller switched"
        task_control("FacePos1")
        rospy.sleep(6.)
        usr_input("Press enter when ready")
        task_control("FacePos2")
        usr_input("Press enter when yogurt recieved")
        rospy.sleep(3.)
        task_control("FacePos3")
        rospy.sleep(6.)
        haptic('False')
        print "haptic control disabled"
        task_control("GoToHome")
        rospy.sleep(2.)
        print "AT HOME"
        #move_to_pic('l_gripper_tool_frame')
        rospy.sleep(2.)
        #print "AT PICTURE SPOT"
        check = usr_input("Done! (c)ontinue eating, (s)top, or (t)owel?")
        if check == 't':
            print "Feature coming soon. A thousand apologies."
            check = usr_input("(c)ontinue or (s)top?")
        if check == 's':
            print "Stopping."
            os._exit(0)
        elif check == 'c':
            print "Continuing"


if __name__ == "__main__":
    run_task()

    

