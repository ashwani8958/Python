from PIL import Image
from PIL import ImageFilter
from pylab import *

# Load Image
im0  = Image.open('../images/moon.png')
gray()

# Setting Figure size
figure(figsize =(15,15))

# Subplot for plotting in the same plot
subplot(3,4,1)

# Plotting 1st images without any filters
plt.imshow(im0)
plt.title('Original')

# Plotting at the another slot
subplot(3,4,2)
im2 =  im0.filter(ImageFilter.CONTOUR) # With CONTOUR filter
plt.imshow(im2)
plt.title('Contour')

subplot(3,4,3)
im3 =  im0.filter(ImageFilter.DETAIL) # With DETAIL filter
plt.imshow(im3)
plt.title('Detail')

subplot(3,4,4)
im4  = im0.filter(ImageFilter.EDGE_ENHANCE) # With EDGE_ENHANCE filter
plt.imshow(im4)
plt.title('Edge Enhance')

subplot(3,4,5)
im5 = im0.filter(ImageFilter.EDGE_ENHANCE_MORE) # With EDGE_ENHANCE_MORE filter
plt.imshow(im5)
plt.title('Edge Enhance More')

subplot(3,4,6)
im6 = im0.filter(ImageFilter.EMBOSS) # With EMBOSS filter
plt.imshow(im6)
plt.title('Emboss')

subplot(3,4,7)
im7 =  im0.filter(ImageFilter.FIND_EDGES) # With FIND_EDGES Fliter
plt.imshow(im7)
plt.title('Find Edges')

subplot(3,4,8)
im8 =  im0.filter(ImageFilter.SMOOTH) # With SMOOTH lowpass Filter
plt.imshow(im8)
plt.title('Lowpass 1')

subplot(3,4,9)
im9 =  im0.filter(ImageFilter.SMOOTH_MORE) # With SMOOTH_MORE lowpass Filter
plt.imshow(im9)
plt.title('Lowpass 2')

subplot(3,4,10)
im10 = im0.filter(ImageFilter.SHARPEN) # With SHARPEN filter(high pass filter)
plt.imshow(im10)
plt.title('Sharpen')


#Custom kernels
size = (3,3)
kernel1  = [1,1,1,1,-1,1,-1,-1,-1]
ker1 =  ImageFilter.Kernel(size,kernel1,scale=None,offset =0) #With customer filter Setting
subplot(3,4,11)
im11  =  im0.filter(ker1)
plt.imshow(im11)
plt.title('Custom Filter 1')


kernel2 = [1,0,-1,1,0,-1,0,0,-1]
ker2 = ImageFilter.Kernel(size,kernel2,scale =None,offset=0) #With customer filter Setting
subplot(3,5,12)
im12 =  im0.filter(ker2)
plt.imshow(im12)
plt.title('Custom filter 2')

plt.show()
