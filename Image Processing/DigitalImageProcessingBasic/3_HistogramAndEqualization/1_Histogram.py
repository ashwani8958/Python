from PIL import Image
from pylab import *

img = Image.open('../images/profile.jpg').convert('L')

# convert the image in the array
img_array = array(img)
#img.show()

#convert to histogram
figure()
hist(img_array.flatten(),500)

show()
