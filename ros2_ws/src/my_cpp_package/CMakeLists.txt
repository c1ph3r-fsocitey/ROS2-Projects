cmake_minimum_required(VERSION 3.5)
project(my_cpp_package)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_components REQUIRED)
find_package(rmw REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rmw_fastrtps_cpp QUIET)
find_package(example_interfaces REQUIRED)
find_package(my_robot_interfaces REQUIRED)

include_directories(include)

add_executable(cpp_node src/my_first_node.cpp)
ament_target_dependencies(cpp_node rclcpp)

add_executable(robot_news_station src/robot_news_station.cpp)
ament_target_dependencies(robot_news_station rclcpp example_interfaces)

add_executable(smartphone src/smartphone.cpp)
ament_target_dependencies(smartphone rclcpp example_interfaces)

add_executable(add_two_ints_server src/add_two_ints_server.cpp)
ament_target_dependencies(add_two_ints_server rclcpp example_interfaces)

add_executable(add_two_ints_client src/add_two_ints_client.cpp)
ament_target_dependencies(add_two_ints_client rclcpp example_interfaces)

add_executable(add_two_ints_client_oops src/add_two_ints_client_oops.cpp)
ament_target_dependencies(add_two_ints_client_oops rclcpp example_interfaces)

add_executable(hardware_status_publisher src/HardwareStatus.cpp)
ament_target_dependencies(hardware_status_publisher rclcpp example_interfaces my_robot_interfaces)

add_executable(basic_pub src/basic_pub.cpp)
ament_target_dependencies(basic_pub rclcpp example_interfaces)

add_executable(basic_sub src/basic_sub.cpp)
ament_target_dependencies(basic_sub rclcpp example_interfaces)

add_executable(LED_panel src/LED_panel.cpp)
ament_target_dependencies(LED_panel rclcpp my_robot_interfaces)

add_executable(battery src/battery.cpp)
ament_target_dependencies(battery rclcpp my_robot_interfaces)

add_executable(number_publisher src/number_publisher.cpp)
ament_target_dependencies(number_publisher rclcpp example_interfaces)

add_executable(number_counter src/number_counter.cpp)
ament_target_dependencies(number_counter rclcpp example_interfaces)


install(TARGETS
  cpp_node
  robot_news_station
  smartphone
  add_two_ints_server
  add_two_ints_client
  add_two_ints_client_oops
  hardware_status_publisher
  basic_pub
  basic_sub
  LED_panel
  battery
  number_counter
  number_publisher

  DESTINATION lib/${PROJECT_NAME}
)


ament_package()