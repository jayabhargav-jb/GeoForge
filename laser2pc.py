#!/usr/bin/env python

import sensor_msgs.point_cloud2 as pc2
import rospy
from sensor_msgs.msg import PointCloud2, LaserScan
from sensor_msgs.msg import PointField
# from sensor_msgs.msg._Po
from geometry_msgs.msg import PoseStamped
# import geometry_msgs.msgs import
import laser_geometry.laser_geometry as lg
import math
pos=[0, 0, 0]
rospy.init_node("laserscan_to_pointcloud")

lp = lg.LaserProjection()

pc_pub = rospy.Publisher("converted_pc", PointCloud2, queue_size=1)
# pose_sub = 

def scan_cb(msg):
    # convert the message of type LaserScan to a PointCloud2
    pc2_msg = lp.projectLaser(msg)
    point_list = pc2.read_points_list(pc2_msg)
    print(list(point_list[0]))
    print("x", point_list[0].x)
    # a=b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    # x.deserialize(a)
    # print(a)
    # print(pc2_msg.fields[0], x)
    # print(x)
    # now we can do something with the PointCloud2 for example:
    # publish it
    print(type(point_list[0].x))
    resx=(point_list[0].x)+pos[0]
    print(resx)
    
    # pc2_msg.deserialize()
    # point_list[0].x = point_list[0].x._replace(x=)
    # pc2_msg.fields[1]=pc2_msg.fields[1]+pos[1]
    # pc2_msg.fields[2]=pc2_msg.fields[2]+pos[2]
    pc_pub.publish(pc2_msg)
    
    # convert it to a generator of the individual points
    point_generator = pc2.read_points(pc2_msg)
    

    # we can access a generator in a loop
    sum = 0.0
    num = 0
    for point in point_generator:
        if not math.isnan(point[2]):
            sum += point[2]
            num += 1
    # we can calculate the average z value for example
    # print(str(sum/num))

    # or a list of the individual points which is less efficient
    point_list = pc2.read_points_list(pc2_msg)
    # print(point_list)
    # print(point_list)
    # we can access the point list with an index, each element is a namedtuple
    # we can access the elements by name, the generator does not yield namedtuples!
    # if we convert it to a list and back this possibility is lost
    # print(point_list[int(len(point_list)/2)])

def get_pos(msg):
    pos[0] = msg.pose.position.x
    pos[1] = msg.pose.position.y
    pos[2] = msg.pose.position.z

rospy.Subscriber("/ground_truth_to_tf/pose", PoseStamped, get_pos, queue_size=1)
rospy.Subscriber("/scan", LaserScan, scan_cb, queue_size=1)
rospy.spin()