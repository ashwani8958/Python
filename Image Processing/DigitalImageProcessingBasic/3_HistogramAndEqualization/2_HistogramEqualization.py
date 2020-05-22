import numpy as np
import scipy.misc, math
from PIL import Image

img = Image.open('../images/lena512.bmp')

# Line 9 is used to fix the error thrown by Line 8
# img1 = scipy.misc.fromimage(imag)
img1 = np.array(img)

# Remember the image is a two dimensional array but we need to flatten it into a 1D because
# histogram function accept 1D arrays as its input
fl = img1.flatten()
hist, bins = np.histogram(img1,256,[0,255])

# cumulative distribution function
cdf = hist.cumsum()

# After that we're going to make sure that places where the cumulative distribution
# function is 0 are ignored and then we store the rest in a new variable
cdf_m = np.ma.masked_equal(cdf,0)

# Once that is done we begin with the equalization, calculate numerator and denominator
num_cdf_m = (cdf_m - cdf_m.min())*255
den_cdf_m  = (cdf_m.max()-cdf_m.min())

cdf_m  = num_cdf_m / den_cdf_m

# Now we'll make sure the masked places are zero
cdf = np.ma.filled(cdf_m,0).astype('uint8')

# Once that is done we assigned a CDF values to the flattened array the one dimensional array
im2 = cdf[fl]

# 1D array is converted to two dimensional array
im3 = np.reshape(im2,img1.shape)

# Line 40 is used to fix the error thrown by Line 39
# im4 = scipy.misc.toimage(im3)
im4 = Image.fromarray(im3)

im4.show()
