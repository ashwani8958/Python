from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from pylab import *
from skimage import data

# Refer:- https://scikit-image.org/docs/dev/api/skimage.data.html#page
scanned =  data.page()

# plt.imshow(scanned, cmap =cm.gray)
# plt.show()


thres =  np.zeros(shape(scanned)).astype('uint8')

# set threshold, if pixel is below the threshold it will be converted in
# black pixel otherwise white
threshold = 150
thres[scanned <threshold] =0  #black pixel
thres[scanned >=threshold] = 255 #white pixel

plt.imshow(thres, cmap=cm.gray) # cmap=cm.gray will show the image in greyscale
plt.show()


# numpy.zeros(shape, dtype=float, order='C')
# Return a new array of given shape and type, filled with zeros.
#`
# Parameters
# 1) shape:- int or tuple of ints
#       Shape of the new array, e.g., (2, 3) or 2.
# 2) dtype:- data-type, optional
#       The desired data-type for the array, e.g., numpy.int8. Default is numpy.float64.
# 3) order:- {‘C’, ‘F’}, optional, default: ‘C’
#       Whether to store multi-dimensional data in row-major (C-style) or column-major (Fortran-style) order in memory.
# Returns
# out:- ndarray
# Array of zeros with the given shape, dtype, and order.
