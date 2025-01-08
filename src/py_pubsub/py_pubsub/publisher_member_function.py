#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('publish_a_b')
        self.a= self.create_publisher(Int32, 'a', 10)
        self.b= self.create_publisher(Int32, 'b', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.send_msg)
        self.get_logger().info('Published')

    def send_msg(self):
        msga = Int32()
        msga.data = 32
        msgb = Int32()
        msgb.data = 45
        self.a.publish(msga)
        self.b.publish(msgb)

def main(args=None):
    rclpy.init(args=args)

    publish_a_b = MinimalPublisher()

    rclpy.spin(publish_a_b)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
