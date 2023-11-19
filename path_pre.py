#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Point 
from geometry_msgs.msg import PoseStamped
pos = [0, 0, 0]
rospy.init_node("rec_path")

pub_obj=rospy.Publisher("/rec_path_pre",Point,queue_size=1)

def rec(msg):
    pos[0] = msg.pose.position.x
    pos[1] = msg.pose.position.y
    pos[2] = msg.pose.position.z
    pt=Point()
    pt.x=pos[0]
    pt.y=pos[1]
    pt.z=pos[2]
    print(pt)
    pub_obj.publish(pt)


rospy.Subscriber("/ground_truth_to_tf/pose", PoseStamped, rec,queue_size=1)
rospy.spin()