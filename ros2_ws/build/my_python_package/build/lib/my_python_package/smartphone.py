#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
 
 
class SmartPhoneNode(Node): 
    def __init__(self):
        super().__init__("smartphone") # type: ignore
        self.subsriber = self.create_subscription(String, "robot_news", self.smartphone_callback, 10) 
        self.get_logger().info("smartphone node has started")

    def smartphone_callback(self, msg):
        self.get_logger().info(msg.data)
 
def main(args=None):
    rclpy.init(args=args)
    node = SmartPhoneNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()