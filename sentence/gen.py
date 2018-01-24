from __future__ import print_function
import os
import re
from argparse import ArgumentParser

def main(in_file):

	try:
		open('gendata/snt.txt','w').close()
		open('gendata/par.txt','w').close()

	except Exception as e:
		print("Error in clearning data from 'gendata': No data cleared:")


	with open(in_file,'r') as infile:
		for line in infile:
			if line == '\n':
				pass

			
			par = ""
			snt = ""

			par =  re.sub(r'[^\x00-\x7F]+',' ', line) 

			if par[-1] != '\n':
				par = par + '\n'

			snt =  par.replace(".",".\n")
			snt = snt.replace("\n ", "\n")
			if snt[-1] == '\n':
				snt = snt[:-1]

			n = snt.count('\n') 
			
				
			with open('gendata/snt.txt','a') as f_snt:
				f_snt.writelines(snt)
			with open('gendata/par.txt', 'a') as f_par:
				for i in range(n):
					f_par.writelines(par)







if __name__ == "__main__":
	parser = ArgumentParser()
	parser.add_argument("-i", "-input", dest="in_file")
	args = parser.parse_args()

	main(args.in_file)