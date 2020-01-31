# importing Host from comms-python framework
import sys
sys.path.append('/home/kai/comms-python')
from Host import Host


# make a class that extends Host
class Receiver(Host):

	# override the name attribute (should match this module's name in the configs)    
	name = 'receiver'

	# override the run method (treat this as the starting point of your script)	
	def run(self):
		msg = self.node.recv_simple('example-topic')
		print("Message received:")
		print(msg)
