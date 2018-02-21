#!/usr/bin/env python
import sys

key_actuel= None
value_actuel = 0
key = None

for ligne in sys.stdin:
	ligne=ligne.strip()
	key,value=ligne.split()
	if key_actuel==key:
		value_actuel.append(value)
    	else:
	    	if key_actuel:
	    		print '%s\t%s\t%s' % (key_actuel,1/float(75000),value_actuel)
	    	key_actuel=key
	    	value_actuel=[value]
if key_actuel==key:
	print '%s\t%s\t%s' % (key_actuel,1/float(75000),value_actuel)