import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


x = np.random.randint(0,255,(300,300)).astype('uint8')
#plt.imshow(x,cmap = cm.gray)


y  = np.random.randint(0,255,(300,400,3)).astype('uint8')
plt.imshow(y)
plt.show()
