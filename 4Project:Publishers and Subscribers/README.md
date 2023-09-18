The project scenario is this we have a mobile robot with wheels of a certain radius.
One of the wheels has a rotary encoder sensor on it, which outputs how many rotations per minute.
The wheel is rotating.For this project, we will keep it simple and say the robot is going at a constant speed.
The first node that we create is a publisher node, which publishes to a topic named RPM with the sensor value that we are going to be publishing,
in this case, a constant value of your choice.
Now, we have no idea how fast the robot is actually going on this.we take into account the size of its wheels, so we to create a second node which subscribes
to the RPM topic calculates the speed the robot is going based on its wheel size and then publishes a result to the topic called speed.
<p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/projict11.png?raw=true"alt="Sublime's custom image"/>
 </p>

 In this project, you will create two nodes, one which publishes a value simulating rotations per minute of the robot wheel spinning and a second script which subscribes to this value, and then goes ahead
and publishes the calculated speed of the robot. You should be able to run these two nodes in two separate terminals to get your corresponding output.
<p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/projict12.png?raw=true"alt="Sublime's custom image"/>
 </p>

 ## Terminal Output
 <p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/projict14.png?raw=true"alt="Sublime's custom image"/>
 </p>

