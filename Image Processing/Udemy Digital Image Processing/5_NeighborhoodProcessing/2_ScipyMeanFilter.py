from PIL import Image
import scipy.ndimage
import numpy as np

a = Image.open('../images/profile.jpg').convert('L')

k = np.ones((5,5))/25
b = scipy.ndimage.filters.convolve(a,k)
b = Image.fromarray(b)

# b = scipy.misc.toimage(b)
b.save('../images/mean_profile.jpg')
