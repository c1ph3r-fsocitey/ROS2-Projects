#include "rclcpp/rclcpp.hpp"
#include "my_robot_interfaces/msg/led_status_array.hpp"
#include "my_robot_interfaces/srv/set_led.hpp"

class LedPanelNode : public rclcpp::Node
{
public:
    LedPanelNode() : Node("led_panel")
    {
        this->declare_parameter("led_status", std::vector<int64_t>{0, 0, 0});
        led_status = this->get_parameter("led_status").as_integer_array();
        
        led_status_publisher_ =
            this->create_publisher<my_robot_interfaces::msg::LEDStatusArray>("led_states", 10);
        led_status_timer_ =
            this->create_wall_timer(std::chrono::seconds(4),
                                    std::bind(&LedPanelNode::publishLedStates, this));
        set_led_service_ = this->create_service<my_robot_interfaces::srv::SetLED>(
            "set_led",
            std::bind(&LedPanelNode::callbackSetLed, this, std::placeholders::_1, std::placeholders::_2));
        RCLCPP_INFO(this->get_logger(), "Led panel node has been started");
    }

private:
    void publishLedStates()
    {
        auto msg = my_robot_interfaces::msg::LEDStatusArray();
        msg.led_status = led_status;
        led_status_publisher_->publish(msg);
    }

    void callbackSetLed(const my_robot_interfaces::srv::SetLED::Request::SharedPtr request,
                        const my_robot_interfaces::srv::SetLED::Response::SharedPtr response)
    {
        int64_t led_number = request->led_number;
        int64_t state = request->status;

        if (led_number > (int64_t)led_status.size() || led_number <= 0)
        {
            response->success = false;
            return;
        }

        if (state != 0 && state != 1)
        {
            response->success = false;
            return;
        }

        led_status.at(led_number - 1) = state;
        response->success = true;
        publishLedStates();
    }

    std::vector<int64_t> led_status;

    rclcpp::Publisher<my_robot_interfaces::msg::LEDStatusArray>::SharedPtr led_status_publisher_;
    rclcpp::TimerBase::SharedPtr led_status_timer_;
    rclcpp::Service<my_robot_interfaces::srv::SetLED>::SharedPtr set_led_service_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<LedPanelNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
