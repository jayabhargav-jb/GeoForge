import rospy
from geometry_msgs.msg import Twist

rospy.init_node('drone_control', anonymous=False)
vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

def initialize(vx,vy,vz,vangz):
    vel_msg = Twist()
    vel_msg.linear.x = float(vx)
    vel_msg.linear.y = float(vy)
    vel_msg.linear.z = float(vz)
    vel_msg.angular.z = float(vangz)
    vel_msg.angular.x = float(0.0)
    vel_msg.angular.y = float(0.0)
    vel_pub.publish(vel_msg)

def hover():
    initialize(0.0,0.0,0.0,0.0)

def up():
    vel_msg = Twist()
    vel_msg.linear.z = float(1.0)
    vel_pub.publish(vel_msg)

def down():
    vel_msg = Twist()
    vel_msg.linear.z = float(-1.0)
    vel_pub.publish(vel_msg)

def forward():
    vel_msg = Twist()
    vel_msg.linear.x = float(1.0)
    vel_pub.publish(vel_msg)

def backward():
    vel_msg = Twist()
    vel_msg.linear.x = float(-1.0)
    vel_pub.publish(vel_msg)

def right():
    vel_msg = Twist()
    vel_msg.linear.y = float(-1.0)
    vel_pub.publish(vel_msg)

def left():
    vel_msg = Twist()
    vel_msg.linear.y = float(1.0)
    vel_pub.publish(vel_msg)

def cw():
    vel_msg = Twist()
    vel_msg.angular.z = float(-1.0)
    vel_pub.publish(vel_msg)

def ccw():
    vel_msg = Twist()
    vel_msg.angular.z = float(1.0)
    vel_pub.publish(vel_msg)

if __name__ == "__main__":
    forward(1.0)