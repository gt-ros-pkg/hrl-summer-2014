#! /usr/bin/python

#Chris Birmingham, HRL, 7/16/14
#This file controls the state the robot is in and what actions 
#it performs. It broadcasts the robot state to the Main_Control topic
#and listens to the task_check topic to know when action nodes are done
#performing an action and listens to emergency to know when an anomaly has 
#occured. 

from RYDS.srv import *
import roslib; roslib.load_manifest('RYDS')
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
#starts publishers, subscribers, and services needed for running
#the yogurt feeding process

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

print "waiting for compare_histo and snap_node and haptic mpc"
rospy.wait_for_service('haptic_mpc/enable_mpc')
rospy.wait_for_service('right/haptic_mpc/enable_mpc')
haptic = rospy.ServiceProxy('haptic_mpc/enable_mpc', EnableHapticMPC)
haptic('False')
r_haptic = rospy.ServiceProxy('right/haptic_mpc/enable_mpc', EnableHapticMPC)
r_haptic('False')
rospy.wait_for_service('compare_histo')
rospy.wait_for_service('snap_node')
print "compare_histo and snap_node and haptic mpc found"
pic = rospy.ServiceProxy('snap_node', CompareHisto)
haptic('False')


###Subscriber callbacks set global variables used by all functions###

def check_task(word): #Checking if the task is complete
    global globev_task_check 
    globev_task_check = word.data

def check_emerg(word): #Checking if anomaly detected
    global globev_emergency 
    globev_emergency = word.data
    print "Stop recieved!"
    os._exit(0)     #exits when stop is recieved

def check_mctrl(word): #Checking what state the robot is in
    global globev_main_ctrl 
    globe_main_ctrl = word.data

def usr_input(words):
    reciever = raw_input('%s' % words)
    return reciever


###Task Control###
#Publish msgs to control topic and wait for action node to tell when done while
#checking for anomaly on emergency topic. When finished will reset task done variable
def task_control(task):
    global globev_emergency
    global send 
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
        g.target.point.x = 0.2
        g.target.point.y = -0.2
        g.target.point.z = 0.0
        g.min_duration = rospy.Duration(1.0)
        client.send_goal(g)
        client.wait_for_result()
    else:    #used for going to the spoon
        client = actionlib.SimpleActionClient('/head_traj_controller/point_head_action', PointHeadAction)
        client.wait_for_server()
        g = PointHeadGoal()
        g.target.header.frame_id = frame
        g.target.point.x = 0.0
        g.target.point.y = 0.0
        g.target.point.z = 0.0
        g.min_duration = rospy.Duration(1.0)

        client.send_goal(g)
        client.wait_for_result()


###Histogram Control###
#take_pic takes a picture of the spoon and saves the picture 
#for making a comparison
def take_pic():
    pit = -1
    while pit == -1:
        global globev_emergency
        if globev_emergency == "STOP":
            return
        print "taking first picture"
        pit = 0
        pit = pic(0)
    print "picture returned"


def compare_pic():
    global globev_emergency
    if globev_emergency == "STOP":
        return
    print "comparing picture"
    pit = 0
    pit = pic(1)
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

###Main Function###
#
def run_task():
    move_to_pic('/head_frame')
    rospy.Subscriber('emergency', String, check_emerg)
    rospy.Subscriber('task_check', String, check_task)
    rospy.Subscriber('Main_Control', String, check_mctrl)

    raw_input("Press enter when ready to begin")
    haptic('Enabled')
    r_haptic('Enabled')

    part = 0
    while not rospy.is_shutdown() and globev_emergency != "STOP":

        if part > 11 or part < 0:
            send.publish("STOP")
            check = raw_input("continue? (y) or (n)")
            if check == 'n':
                send.publish("STOP")
                os._exit(0)
               
            elif check == 'y':
                send.publish("STOP")
                part = 0

        task_control("Part%s" %str(part))
        task_control("Part%s" %str(part)) #Done twice to ensure it reaches the correct location
        rospy.sleep(3)
        if part == 0:
            move_to_pic('/l_gripper_spoon_frame')
            take_pic()
        if part == 7:
            task_control("Part%s" %str(part))
            test = compare_pic()
            if test == False:
                part = 0
        if part == 10:
            rospy.sleep(3)

        part = part + 1




if __name__ == "__main__":
    run_task()

    

