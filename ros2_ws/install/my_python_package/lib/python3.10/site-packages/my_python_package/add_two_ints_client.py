#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

# a = int(input("enter a number: "))
# b = int(input("enter another number: "))

def main(args=None):
    rclpy.init(args=args)
    node = Node("add_two_ints_client")  # type: ignore
    
    client = node.create_client(AddTwoInts, "add_two_ints")
    while not client.wait_for_service(1.0):
        node.get_logger().warning("waiting for the service to start")

    request = AddTwoInts.Request()
    request.a =  int(input("enter a number: "))
    request.b = int(input("enter another number: "))


    future = client.call_async(request)
    rclpy.spin_until_future_complete(node, future)
    
    try:
        response = future.result()
        node.get_logger().info(str(response.sum)) #type: ignore
    except Exception as e:
        node.get_logger().error("service call failed %r" % (e,))
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()