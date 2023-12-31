# ROS2-Robotics-Developer-Course---Using-ROS2-In-Python


## ROS 2 Simulation & Visualization Tools Overview
ROS also includes software suites to help with robotics simulation and data visualization. This article is just a quick overview so you are aware of these features. These software suites will be gone over in more detail later in the course.

### Simulation
- #### Gazebo
Gazebo is a free-to-use robot simulator which is able to communicate data over ROS2. It is able to keep track of robot positions, as well as mimic the state of a real robot. It includes virtual sensors which can be used to simulate real sensor data so that you are able to test your robot code as if you were running it on a physical robotic system.

Website: http://gazebosim.org/

<p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/ros1.png?raw=true"alt="Sublime's custom image"/>
</p>

### Visualization
- #### RViz2
 RViz2 is a 3D data visualization software suite which also interacts with data over ROS2. RViz2 comes with data visualization features, as well as other localization based tools for you to interact with your robot, especially of one in simulation.

Website: http://wiki.ros.org/rviz

<p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/ros2.png?raw=true"alt="Sublime's custom image"/>
</p>

- #### RQT
 RQT is plugin based graphical user interface to be used with ROS2. It comes with various graphical plugins, such as a topic publisher, image viewer, parameter updater, node graph visualizer, and much more. It is worth noting that RViz2 and RQT have certain features with both software suites can perform. RQT is focused more towards user interaction with ROS2, where RVIZ2 focuses on visualizing 3D data.

Website: http://wiki.ros.org/rqt  

<p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/ros3.png?raw=true"alt="Sublime's custom image"/>
</p>


### Extra Resources:
- http://design.ros2.org/articles/changes.html

- https://design.ros2.org/articles/ros_on_dds.html

- https://design.ros2.org/articles/ros2_access_control_policies.html

- https://github.com/ros2/ros1_bridge

## Create ROS2 Workspace
- Create workspace folder ***workspaces***
- Inside this folder create folder ***ros2-py-ws***
- Inside this folder create source folder ***src***
- Now open the terminal and typer the following commands
    1) cd workspaces/ros2_py_ws/src
    2) ros2 pkg create ros2_pkg --build-type ament-cmake
    3) inside the ros2_pkg folder create ***scripts*** folder
    4) cd ../
    5) now we are in ros2_py_ws type command ***colcon build***
    6) if got error then type this command ***sudo apt install python3-colcon-common-extensions***
    7) After that  to include our package in our terminal environment  ***source install/setup.bash***
    8) to check package list ***ros2 pkg list***
