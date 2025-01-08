#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node): #NODE CREATION
    def __init__(self):
        super().__init__("first_node")
        self.create_timer(1.0,self.timer_callback)
        

    def timer_callback(self):
        self.get_logger().info("Hello fro ROS2")

def main(args=None):
    rclpy.init(args=args)

    node1 = MyNode() #NODE CREATED IN MAINpu
    rclpy.spin(node1)
    rclpy.shutdown()
    pass
if __name__ == '__main__':
    main()
