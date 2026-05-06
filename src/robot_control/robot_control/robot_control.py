#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class RobotControlNode(Node):
    def __init__(self):
        super().__init__("Robot_Control_Node")
        self.get_logger().info("Robot control node running...")
        self.create_timer(1.0,self.timer_callback)
    def timer_callback(self):
        self.get_logger().info(f"Robot Control node running ...")
     
     
def main(args=None):
    rclpy.init(args=args)
    node=RobotControlNode()
    # rclpy.spin(node)
    rclpy.spin(node)
    rclpy.shutdown()


if __name__=="__main__":
    main()