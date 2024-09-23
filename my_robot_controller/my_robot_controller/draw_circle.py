#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist # gotten from ros2 info on the turtlesim node

class DrawCircleNode(Node):
    def __init__(self):
        super().__init__("draw_circle") #Node name
        # PAY ATTENTION TO TYPE AND NAME OR COMMUNCATION WILL NOT WORK
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10) #Creating a ros publisher
        self.timer = self.create_timer(0.5, self.send_velocity_command) # Timer to callback function to publish the msg 
        self.get_logger().info("Draw circle node has been started") #Logging message

    # callback 
    def send_velocity_command(self):
        msg = Twist()
        # from "ros2 interface show geometry_msgs/msg/Twist"
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub_.publish(msg)

    

def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node) # spinning the node to iterate and not shutdown after one 
    rclpy.shutdown()
