"""
main.py: Main python script for the piUnity project.  

This script creates a UDP socket between a Raspberry Pi (outfitted with a Sense hat)
and blasts the orientation data over to a Unity application.

"""

__author__  = 'Erik Fredericks'
__version__ = '0.1'

import socket
import argparse
from sense_hat import SenseHat

# Initialize sense hat and arguments
sh = SenseHat()

# Handle arguments
parser = argparse.ArgumentParser(description="piUnity Sensor Controller")
parser.add_argument("--ip", required=True)
parser.add_argument("--port", required=True, type=int)
parser.add_argument("--debug", action="store_true")
args = parser.parse_args()


# Setup socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket created - {0}:{1}".format(args.ip, args.port))

# Run forever!
while True:
  try:
    orientation = sh.get_orientation()
    txData = "{roll};{pitch};{yaw}".format(**orientation)#gyro)
    sock.sendto(bytes(txData, "utf-8"), (args.ip, args.port))

    if args.debug:
      print("Sending [{0}] to [{1}:{2}]".format(txData, args.ip, args.port))

  except Exception as e:
    print("Error: {0}".format(e))
    sock.close()
    break
