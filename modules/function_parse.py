#!/usr/bin/env python3

from math import *

def GetFunctionValue(function, x, y):
	try:
		value = eval(function.replace('x', str(x).replace('y', str(y))))
	except:
		print("Incorrect!")
		value = 0
	return value