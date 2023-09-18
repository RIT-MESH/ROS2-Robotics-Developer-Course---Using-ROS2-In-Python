#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String

#The ROS client library contains a node class with all the different ROS functionality to implement in
#our code.So what we can do is create our own class which inherits all the functionality of that existing ROS
#node class.
class HelloWorldPublisher(Node): #Now I can pass this node class into our Hello world publisher for it to inherit it.
	def __init__(self):
		#And the first thing we will do is initialize the node.
        #So we will use Python's super function to gain access to the init method from that node object we inherited
        #from ROS client library.
		super().__init__("hello_world_pub_node")
		#Let's create our publisher.
		#The second parameter is the topic name we want to publish over.
        #I will just call it Hello World.
		self.pub = self.create_publisher(String, "hello_world", 10)
		#timer functionality was added to help  simplify this so we can create a timer variable and set it equal to our nodes.
        #Create timer function.
		#This function takes in two parameters the rate of our timer in seconds and the callback function We
        #want to run at that rate in this case, we're going to want to create a callback function to publish
        #our Hello world message.
		self.timer = self.create_timer(0.5, self.publish_hello_world)
		self.counter = 0
        
		#create hello world function
	def publish_hello_world(self):
		msg = String()
		msg.data = "Hello World " + str(self.counter)
		self.pub.publish(msg)
		self.counter += 1

def main(args=None):
	rclpy.init() #initializing ROS DDS function
	my_pub = HelloWorldPublisher()
	print("Publisher Node Running...")

    #To stop our Python scripts from finishing right after we create our My Pub variable, I will use
    #the ROS client library spin function, which we will run until there is a keyboard interrupt.
    #So I will wrap it in a try except statement like so.
	try:
		rclpy.spin(my_pub)
	except KeyboardInterrupt:
		print("Terminating Node...")
		#I'm going to want to stop my node by calling the destroy
        #node function.
		my_pub.destroy_node()


if __name__ == '__main__':
	main()