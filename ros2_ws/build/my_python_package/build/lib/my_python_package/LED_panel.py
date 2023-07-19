#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import LEDStatusArray
from my_robot_interfaces.srv import SetLED


class LedPanelNode(Node):
    def __init__(self):
        super().__init__("led_panel")  # type: ignore
        self.led_Status = [0, 0, 0]
        self.led_status_publisher = self.create_publisher(
            LEDStatusArray, "led_status", 10)
        self.set_led_service = self.create_service(
            SetLED, "set_led", self.callback_Set_LED)
        self.Led_status_timer = self.create_timer(5, self.publish_led_Status)
        self.get_logger().info("LED Panel has started")

    def publish_led_Status(self):
        msg = LEDStatusArray()
        msg.led_status = self.led_Status
        self.led_status_publisher.publish(msg)

    def callback_Set_LED(self, request, response):
        led_number = request.led_number
        status = request.status

        if led_number > len(self.led_Status) or led_number <= 0:
            response.success = False
            return response

        if status not in [0, 1]:
            response.success = False
            return response

        self.led_Status[led_number - 1] = status
        response.success = True
        self.publish_led_Status()
        return response

def main(args=None):
    rclpy.init(args=args)
    node = LedPanelNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
