#!/usr/bin/env python  
import roslib
roslib.load_manifest('RobotCode')
import rospy
import math
import numpy as np
import tf
import std_msgs.msg
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
import geometry_msgs.msg
import tf_conversions.posemath as pm

if __name__ == '__main__':
    rospy.init_node('convert_tf_to_pose')
    listener = tf.TransformListener()
    Broadcaster = tf.TransformBroadcaster()
    i = 0
    pose_pub = rospy.Publisher('feed_pos', PoseStamped)

    rate = rospy.Rate(10.0)
#translational note: (red,green,blue)
#Quaternian note: (red,green,blue,?)
    while not rospy.is_shutdown():
        Broadcaster.sendTransform((0.6, -0.1, -0.1),(3, 14, 20, -1),
                        rospy.Time.now(),"/FeedPos", "/head_frame")
        #Broadcaster.sendTransform((0.49, -0.0, -0.1),(3, 14, 20, -1),
        #                rospy.Time.now(),"/FeedPos", "/head_frame")
        #Broadcaster.sendTransform((0.53, -0.0, -0.08),(3, 14, 20, -1),
        #                rospy.Time.now(),"/FeedPos", "/head_frame")
        try:
            (trans, rot) = listener.lookupTransform('/torso_lift_link', '/FeedPos', rospy.Time(0))
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
            pose_msg = PoseStamped(
               header = hdr,
               pose = Pose(transa, rota))
            #print pose_msg
            pose_pub.publish(pose_msg)
            i=i+1
            
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        


        rate.sleep()
