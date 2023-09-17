we configure our packages so we can run our Python scripts using the ROS to run command for packages that use the cmake build type.
We configured the package xml file by including build tool dependencies for ament cmake, cmake python and rclpy.
<p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/configuration3.png?raw=true"alt="Sublime's custom image"/>
 </p>

we now configured our to make list text files where we used find package to include the same dependencies.
Then we set our scripts folder as our python package directory by using a ament python install package.
Remember that the folder must have an init script in it.Then we use the install programs to include each of our scripts and set the destination to lib slash
and the package name which we are able to call with the project name variable.
<p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/Configuration4.png?raw=true"alt="Sublime's custom image"/>
 </p>

We configured our Python files by telling the compiler how to run our scripts.
And once we did all of that, we were able to build source and run our python nodes using the ROS to run command.
We also took a look at how to configure our package XML and setup files.
<p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/Configuration5.png?raw=true"alt="Sublime's custom image"/>
 </p>

 ## Terminal output
 <p align="center"><img src="https://github.com/RIT-MESH/ROS2-Robotics-Developer-Course---Using-ROS2-In-Python/blob/main/images/Configuration1.png?raw=true"alt="Sublime's custom image"/>
 </p>
