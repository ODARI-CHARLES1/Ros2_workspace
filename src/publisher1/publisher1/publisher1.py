#!/usr/bin/env python3 

import rclpy 
from rclpy.node import Node

class DrawCircleNode(Node):
    def __init__(self):
        super().__init__("draw circle")
        self.cmd_vel_pub=self.create_publisher()
        self.get_logger().info("Draw circle node has been started")

def main(args=None):
    rclpy.init(args=args)
