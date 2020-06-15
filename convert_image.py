import os
import numpy as np 
import nibabel as nib
import sys
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage 
import med2image as m2i

def convert(xyz):
	myimg = xyz;

	img = nib.load(myimg)
	imgU16 = img.get_data().astype(np.float64)

	os.popen('med2image -i ' + xyz + ' -o ' + xyz + '_jpg.jpg -s m') 
# get middle slice

def main(argv):
   inputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:",["ifile="])
      elif opt in ("-i", "--ifile"):
         inputfile = arg

if __name__ == '__main__':
	x = main(sys.argv[1:])
	convert(x)