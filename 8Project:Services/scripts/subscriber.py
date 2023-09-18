#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node 
from std_msgs.msg import String


class HelloWorldSubscriber(Node):
	def __init__(self):
		super().__init__("hello_world_sub_node")
		# create our subscriber.
        #I will just make a variable called sub and use the create subscription function from our node class.
		self.sub = self.create_subscription(String, "hello_world", self.subscriber_callback, 10)
        
		#subscriber_callback
		#This function will take in self and the message that comes in over the topic.
        
	def subscriber_callback(self, msg):
		#Once we receive the message, we are just going to print it to the terminal screen.
		print("Recieved: " + msg.data)


#This is our main function where we initialize our communication pipeline, create an instance of
#our subscriber class print that we are waiting for data to be published
def main(args=None):
	rclpy.init()
	my_sub = HelloWorldSubscriber()
	print("Waiting for data to be published...")

	try:
		rclpy.spin(my_sub)
	except KeyboardInterrupt:
		print("Terminating Node...")
		my_sub.destroy_node()


if __name__ == '__main__':
	main()