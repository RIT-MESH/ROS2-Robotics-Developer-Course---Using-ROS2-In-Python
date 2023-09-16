Here we will  create subscribers in Python.
Within our node class we use the create subscription function to subscribe to a topic with a particular message type.
Every time data is published over that topic, a subscriber callback function runs.
This callback function takes in the message received over the topic where we can then process it.
In this lecture we just printed the data attribute of our string message, but you're free to process it however you want within your callback function.

<p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/subscriber2.png?raw=true"alt="Sublime's custom image"/>
 </p>

## Terminal output
<p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/subscriber1.png?raw=true"alt="Sublime's custom image"/>
 </p>
