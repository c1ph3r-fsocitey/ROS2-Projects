#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/string.hpp"

class basicSubscriber : public rclcpp::Node // MODIFY NAME
{
public:
    basicSubscriber() : Node("basic_subscriber") // MODIFY NAME
    {
        subscriber_ = this->create_subscription<example_interfaces::msg::String>("basic_pub", 10,
                        std::bind(&basicSubscriber::callbackSubscriber, this, std::placeholders::_1));
            RCLCPP_INFO(get_logger(), "basic subscriber node started");                    
    }

private:
    void callbackSubscriber(const example_interfaces::msg::String::SharedPtr msg)
    {
        RCLCPP_INFO(this->get_logger(), "%s", msg->data.c_str());        
    }
    rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber_;

};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<basicSubscriber>(); // MODIFY NAME
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}