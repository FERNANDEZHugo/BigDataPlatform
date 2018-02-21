#!/usr/bin/env python
from operator import itemgetter
import sys

mot_actuel= None
comptage_actuel = 0
mot = None

for ligne in sys.stdin:
	ligne=ligne.strip()
	mot,comptage=ligne.split('\t',1)
	try:
		comptage=int(comptage)
	except ValueError:
        	continue
    	if mot_actuel==mot:
		comptage_actuel+=comptage
    	else:
	    	if mot_actuel:
	    		print '%s\t%s\t%s' % (mot_actuel, comptage_actuel,1)
	    	comptage_actuel=comptage
	    	mot_actuel=mot
if mot_actuel==mot:
    print '%s\t%s\t%s' % (mot_actuel, comptage_actuel,1)
