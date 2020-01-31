# imports for the starter code
import time
import multiprocessing as mp


# imports for the modules to test (edit for your own modules)
import sys
sys.path.append('/home/kai/comms-testing/example') # append path of directory containing each module
from Sender import Sender
from Receiver import Receiver

# config constants (change values for your own modules)
CONFIG = '../configs/example.json'
HOSTS = [Sender, Receiver]


# default starter code from here on
def starter(host, probe, trigger):
	x = host(CONFIG)
	probe.put('setup complete')
	while trigger.empty():
		pass
	x.run()

if __name__ == '__main__':
	probe = mp.Queue()
	trigger = mp.Queue()

	procs = []

	for host in HOSTS:
		proc = mp.Process(target=starter, args=(host, probe, trigger))
		procs.append(proc)

	for proc in procs:
		proc.start()

	for proc in procs:
		probe.get(block=True)
	
	time.sleep(1)
	trigger.put('all setup complete')

	for proc in procs:
		proc.join
