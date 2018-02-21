#!/usr/bin/env python
import sys

s=0
key_actuel= None
value_actuel = 0
key = None
out_actuel=0
out=0

for ligne in sys.stdin:
	ligne=ligne.strip()
	key,value=ligne.split('\t',1)
	try:
		value=float(value)
	except ValueError:
		value=eval(value)
		if len(value)==1:
			value=0
		else:
			value=value[1]
	if key_actuel==key:
		if type(value) is float:
			s+=value
		else:
			out_actuel=value
	else:
		if key_actuel:
			print '%s\t%s' % (key_actuel,0.15/float(75879)+0.85*s)
		key_actuel=key
		if type(value) is float:
			s=value
			out_actuel=0
		else:
			s=0
			out_actuel=value
		

if key_actuel==key:
	print '%s\t%s' % (key_actuel,0.15/float(75879)+0.85*s)