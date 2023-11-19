#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped
rospy.init_node('get_pose', anonymous=False)
def get_pose(msg):
    # print(msg, type(msg))
    print(msg.pose.position.z)

rospy.Subscriber("/ground_truth_to_tf/pose", PoseStamped, get_pose, queue_size=1)
rospy.spin()