Till now we have been running all of our rosters nodes independently, with each node needing its own dedicated terminal to run.
We have also had to open extra terminals to do actions such as setting parameters.
Launch files are a feature in ROS which allow you to launch multiple nodes and configure them all with a single command.

We created our launch files in Python by importing the launch description node and execute process objects from the different launch modules and then utilize them within our launch files. Generate Launch Description function. In the lunch description, we were able to run our Ros nodes we created using the node object and specifying the package and executable name. We can then also pass in a node name which will override the default node name specified in the code.
we can even specify values of particular parameters of that node. We also took a look at the execute process instance in which we can run terminal commands utilizing
our launch file and we specify output to screen so that the output of these commands can be seen on the terminal.
<p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/launch2.png?raw=true"alt="Sublime's custom image"/>
 </p>

## Terminal Output
<p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/launch1.png?raw=true"alt="Sublime's custom image"/>
 </p>
