#!usr/bin/env python3

import rclpy
from rclpy.node import Node

def main():
    rclpy.init()
    node=Node("python_node")
    node.get_logger().info("Testing robot description.... in ROS2")
    rclpy.shutdown()