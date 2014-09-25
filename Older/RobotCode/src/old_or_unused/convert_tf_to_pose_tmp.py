#!/usr/bin/env python  
import roslib
roslib.load_manifest('RobotCode')
import rospy
import math
import time
import numpy as np
import tf
import std_msgs.msg
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
import geometry_msgs.msg
import tf_conversions.posemath as pm

stop = ""
i = 0


def e_check(data):
    global stop 
    stop = data.data
    if stop != "STOP":
        return
    data.data = "FaceStop"
    run("Face")

#translational note: (red,green,blue)
#Quaternian note: (red,green,blue,twist)
def broadcaster(position):
    Broadcaster = tf.TransformBroadcaster()
    if position == "FacePos1":
        Broadcaster.sendTransform((0.6, -0.1, -0.1),(3, 14, 13, -1),
                        rospy.Time.now(),"/FeedPos", "/head_frame")
        print "Broadcast transform for FacePos1"
    elif position =="FacePos2":
        Broadcaster.sendTransform((0.285, -0.0, -0.0),(3, 14, 13, -1),
                        rospy.Time.now(),"/FeedPos", "/head_frame")
        print "Broadcast transform for FacePos2"
    elif position =="FacePos3":
        Broadcaster.sendTransform((0.53, -0.0, -0.08),(3, 14, 13, -1),
                        rospy.Time.now(),"/FeedPos", "/head_frame")
        print "Broadcast transform for FacePos3"

    #Broadcast current position to force movement to stop
    if stop == "STOP":
        Broadcaster.sendTransform((0, 0, 0),(0, 0, 0, 1),
                        rospy.Time.now(),"/FeedPos", "/l_wrist_roll_link") 
        print "Broadcast STOP"
    return

def run(data):
    position = data

    if position[0] != "F":
        print ("Heard: %s, will keep listening." % position)
        return

    print ("Heard: %s, Starting." % position)

    task_set = rospy.Publisher('task_check', String)
    task_set.publish("no")

    listener = tf.TransformListener()
    pose_pub = rospy.Publisher('haptic_mpc/goal_pose', PoseStamped)

    rat = rospy.Rate(1)
    print "Entering loop"
    published = False
    while (not rospy.is_shutdown() and published == False):
        global i
        broadcaster(position)
        try:
            (trans, rot) = listener.lookupTransform('/torso_lift_link', '/FeedPos', 
                                                                      rospy.Time(0))
            hdr = std_msgs.msg.Header()
            hdr.frame_id = '/torso_lift_link'
            hdr.stamp = rospy.Time.now()
            hdr.seq = i
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
            pose_pub.publish(pose_msg)
            published = True
            print "goal pose published"

        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            print "tf Exception, please broadcast again"

    while (not rospy.is_shutdown() and stop != "STOP"):
        broadcaster(position)
        try:
            (trans, rot) = listener.lookupTransform('/l_wrist_roll_link', '/FeedPos', rospy.Time(0))
            print trans, rot
            if (trans[1] < .01 and trans[2] < .01):
                raw_input("Press enter when close enough")
                msg = position + "Done"
                task_set.publish(msg)
                break
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        rat.sleep()

if __name__ == '__main__':
    rospy.init_node('convert_tf_to_pose')
    run("FacePos1")
    run("FacePos2")
    run("FacePos3")
    rospy.Subscriber('Main_Control', String, run)
    rospy.Subscriber('emergency', String, e_check)
    rospy.spin()



       
