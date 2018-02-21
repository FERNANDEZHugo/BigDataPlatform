#!/usr/bin/env python
from operator import itemgetter
import sys

mot_actuel= None
freq = 0
mot = None
nbr_doc_actu=1
N=0
N_2=0

for ligne in sys.stdin:
	ligne=ligne.strip()
	mot,comptage,num_doc=ligne.split('\t',2)
	if mot=='111111':
		if N==0:
			N=int(comptage)
		else:
			N_2=int(comptage)

	try:
		comptage=int(comptage)
		num_doc=int(num_doc)
	except ValueError:
	    	continue
	if mot_actuel==mot:
		nbr_doc_actu+=1
		if num_doc==1:
			freq=float(comptage)/float(N)
		else:
			freq_2=float(comptage)/float(N)
	else :
		if mot_actuel:
			print '%s\t%s\t%s\t%s' % (mot_actuel, freq,freq_2,nbr_doc_actu)
		freq_2=0
		freq=0
		if num_doc==1:
			freq=float(comptage)/float(N)
		else:
			freq_2=float(comptage)/float(N)
		mot_actuel=mot
		nbr_doc_actu=1
		
if mot_actuel==mot:
    print '%s\t%s\t%s\t%s' % (mot_actuel, freq,freq_2,nbr_doc_actu)

