#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
 
 
class BasicSub(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("basic_sub") # type: ignore # MODIFY NAME 
        self.subscriber = self.create_subscription(String, "basic_pub", self.sub_callback, 10)
        self.get_logger().info("Basic Subscriber has started")

    def sub_callback(self, msg):
        self.get_logger().info(msg.data)
 
 
def main(args=None):
    rclpy.init(args=args)
    node = BasicSub() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()