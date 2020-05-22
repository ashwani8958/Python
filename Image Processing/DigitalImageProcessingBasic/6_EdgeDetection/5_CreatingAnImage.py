import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


# Image is describe as pixel value from 0 to 255
# Image size of 300 x 300
x = np.random.randint(0,255,(300,300)).astype('uint8')
# plt.imshow(x,cmap = cm.gray)

# Image is describe as pixel value from 0 to 255
# Image size of 300 x 400 as RGB as three channel therefore 3
y  = np.random.randint(0,255,(300,400,3)).astype('uint8')

plt.title("Y")
plt.imshow(y)
plt.show()

plt.title("X")
plt.imshow(y)
plt.show()
