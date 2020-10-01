#!/bin/python3

import sys #sys usually used for taking arguments and exits
import socket
from datetime import datetime as dt

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #basically converts hostname to IPV4
else:
	print("Invalid Syntax")
	print("Give an arguments Syntax-- pyhton3 scanner.py <ip>")
	sys.exit()	

# Add a pretty banner

print("-" * 50)
print("Scanning target: " + target)
t1 = dt.now()
print("Time Started : " + str(t1))
print("-" * 50)

# Port Scanner
bol = False

try:
	for port in range(80,112):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		 # AF_net is for IPV4 and Sock Stream is for PORT
		socket.setdefaulttimeout(0.9) #it is a float
		print("Scanning the port {} ".format(port))
		result = s.connect_ex((target,port)) ## checks for error in while port scan
		if result == 0:
			bol = True
			print("The Scanned/Opened port is {} ".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("Exiting the scan")
	sys.exit()

except socket.gaierror:
	print("Host could not be resolved")
	sys.exit()

except socket.error:
	print("Could not connect to the server")
	sys.exit()					
if bol == False:
	print("No ports open.")	

t2 = dt.now()
print("-"* 50)
print("Time Latency : " + str(t2 -t1) + " secs")	
