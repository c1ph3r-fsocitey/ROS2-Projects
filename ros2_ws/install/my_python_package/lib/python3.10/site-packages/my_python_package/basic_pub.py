#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
 
 
class BasicPub(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("basic_publisher") # type: ignore # MODIFY NAME 
        self.publisher = self.create_publisher(String, "basic_pub", 10)
        self.timer = self.create_timer(0.5, self.publish_basic)
        self.get_logger().info("Basic Publisher has started")

    def publish_basic(self):
        msg = String()
        msg.data = ("hi, this is C1PH3r, with this basic publisher")
        self.publisher.publish(msg)

 
 
def main(args=None):
    rclpy.init(args=args)
    node = BasicPub() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()