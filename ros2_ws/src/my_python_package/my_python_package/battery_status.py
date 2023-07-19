#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLED
from functools import partial

class BatteryNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("battery") # type: ignore
        self.battery_status = "full"
        self.last_battery_check = self.get_current_time()
        self.battery_timer = self.create_timer(0.1, self.check_battery_status)
        self.get_logger().info("The Battery Node has been started")
    
    def get_current_time(self):
        secs, nanosecs = self.get_clock().now().seconds_nanoseconds() 
        return secs + nanosecs / 1000000000.0
    
    def check_battery_status(self):
        time_now = self.get_current_time()
        if self.battery_status == "full":
            if time_now - self.last_battery_check > 4.0:
                self.battery_status = "empty"
                self.get_logger().info("battery is empty! Charging Battery...")
                self.last_battery_check = time_now
                self.call_set_led_server(3, 1)

        else: 
            if time_now - self.last_battery_check > 6.0:
                self.battery_status = "full"
                self.get_logger().info("Battery has been fully charged")
                self.last_battery_check = time_now
                self.call_set_led_server(3, 0)
    
    def call_set_led_server(self, led_number, status):
        client = self.create_client(SetLED, "set_led")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for the service to be started...")

        request = SetLED.Request()
        request.led_number = led_number
        request.status = status

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_call_set_led, led_number = led_number, status = status))

    def callback_call_set_led(self, future, led_number, status):
        try:
            response = future.result()
            self.get_logger().info(str(response.success)) #type: ignore
        except Exception as e:
            self.get_logger().error("service call failed %r" % (e,))
 
def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()