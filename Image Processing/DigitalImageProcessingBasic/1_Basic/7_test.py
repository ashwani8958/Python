import os, sys
from PIL import Image, ImageFilter
from matplotlib import pyplot as plt
import numpy as np


with Image.open('./images/face.jpg') as im:
    im = im.convert('L')

# Convert into -ve Image
# im = np.array(im)
# im = 255 - im
# im = Image.fromarray(im)

# size = (100, 100, 400, 400)

im = im.filter(ImageFilter.FIND_EDGES)
# im = im.filter(ImageFilter.CONTOUR)
# region = im.crop(size)
# region = im.transpose(Image.ROTATE_180)

plt.imshow(im, cmap = 'gray')
plt.show()
