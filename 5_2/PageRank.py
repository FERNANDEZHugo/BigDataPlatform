#!/usr/bin/python
from mrjob.job import MRJob
from mrjob.step import MRStep

import sys


class Page_rank(MRJob):

	def steps(self):
		return [
		MRStep(mapper=self.mapper1,reducer=self.reducer1),
		MRStep(mapper=self.mapper2,reducer=self.reducer2),
		MRStep(mapper=self.mapper2,reducer=self.reducer2),
		MRStep(mapper=self.mapper2,reducer=self.reducer2),
		MRStep(mapper=self.mapper2,reducer=self.reducer2),
		MRStep(mapper=self.mapper2,reducer=self.reducer2),
		#MRStep(mapper=self.mapper2, reducer=self.reducer3)

		]

	def mapper1(self,_,line):
		ligne = line.strip()
		if ligne.split()[0]!='#':
			node_in,node_out = ligne.split()
			node_out=int(node_out)
			yield node_in, node_out

	def reducer1 (self,key,values):
		yield key,(1/float(75879),list(values))

	def mapper2(self,node_in,node_out):
		l=len(node_out[1])
		yield int(node_in), node_out
		for out in node_out[1]:
			yield out,node_out[0]/float(l)

	def reducer2 (self,key,values):
		s=0
		out=[]
		for val in list(values):
			if type(val) is float:
				s+=val
			else:
				out=val[1]
		yield key,(0.15/float(75879)+0.85*s,out)
		
		


if __name__ == '__main__':
	Page_rank.run()