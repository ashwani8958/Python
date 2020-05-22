from PIL import Image
from pylab import *

im = array(Image.open('../images/profile.jpg'))
imshow(im)

x = [100,150,300,400]
y = [50,500,200,500]

plot(x,y,'r*')


plot(x[:2],y[:2],'r')

plot(x[2:],y[2:],'ks:')

title('Plotting "Profile.jpg"')

show()
