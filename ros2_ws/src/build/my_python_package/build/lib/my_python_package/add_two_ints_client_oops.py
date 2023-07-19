#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
from functools import partial

a = int(input("enter a number: "))
b = int(input("enter another number: "))

class AddTwoIntsClientOops(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("Add_two_ints") # type: ignore # MODIFY NAME 
        self.call_add_two_ints_server(a, b)

    def call_add_two_ints_server(self, a, b):
        client = self.create_client(AddTwoInts, "add_two_ints")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for the service to be started...")

        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_call_add_two_ints, a=a, b=b))

    def callback_call_add_two_ints(self, future, a, b):
        try:
            response = future.result()
            self.get_logger().info(str(response.sum)) #type: ignore
        except Exception as e:
            self.get_logger().error("service call failed %r" % (e,))
 
 
def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClientOops() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()