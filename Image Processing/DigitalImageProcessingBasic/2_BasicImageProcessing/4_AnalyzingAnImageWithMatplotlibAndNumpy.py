import numpy as np
import matplotlib.pyplot as plt

A = plt.imread('../images/profile.jpg')
# print(A)

# NumPy arrays have an attribute called shape that returns a tuple
# with each index having the number of corresponding elements.
# (row, cow) i.e. (707, 749, 3)
print(np.shape(A))

# Print the data type of A i.e. <class 'numpy.ndarray'>
print(type(A))

# Print the data type of member of A i.e. uint8
print(A.dtype)

#build the
plt.imshow(A)
plt.show()
