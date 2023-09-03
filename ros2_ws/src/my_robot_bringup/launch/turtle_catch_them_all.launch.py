from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()

    turtlesim_node = Node(
        package='turtlesim',
        executable='turtlesim_node'
    )

    turtle_spawner_node = Node(
        package='turtle_catch_them_all',
        executable='turtle_spawner',
        parameters=[
            {"turtle_Spawn_frequency": 1.0},
            {"turtle_name": "turtle"}
        ]
    )

    turtle_controller_node = Node(
        package='turtle_catch_them_all',
        executable='turtle_controller',
        parameters=[
            {"catch_closest_turtle_first": True},
            {"turtle_speed": 5}
        ]
    )

    ld.add_action(turtlesim_node)
    ld.add_action(turtle_spawner_node)
    ld.add_action(turtle_controller_node)
    return ld