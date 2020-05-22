import scipy.misc
import scipy.ndimage
from PIL import Image

a = Image.open('../images/lena_noisy.png')
b = scipy.ndimage.filters.median_filter(a,size=5, footprint= None,output=None, mode='reflect',cval=0.0,origin=0)

# Bulid image from nd array
b = Image.fromarray(b)

# b = scipy.misc.toimage(b)# old method removed from new SCIPY library version
b.save('../images/lena_median.png')
