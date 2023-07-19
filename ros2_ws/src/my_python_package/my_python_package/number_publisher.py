#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
 
 
class NumberPublisherNode(Node):
    def __init__(self):
        super().__init__("number_publisher") # type: ignore  \
        self.declare_parameter("number_to_publish", 2) #this is used to set a default value
        self.declare_parameter("publish_frequency", 1.0) 

        self.number = self.get_parameter("number_to_publish").value
        self.publish_frequency = self.get_parameter("publish_frequency").value

        self.publisher = self.create_publisher(Int64, "number", 10)
        self.number_timer = self.create_timer(1.0 / self.publish_frequency, self.number_publisher) # type: ignore
        
        self.get_logger().info("the number publisher has been started.")

    def number_publisher(self):
        msg = Int64()
        msg.data = self.number
        self.publisher.publish(msg)

 
def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()