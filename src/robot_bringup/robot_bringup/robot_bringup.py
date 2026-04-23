#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

def main(args=None):
    rclpy.init(args=args)
    node=Node("python_node")
    node.get_logger().info("Testing node.... in ROS2")
    rclpy.shutdown()

