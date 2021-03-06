#! /usr/bin/python

import copy

import roslib; roslib.load_manifest('hrl_head_registration'); roslib.load_manifest('RYDS')
import rospy
import rosbag
from RYDS.srv import *
from std_msgs.msg import String
from geometry_msgs.msg import PointStamped
from hrl_head_registration.srv import HeadRegistration, ConfirmRegistration


def primary():
    rospy.Subscriber("/clickable_display/l_mouse_click",PointStamped,l_react)
    rospy.Subscriber("/clickable_display/r_mouse_click",PointStamped,r_react)
    
    print "subscribed"
    rospy.spin()

def l_react(point_msgs):
    print "l_react"
    rospy.wait_for_service("initialize_registration")
    click_l = rospy.ServiceProxy("initialize_registration",HeadRegistration)
    trash = click_l(point_msgs.point.x, point_msgs.point.y)
 

def r_react(point_msgs):
    print "r_react"
    rospy.wait_for_service("confirm_registration")
    click_r = rospy.ServiceProxy("confirm_registration",ConfirmRegistration)
    trash = click_r()
    


if __name__ == "__main__":
    rospy.init_node('click_shuttle')
    primary()
    rospy.spin()
