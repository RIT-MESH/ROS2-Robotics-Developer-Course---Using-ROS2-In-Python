In this project, we will create your own Ross service interface.
For this project, we will make two nodes one node which acts like a client, which sends a request
of an angle to a robot to turn a camera and another node which takes in the request and sends back a
response, which will be an image the robot takes after moving the camera to the angle specified.
Now, since we do not have a real robot, we're just going to have some pre taken images which are named by an angle and return one of these images
based on the request.

For this project, we will create two nodes a service client node and a service server node.
The service client node will send a service request of how many degrees to turn the camera to the service


server node.The server will then return the pre taken image data back to the client.


Then as an added feature, see if you can make your service client.
Display the image for the user to see.
In order to complete this task, I will use the OpenCV Library, which is a commonly used computer vision library.


