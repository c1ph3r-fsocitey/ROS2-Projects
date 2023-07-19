#include "rclcpp/rclcpp.hpp"
#include "my_robot_interfaces/msg/hardware_status.hpp"

class HardwareStatusPublisher : public rclcpp::Node // MODIFY NAME
{
public:
    HardwareStatusPublisher() : Node("hardware_status_publisher") // MODIFY NAME
    {
        pub = this->create_publisher<my_robot_interfaces::msg::HardwareStatus>("hardware_status", 10);
        timer = this->create_wall_timer(std::chrono::seconds(1), std::bind(&HardwareStatusPublisher::publish_hardware_status, this));
        RCLCPP_INFO(this->get_logger(), "hardware_publisher has started");
    }

private:
    void publish_hardware_status()
    {
        auto msg = my_robot_interfaces::msg::HardwareStatus();
        msg.temperature = 65;
        msg.are_motors_ready = false;
        msg.debug_message = "motors are too hot";
        pub->publish(msg);
    }
    rclcpp::Publisher<my_robot_interfaces::msg::HardwareStatus>::SharedPtr pub;
    rclcpp::TimerBase::SharedPtr timer;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<HardwareStatusPublisher>(); // MODIFY NAME
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}