# Mean fliter generate the Blur image

from PIL import Image
import scipy.ndimage
import numpy as np

a = Image.open('../images/profile.jpg').convert('L')

# numpy.ones(shape, dtype=None, order='C') Return a new array of given shape and type, filled with ones.
k = np.ones((5,5))/25 # Creating 5 X 5 Mean filter kernel

# Apply convolve filter(Do convolution)
b = scipy.ndimage.filters.convolve(a,k)

# Bulid image from nd array
b = Image.fromarray(b)

# b = scipy.misc.toimage(b) # old method removed from new SCIPY library version
b.save('../images/mean_profile.jpg')
