#!/usr/bin/env python  
import roslib
roslib.load_manifest('RobotCode')
import rospy
import math
import numpy as np
import tf
import std_msgs.msg
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
import tf_conversions.posemath as pm

if __name__ == '__main__':
    rospy.init_node('move_arm_to_head')
    listener = tf.TransformListener()
    Broadcaster = tf.TransformBroadcaster()
    i = 0
    pose_pub = rospy.Publisher('feed_pos', PoseStamped)

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        Broadcaster.sendTransform((0.2, 0.0, 0.0),(0.0, 0.0, 0.0, 1.0),
                        rospy.Time.now(),"/FeedPos", "/r_gripper_r_finger_link")
        try:
            (trans, rot) = listener.lookupTransform('/base_link', '/FeedPos', rospy.Time(0))
            hdr = std_msgs.msg.Header()
            hdr.frame_id = '/head_frame',
            hdr.stamp = rospy.Time.now(),
            hdr.seq = i
            pose_msg = PoseStamped(
               header = hdr,
               pose = Pose(trans, rot))
            #pose_pub.publish(pose_msg)
            i=i+1
            print pose_msg
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        


        rate.sleep()
