#!/usr/bin/env python3 
import sys 
 
current_month = None 
current_max_temp = -float('inf') 
 
for line in sys.stdin: 
line = line.strip() 
month, temp = line.split('\t') 
210701270  
try: 
temp = float(temp) 
except ValueError: 
continue 
 
 
if current_month == month: 
current_max_temp = max(current_max_temp, temp) 
else: 
if current_month: 
print(f'{current_month}\t{current_max_temp}') 
current_month = month 
current_max_temp = temp 
 
if current_month == month: 
print(f'{current_month}\t{current_max_temp}') 
