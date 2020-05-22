import scipy.misc
import scipy.ndimage
from PIL import Image

a  = Image.open('../images/lena512.bmp')

b = scipy.ndimage.filters.minimum_filter(a,size=5, footprint = None, output = None, mode= 'reflect', cval =0.0,origin =0)

b = Image.fromarray(b)
# b = scipy.misc.toimage(b)

b.show()
