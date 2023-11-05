#!/usr/bin/env python3
import sys

if len(sys.argv) !=2:
	print('Invalid number of arguments!')
	sys.exit()
  
x = sys.argv[1]
if not x.isdigit():
	print('Not a number')
	sys.exit()

i = int(x)
print(hex(i))
print(bin(1))
