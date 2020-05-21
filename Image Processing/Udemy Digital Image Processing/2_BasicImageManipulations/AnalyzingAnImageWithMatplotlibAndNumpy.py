import numpy as np
import matplotlib.pyplot as plt

A = plt.imread('images/profile.jpg')
#print(A)
print(np.shape(A))
print(type(A))
print(A.dtype)
plt.imshow(A)
plt.show()
