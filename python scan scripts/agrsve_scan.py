# !/bin/python

import sys
from datetime import datetime
import re
import nmap  
import socket

open_ports = []
start = 440
end = 443
target = socket.gethostbyname(sys.argv[1])
print("Starting Scan : " +str(datetime.now()))
if len(sys.argv) == 3:
	print("Syntax error")
	print("Syntax ---- python3 ultimatescan.py <ip>")

try:
	for port in range(start,end+1):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			#print("h")
			open_ports.append(port)	
		s.close()
		#print("h")

except KeyboardInterrupt:
	print("Exiting the scan")
	sys.exit()

except socket.gaierror:
	print("Host could not be resolved")
	sys.exit()

except socket.error:
	print("Could not connect to the server")
	sys.exit()				 



def port_scan(target):
        host = target
        nm = nmap.PortScanner()
        state = 'scanning'
        try:
            nm.scan(host) #arguments='-T5 -p 1-65535 -sV -sT -Pn --host-timeout 3600'
            #ports = nm[host]['tcp'].keys()
            #report_list = []
            for port in open_ports:
                #report = {}
                state = nm[host]['tcp'][port]['state']
                service = nm[host]['tcp'][port]['name']
                product = nm[host]['tcp'][port]['product']
                print("The state is {} , service : {} , product : {} ".format(state,service,product))
                print("\n")
            
        except Exception as e:
            print(e)

port_scan(target)
	
print("End time : "+str(datetime.now()))	
	
	
	
	
	
	
	
	
	
	
		
