import cv2
import numpy as np
from matplotlib import pyplot as plt

img  = cv2.imread('../images/profile.jpg')

# -1 as 2nd parameter mean output image has same depth as input image
v2.Laplacian(img,-1)

plt.imshow(output)
plt.show()
