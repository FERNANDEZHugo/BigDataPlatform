#!/usr/bin/python
import sys
from string import punctuation
i=0
for ligne in sys.stdin:
    ligne = ligne.strip()
    mots = ligne.split()
    for mot in mots:
		i+=1
		mot=mot.lower()
		mot=mot.strip('1234657890')
		mot=mot.strip(punctuation)
		if mot!='':
			print '%s\t%s' % (mot, 1)
print '%s\t%s' % ('111111', i)
