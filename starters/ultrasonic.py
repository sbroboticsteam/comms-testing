# imports for the starter code
import time
import multiprocessing as mp


# importing the modules to test
import sys
sys.path.append("/home/kai/SBRT_EE_COMMS/2019-2020-IARRC/I2C_Firmware/Ultrasonic")
from URM09 import Ultrasonic
from Test_Receiver import Test_Receiver

# constants (specific to the modules to test)
CONFIG = '../configs/ultrasonic.json'
HOSTS = [Ultrasonic, Test_Receiver]


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
