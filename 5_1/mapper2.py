#!/usr/bin/python
import sys
import nltk
for ligne in sys.stdin:
	ligne = ligne.strip()
	if ligne!='':
		print(ligne)