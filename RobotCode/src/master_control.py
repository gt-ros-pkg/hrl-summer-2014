#! /usr/bin/python
from RobotCode.srv import *
import roslib; roslib.load_manifest('RobotCode')
roslib.load_manifest('snapshot')
roslib.load_manifest('rospy')
roslib.load_manifest('actionlib')
roslib.load_manifest('pr2_controllers_msgs')
roslib.load_manifest('geometry_msgs')
import time
from std_msgs.msg import String
import actionlib
from actionlib_msgs.msg import *
from pr2_controllers_msgs.msg import *
from geometry_msgs.msg import *
import sys
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


print "waiting for compare_histo and snap_node"
rospy.wait_for_service('compare_histo')
rospy.wait_for_service('snap_node')
print "compare_histo and snap_node found"
pic = rospy.ServiceProxy('snap_node', CompareHisto)

###Subscribers set global variables used by all functions

def check_task(word): #Checking if the task is complete
    global globev_task_check 
    globev_task_check = word.data

def check_emerg(word): #Checking if anomaly detected
    print "STOP recieved. Stopping"
    global globev_emergency 
    globev_emergency = word.data

def check_mctrl(word): #Checking what state the robot is in
    global globev_main_ctrl 
    globe_main_ctrl = word.data


##Task Control
#Publish msgs to control topic and wait for action node to tell when done
#                               while checking for anomaly on emergency topic 
#When finished will reset task done variable
def task_control(task):
    print ("In %s loop" % task)
    send.publish(task)
    global globev_task_check
    global globev_emergency
    while (globev_emergency != "STOP" and globev_task_check != (task+"Done") and not rospy.is_shutdown()):
        r.sleep()
    task_set.publish("no")
    print ("Done with %s" % task)



###Histogram Nodes Control
def take_pic():
    print "taking first picture"
    pit = 0
    pit = pic(0)
    got_yogurt = "no"

def compare_pic():
    print "comparing picture"
    pit = 0
    pit = pic(0)
    rec = rospy.ServiceProxy('compare_histo', CompareHisto)
    ret = rec(0)
    print "made it this far"
    print "%d"%ret.R
    got_yogurt = False
    if ret.R == 1:
        print "No major change"
        got_yogurt = False
    elif ret.R == 0 :
        print "Changes occured"
        got_yogurt = True
    else :
        print "Image Loaded"
    return got_yogurt


if __name__ == "__main__":
    rospy.Subscriber('emergency', String, check_emerg)
    rospy.Subscriber('task_check', String, check_task)
    rospy.Subscriber('Main_Control', String, check_mctrl)
    raw_input("Press enter to begin")
    task_control("GoToHome")
    test = False
    while not test:
        take_pic()
        task_control("HomeToBowl")
        task_control("ScoopYogurt")
        task_control("MoveToCheck")
        test = compare_pic()

    task_control("FacePos1")
    task_control("FacePos2")
    task_control("FacePos3")
        

