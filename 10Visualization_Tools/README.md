The first tool we will use is called Orvis, which is a3d visualization tool to run it.
Let's open a new terminal and run rviz2.

When it opens, we can see a series of panels, so go ahead and maximize the window.
This main dark colored section is actually a3d view window.
If we had any sensor, data, localization data or robot transform data, we would be able to see it
here.One of the things I like to use it in the past was for visualizing three D LiDAR data, which is a point
cloud showing the distance surfaces are from the lidar.The left pane is where we can add and manage our sensors and other visualization parameters.
So click on the add button.We'll open up this dialog window where we can either add a sensor by type or a corresponding topic name.
<p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/vizulization3.png?raw=true"alt="Sublime's custom image"/>
 </p>
<p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/vizulization4.png?raw=true"alt="Sublime's custom image"/>
 </p>

Another useful feature for checking interactions between nodes is the Node graph plugin.
And here we see the Rosberg player is publishing to fix, and that's because here in our topic Monitor
we're subscribing to it.

<p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/vizulization2.png?raw=true"alt="Sublime's custom image"/>
 </p>
<p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/vizulization1.png?raw=true"alt="Sublime's custom image"/>
 </p>
