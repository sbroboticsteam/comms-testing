# importing Host from comms-python framework
import sys
sys.path.append('/home/kai/comms-python')
from Host import Host


# make a class that extends Host
class Sender(Host):

	# override the name attribute (should match this module's name in the configs)    
	name = 'sender'

	# override the run method (treat this as the starting point of your script)	
	def run(self):
		self.node.send('example-topic', "Hello")
