#!/usr/bin/python
import sys
from string import punctuation

for ligne in sys.stdin:
    ligne = ligne.strip()
    geo,arron, genre,espece,famille,annee,hauteur,circon,adresse,nom,variete,objID,nom_EV = ligne.split(";")
    if famille!='FAMILLE':
    	print '%s\t%s\t%s\t%s\t%s' % (famille,1,hauteur,annee,arron)

