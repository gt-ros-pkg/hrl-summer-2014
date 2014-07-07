#! /usr/bin/python
from RobotCode.srv import *
import roslib; roslib.load_manifest('RobotCode')
import rospy
import time
from std_msgs.msg import String

globvar = ""

def check(word):
    global globvar 
    globvar = word.data

if __name__ == "__main__":
    rospy.init_node('master_control')
    stopcheck = rospy.Publisher('emergency', String)
    stopcheck.publish("GO")
    send = rospy.Publisher('Main_Control', String)
    send.publish("Wait")
    task_set = rospy.Publisher('task_check', String)
    task_set.publish("no")
    rospy.Subscriber('emergency', String, check)
    stop = globvar
    rospy.Subscriber('task_check', String, check)
    done = globvar

    raw_input("Press enter to begin")
    r = rospy.Rate(20)
    print "In MoveToHome loop"
    while (stop != "STOP" and done != "yes" and not rospy.is_shutdown()):
        task = "MoveToHome"
        send.publish(task)
        rospy.Subscriber('emergency', String, check)
        stop = globvar
        rospy.Subscriber('task_check', String, check)
        done = globvar
        r.sleep()
    task_set.publish("no")
    while globvar != "no" and not rospy.is_shutdown():
        rospy.Subscriber('task_check', String, check)
    done = globvar
    print ("Done with MoveToYogurt?: " + done)

    print "Should be in MoveToYogurt loop"
    while (stop != "STOP" and done != "yes" and not rospy.is_shutdown()):
        task = "MoveToYogurt"
        send.publish(task)
        rospy.Subscriber('emergency', String, check)
        stop = globvar
        rospy.Subscriber('task_check', String, check)
        done = globvar
        r.sleep()
    task_set.publish("no")
    while globvar != "no" and not rospy.is_shutdown():
        rospy.Subscriber('task_check', String, check)
    done = globvar
    print ("Done with MoveToInBowl?: " + done)

    print "Should be in MoveToInBowl loop"
    while (stop != "STOP" and done != "yes" and not rospy.is_shutdown()):
        task = "MoveToInBowl"
        send.publish(task)
        rospy.Subscriber('emergency', String, check)
        stop = globvar
        rospy.Subscriber('task_check', String, check)
        done = globvar
        r.sleep()
    task_set.publish("no")
    while globvar != "no" and not rospy.is_shutdown():
        rospy.Subscriber('task_check', String, check)
    done = globvar
    print ("Done?: " + done)

    print "Should be done"

    rospy.spin()
        

