#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class basicPublisher : public rclcpp::Node
{
public:
    basicPublisher() : Node("basic_publisher"), robot_name("c1ph3r")
    {
        publisher_ = this->create_publisher<example_interfaces::msg::String>("basic_pub", 10);
        timer_ = this->create_wall_timer(std::chrono::milliseconds(500),
                                         std::bind(&basicPublisher::basicPublish, this));
        RCLCPP_INFO(get_logger(), "This node has been started");
    }

private:
    void basicPublish()
    {
        auto msg = example_interfaces::msg::String();
        msg.data = "Welcome to basic publisher " + robot_name;
        publisher_->publish(msg);
    }

    std::string robot_name;
    rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<basicPublisher>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
