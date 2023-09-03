#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
 
class AddTwoIntsServer(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("add_two_ints") # type: ignore # MODIFY NAME 
        self.server = self.create_service(AddTwoInts, "add_two_ints", self.addition_callback)
        self.get_logger().info("Add Two Ints Server has been started")

    def addition_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(str(response.sum))
        return response
 
def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsServer() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()