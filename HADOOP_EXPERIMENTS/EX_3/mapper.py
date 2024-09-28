#!/usr/bin/env python3 
import sys 
for line in sys.stdin: 
line = line.strip() 
month = line[4:6] # Extracting month 
temp = line[7:11] # Extracting temperature 
print(f'{month}\t{temp}')
