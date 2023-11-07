from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    turtlesim_node = Node(
        package="turtlesim",
        executable="turtlesim_node"
    )
    Go_to_goal_=Node(
        package= "turtle_stimulation",
        executable="Go_to_goal_"

    )
    ld.add_action(turtlesim_node)
    ld.add_action(Go_to_goal_)

    return ld
    