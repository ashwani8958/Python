from PIL import Image
from pylab import *

im = array(Image.open('../images/profile.jpg').convert('L'))

# if we want image to appear in greyscale
gray()

#negative image
im2 = 255 - im

# image should contain pixel with value between 100 to 200
im3 = (100.0/255) *im + 100 # Clamp to interval 100 ... 200

# square the pixel value
im4 = 255.0 *(im/255.0)**2

imshow(im4)

show();
