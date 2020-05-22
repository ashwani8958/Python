import math
import numpy
import scipy.misc
from PIL import Image

a = Image.open('../images/lena512.bmp')

# NOT WORKING LINE NO 9, Same work done by line 11
# b = scipy.misc.fromimage(a)

# convert to nD array from image
b = numpy.array(a)

gamma = 0.5

# convert b into float
b1 =  b.astype(float)

# Find maximum values in b1 data
b3 = numpy.max(b1)

# normalize the value
b2 = b1/b3

# compute gamma correction exponent
b3 = numpy.log(b2)*gamma

# gamma correction
c = numpy.exp(b3)*255.0

# NOT WORKING LINE NO 32 and 33, Same work done by line 36
# c1 = c.astype(int)
# d = scipy.misc.toimage(c1)

# convert from nD array to image
d = Image.fromarray(c)

d.show()
