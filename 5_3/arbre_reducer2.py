#!/usr/bin/env python
from operator import itemgetter
import sys

famille_actuel= None
comptage_actuel = 0
famille = None
annee_min=2018
borough_old=0

for ligne in sys.stdin:
	ligne = ligne.strip()
	famille,comptage,hauteur,annee,arron=ligne.split('\t',4)
	if annee!='':
		if annee_min>int(annee):
			annee_min=int(annee)
			borough_old=arron
	try:
		comptage=int(comptage)
		hauteur=float(hauteur)
	except ValueError:
	    	continue
	if famille_actuel==famille:
		comptage_actuel+=comptage
		if hauteur_actuelle<hauteur:
			hauteur_actuelle=hauteur
	else:
		if famille_actuel:
			print '%s\t%s\t%s' % (famille_actuel, comptage_actuel,hauteur_actuelle)
		comptage_actuel=comptage
		famille_actuel=famille
		hauteur_actuelle=hauteur

if famille_actuel==famille:
    print '%s\t%s\t%s' % (famille_actuel, comptage_actuel,hauteur_actuelle)

print '%s\t%s\t%s' % ("borough of the oldest tree in Paris and its age",borough_old,2018-annee_min)
