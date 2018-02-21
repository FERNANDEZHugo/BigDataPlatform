#!/usr/bin/python
from operator import itemgetter
import sys
from math import log


mot_actuel= None
mot = None
N=2

for ligne in sys.stdin:
	ligne=ligne.strip()
	mot,freq,freq2,nbr_doc=ligne.split('\t',3)
	freq=float(freq)
	freq2=float(freq2)
	nbr_doc=float(nbr_doc)
	if mot_actuel:
		print '%s\t%s\t%s' % (mot_actuel, TFIDF_1,TFIDF_2)
	TFIDF_1=freq*log(N/nbr_doc)
	TFIDF_2=freq2*log(N/nbr_doc)
	mot_actuel=mot
if mot_actuel==mot:
    print '%s\t%s\t%s' % (mot_actuel, TFIDF_1,TFIDF_2)

