#!/usr/bin/python
import sys
for ligne in sys.stdin:
	ligne = ligne.strip()
	ligne2=ligne.split()
	if ligne2[0]!='#':
		node_in,node_out = ligne.split()
		print '%s\t%s' % (node_in,node_out)