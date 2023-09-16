
In this chapter, we will see how to use the ROS client Library Python API to create a publisher node.
We imported the ROS client library, node class and string message types.

Then we created our own class, which is based off of the ROS client libraries Node object.
We then use the super init call to initialize our node with a node name.
We then use the create publisher function, which takes in the message type, topic, name and queue size.
And lastly, we utilize a create timer function to run a callback function at a particular rate.
<p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/ros%20publisher2.png?raw=true"alt="Sublime's custom image"/>
 </p>

We then loaded the data attribute of it with the data we wanted to send.
Then we call the publish function of our publisher variable, which takes in the message object and publishes it over Ros.
Lastly, within our main function we initialize our ROS communications and use the spin function to keep the node running.
