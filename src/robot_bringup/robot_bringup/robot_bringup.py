#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class RobotBringupNode(Node):
    def __init__(self):
        super().__init__("Robot_bringup_node")
        self.get_logger().info("Robot Bringup node running...")
    
    
def main(args=None):
    rclpy.init(args=args)
    node=RobotBringupNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()