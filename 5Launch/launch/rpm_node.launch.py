from launch import LaunchDescription
from launch_ros.actions import Node 
from launch.actions import ExecuteProcess
#In order for the ROS to launch command to interpret this python file, we will need to have a function
#called Generate Launch description in it, which returns a launch description object.
def generate_launch_description():
    return LaunchDescription([
        Node(
            package="udemy_ros2_pkg",
            executable="rpm_pub.py",
            name="rpm_pub_node"
        ), 
        ExecuteProcess(
            cmd=['ros2', 'topic', 'list'], 
            output="screen"
        )
    ])