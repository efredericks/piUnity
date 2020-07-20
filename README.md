# piUnity

This script blasts out orientation data from a Raspberry Pi outfitted with a [Sense hat](https://www.raspberrypi.org/products/sense-hat/) to a Unity project.  The intent is to act as a network-based controller for *some* object.  

## Requirements

This was coded for Python 3, though I doubt there would be much of an issue running it in 2.  Ensure you have the correct modules installed (`argparse` and `sense-hat`).  The specific versions I used are provided in a requirements file.

`pip3 install -r requirements.txt`

## Running

The script takes the IP address, port, and debug flag as command line options.  IP and port are required.

Sample usage:

`python3 --ip 192.168.1.2 --port 50001`
