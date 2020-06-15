import os
import numpy as np 
import sys
import matplotlib.pyplot as plt

def error_calc(file):
	with open('file',newline='') as csvfile:
		fileread = csv.reader(csvfile,delimiter=' ',quotechar='|')
		filewrite = csv.writer('error.csv',delimiter=' ',quotechar='|')
		for row in fileread:
			x = ((2-row)/2)*((2-row)/2)
			filewrite.writerow(x)

def main(argv):
   inputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:",["ifile="])
      elif opt in ("-i", "--ifile"):
         inputfile = arg

if __name__ == '__main__':
	x = main(sys.argv[1:])
	error_calc(x)