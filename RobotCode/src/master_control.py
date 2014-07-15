#! /usr/bin/python
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
#sets global variables 
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


print "waiting for compare_histo and snap_node and haptic mpc"
rospy.wait_for_service('compare_histo')
rospy.wait_for_service('snap_node')
rospy.wait_for_service('haptic_mpc/enable_mpc')
print "compare_histo and snap_node and haptic mpc found"
pic = rospy.ServiceProxy('snap_node', CompareHisto)
haptic = rospy.ServiceProxy('haptic_mpc/enable_mpc', EnableHapticMPC)
haptic('False')

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


##Task Control
#Publish msgs to control topic and wait for action node to tell when done
#                               while checking for anomaly on emergency topic 
#When finished will reset task done variable
def task_control(task):
    global globev_emergency
    if globev_emergency == "STOP":
        return
    print ("In %s task." % task)
    send.publish(task)
    global globev_task_check
    while (globev_emergency != "STOP" and globev_task_check != (task+"Done") and not rospy.is_shutdown()):
        r.sleep()
    task_set.publish("no")
    print ("Done with %s" % task)

def move_to_pic(frame):
    global globev_emergency
    if globev_emergency == "STOP":
        return
    client = actionlib.SimpleActionClient('/head_traj_controller/point_head_action', PointHeadAction)
    client.wait_for_server()

    g = PointHeadGoal()
    g.target.header.frame_id = frame
    g.target.point.x = 0.0
    g.target.point.y = -0.3
    g.target.point.z = 0.1
    g.min_duration = rospy.Duration(1.0)

    client.send_goal(g)
    client.wait_for_result()

    if client.get_state() == GoalStatus.SUCCEEDED:
        print "Head Movement Succeeded"
    else:
        print "Head Movement Failed"

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
        print "Image Loaded"
    return got_yogurt

def run_task():
    rospy.Subscriber('emergency', String, check_emerg)
    rospy.Subscriber('task_check', String, check_task)
    rospy.Subscriber('Main_Control', String, check_mctrl)
    raw_input("Press enter to begin")
    task_control("GoToHome")
    task_control("GoToHome")
    rospy.sleep(2.)
    print "AT HOME"
    move_to_pic('l_gripper_tool_frame')
    rospy.sleep(2.)
    print "AT PICTURE SPOT"
    test = False
    while not (rospy.is_shutdown() and globev_emergency != "STOP"):
        while (not test and not rospy.is_shutdown() and globev_emergency != "STOP"):
            rospy.sleep(1.)
            print "TAKING PICTURE"
            take_pic()
            print "PICTURE TAKEN"
            rospy.sleep(.2)
            task_control("HomeToBowl")
            rospy.sleep(.2)
            task_control("ScoopYogurt")
            rospy.sleep(.2)
            task_control("MoveToCheck")
            rospy.sleep(.2)
            task_control("GoToHome")
            task_control("GoToHome")
            print "AT HOME2"

            rospy.sleep(1.)
            print "MAKING SECOND PICTURE AND COMPARING"
            test = compare_pic()
        test = False
        rospy.sleep(1.)
        haptic('Enabled')
        print "haptic control enabled"
        task_control("SwitchControllers")
        print "Controller switched"
        task_control("FacePos1")
        rospy.sleep(6.)
        #raw_input("Press enter when FacePos1 reached")
        task_control("FacePos2")
        raw_input("Press enter when FacePos2 reached")
        rospy.sleep(3.)
        task_control("FacePos3")
        rospy.sleep(6.)
        #raw_input("Press enter when FacePos3 reached")
        haptic('False')
        print "haptic control disabled"
        task_control("GoToHome")
        task_control("GoToHome")
        rospy.sleep(2.)
        print "AT HOME"
        move_to_pic('l_gripper_tool_frame')
        rospy.sleep(2.)
        print "AT PICTURE SPOT"
        raw_input("Press enter to repeat")

if __name__ == "__main__":
    run_task()

    

