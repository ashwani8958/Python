
# from scipy import ndimage,misc
import cv2
from skimage import filters, img_as_ubyte, img_as_int
from PIL import Image
from scipy import ndimage
from pylab import *
import numpy as np

# 1st Method
a = Image.open('../images/profile.jpg')
b = filters.prewitt(a)

imshow(b, cmap = 'gray')
show()

# Line from 18 to 22 are the part of Method 1 and are not working
# # Bulid image from nd array
# b = Image.fromarray(b)
#
# # b = scipy.misc.toimage(b) # old method removed from new SCIPY library version
# b.save('../images/moon_prewitt.jpg')



# 2nd Method
# moon = cv2.imread('../images/moon.jpg', 0) # zero to convert to grayscale
# img = img_as_int(moon) # convert image to interger
#
# prewittVertical = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype = 'float64')
#
# prewittVertical_out = img_as_ubyte(ndimage.convolve(img, prewittVertical, mode = 'constant', cval = 0.0))
#
# imshow(prewittVertical_out, cmap = 'gray')
# show()
