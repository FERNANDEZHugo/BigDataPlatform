#!/usr/bin/python
import sys
for ligne in sys.stdin:
	ligne = ligne.strip()
	key,value,out_node = ligne.split('\t',2)
	if out_node!='0':
		out_node=eval(out_node)
		l=len(out_node)
		value=float(value)
		print '%s\t%s' % (key,[value,out_node])
		for out in out_node:
			print '%s\t%s' % (out,value/float(l))
	else:
		print '%s\t%s' % (key,[value])