import numpy as np 
import nibabel as nib
import sys
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage 

img = nib.load()
imgU16 = img.get_data().astype(np.float64)

data = scipy.misc.imresize(imgU6,50,interp='bilinear',mode=None)

# midp = imgU16.len() / 2
# midp = math.floor(midp)
# midsamp = imgU16[midp-10:midp+10]
# data_nii = nib.Nifti1Image(midsamp,img.affine,img.header)


data_nii = nib.Nifti1Image(data,img.affine,img.header)
nib.save(data_nii,'')