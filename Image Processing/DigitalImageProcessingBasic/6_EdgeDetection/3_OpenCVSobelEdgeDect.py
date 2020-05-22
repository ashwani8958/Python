import cv2
import numpy as np
from matplotlib import pyplot as plt

img  = cv2.imread('../images/profile.jpg', 0) # 0 to convert image into grayscale

sobel_x  = cv2.Sobel(img,-1,1,0,ksize=5)
sobel_y  = cv2.Sobel(img,-1,0,1,ksize=5)

plt.title('Soble Y')
plt.imshow(sobel_y, cmap ='gray')
plt.show()

plt.title('Soble X')
plt.imshow(sobel_x, cmap ='gray')
plt.show()
