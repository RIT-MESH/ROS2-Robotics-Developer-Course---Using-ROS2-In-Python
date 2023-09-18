As you learned in the Ross two overview video, Ross actions is another inter node communication method.
Here in action goal is similar to a service request and an action result is similar to a service response.
The feedback aspect of an action is similar to a publisher in which it keeps publishing feedback relevant
to the state of the goal until a result is reached.

In this project walkthrough, we will program similar functionality shown in the Ross overview animation.
The project scenario is that we have a mobile camera robot and we want to send it to coordinates to
a goal point to navigate to.
<p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/project51.png?raw=true"alt="Sublime's custom image"/>
 </p>

While the robot is navigating, we want it to send feedback on how far away it is from the goal point.
When it reaches the goal, the robot then returns a result of how long it took to get to that goal point.
<p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/project52.png?raw=true"alt="Sublime's custom image"/>
 </p>

This is an ideal situation where we'd want to use a Ross action.
It has a goal aspect, feedback aspect and a result aspect to it.
<p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/project53.png?raw=true"alt="Sublime's custom image"/>
 </p>

An additional thing to note is we will also need to create a publisher to simulate a position senso
which tells us the current point the robot is at.
Our action will find the distance between the goal point and the simulated current position to send
feedback on how far the robot is from the goal.
