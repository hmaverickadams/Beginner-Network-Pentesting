#!/bin/python

import re
import sys
from datetime import datetime as dt
from pathlib import Path

bol = False

if len(sys.argv) != 2 :
	print("Syntax error")
	print("Syntax --  breach-parse <domain name> <file_name>  ")
	
else:
	datafolder= Path("/root/Documents/Breach-parse/")
	fopen = datafolder/"new.txt"
	f= open(fopen)
	domain = sys.argv[1]
	for line in f:
		if re.search(domain,line):
			bol = True
			passw = line.split('::')[1]
			print("Domain {} , Password: {} ".format(line.split('::')[0],passw))

if bol == False:
	print("No Domain exists similar to what u wrote")		
		
