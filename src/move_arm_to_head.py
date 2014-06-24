#!/usr/bin/env python  
import roslib
roslib.load_manifest('feed_yogurt')
import rospy
import math
import tf

if __name__ == '__main__':
    rospy.init_node('move_arm_to_head')

    listener = tf.TransformListener()
    Broadcaster = tf.TransformBroadcaster()

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        Broadcaster.sendTransform((0.2, 0.0, 0.0),(0.0, 0.0, 0.0, 1.0),
                        rospy.Time.now(),"/FeedPos", "/head_frame")
        try:
            (trans,rot) = listener.lookupTransform('/base_link', '/head_frame', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        


        rate.sleep()
