#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('ab_sum')
        self.a_sub = self.create_subscription(Int32,'a',self.callA,10)
        self.b_sub = self.create_subscription(Int32,'b',self.callB,10)
        self.ab_sum = self.create_publisher(Int32,'sum_c',10)

        self.get_logger().info('sum a,b publish hogya sir')
        self.a_val = None
        self.b_val = None
    
    def callA(self,msg:Int32):
        self.a_val = msg.data
        self.calc()

    def callB(self,msg:Int32):
        self.b_val = msg.data
        self.calc()
    
    def calc(self):
        if self.a_val is not None and self.b_val is not None:
            result=Int32()
            result.data=self.a_val+self.b_val
            self.ab_sum.publish(result)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
