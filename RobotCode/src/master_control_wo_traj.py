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
    print "In HomeToBowl loop"
    while (stop != "STOP" and done != "yes" and not rospy.is_shutdown()):
#        task = "HomeToBowl"
#        send.publish(task)
#        rospy.Subscriber('emergency', String, check)
#        stop = globvar
#        rospy.Subscriber('task_check', String, check)
#        done = globvar
#        r.sleep()
#    task_set.publish("no")
#    while globvar != "no" and not rospy.is_shutdown():
#        rospy.Subscriber('task_check', String, check)
#    done = globvar
#    print "Done with HomeToBowl"
#
#    print "Should be in ScoopYogurt loop"
#    while (stop != "STOP" and done != "yes" and not rospy.is_shutdown()):
#        task = "ScoopYogurt"
#        send.publish(task)
#        rospy.Subscriber('emergency', String, check)
#        stop = globvar
#        rospy.Subscriber('task_check', String, check)
#        done = globvar
#        r.sleep()
#    task_set.publish("no")
#    while globvar != "no" and not rospy.is_shutdown():
#        rospy.Subscriber('task_check', String, check)
#    done = globvar
#    print "Done with MoveToYogurt"
#
#    print "Should be in MoveToCheck loop"
#    while (stop != "STOP" and done != "yes" and not rospy.is_shutdown()):
#        task = "MoveToCheck"
#        send.publish(task)
#        rospy.Subscriber('emergency', String, check)
#        stop = globvar
#        rospy.Subscriber('task_check', String, check)
#        done = globvar
#        r.sleep()
#    task_set.publish("no")
#    while globvar != "no" and not rospy.is_shutdown():
#        rospy.Subscriber('task_check', String, check)
#    done = globvar
#    print "Done with MoveToCheck"

    print "Should be in FacePos1 loop"
    while (stop != "STOP" and done != "yes" and not rospy.is_shutdown()):
        task = "FacePos1"
        send.publish(task)
        rospy.Subscriber('emergency', String, check)
        stop = globvar
        rospy.Subscriber('task_check', String, check)
        done = globvar
        r.sleep()
    task_set.publish("no")
    print "Done with FacePos1"
    while globvar != "no" and not rospy.is_shutdown():
        rospy.Subscriber('task_check', String, check)
    done = globvar

    
    print "Should be in FacePos2 loop"
    while (stop != "STOP" and done != "yes" and not rospy.is_shutdown()):
        task = "FacePos2"
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
    print "Done with FacePos2"

    print "Should be in FacePos3 loop"
    while (stop != "STOP" and done != "yes" and not rospy.is_shutdown()):
        task = "FacePos3"
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
    print "Done with FacePos3"

    rospy.spin()
        

