

from skimage import filters
from PIL import Image
import scipy
from pylab import *

a = Image.open('../images/moon.jpg')
b = filters.sobel(a)

imshow(b)
show()

# # Bulid image from nd array
# b = Image.fromarray(b)
#
# # b = scipy.misc.toimage(b) # old method removed from new SCIPY library version
# b.save('../images/moon_sobel.jpg')
