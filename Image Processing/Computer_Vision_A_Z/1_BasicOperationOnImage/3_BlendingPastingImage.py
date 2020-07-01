import cv2
import numpy as np

############################################################################################################
# CODE SECTION 1:- When Image is of same size or make image of same size before blending
############################################################################################################
DogImage = cv2.imread('../DATA/dog_backpack.png')
WatermarkImage = cv2.imread('../DATA/watermark_no_copy.png')

# Resize the image to same size so that overlap can happen
DogImage = cv2.resize(DogImage, (1200, 1200))
WatermarkImage = cv2.resize(WatermarkImage, (1200, 1200))

BlendedImage = cv2.addWeighted(src1=DogImage, alpha=0.7, src2=WatermarkImage, beta=0.3, gamma=0)

############################################################################################################
# CODE SECTION 2:- Overlaying Images of Different Size
############################################################################################################
DogImage = cv2.imread('../DATA/dog_backpack.png')
WatermarkImage = cv2.imread('../DATA/watermark_no_copy.png')

WatermarkImage = cv2.resize(WatermarkImage, (600, 600))
LargerImage = DogImage
SmallerImage = WatermarkImage

Xoffset = 0
Yoffset = 0

LargerImage[Yoffset:Yoffset+SmallerImage.shape[0], Xoffset:Xoffset+SmallerImage.shape[1]] = SmallerImage


############################################################################################################
# CODE SECTION 3:- Blending Images of Different Sizes
############################################################################################################

DogImage = cv2.imread('../DATA/dog_backpack.png')
WatermarkImage = cv2.imread('../DATA/watermark_no_copy.png')
WatermarkImage = cv2.resize(WatermarkImage, (600, 600))

# Create the Region of Interest(ROI), as the Shape of DogImage is (1401, 934, 3)
xOffset = 934 - 600
yOffset = 1401 - 600

# Creating an ROI of the same size of the foreground image (smaller image that will go on top)
rows, cols, channels = WatermarkImage.shape
ImageROI = DogImage[yOffset:1401, xOffset:934]

# Creating Mask
WatermarkImageGray = cv2.cvtColor(WatermarkImage, cv2.COLOR_RGB2GRAY)
MaskInversion = cv2.bitwise_not(WatermarkImageGray)

# Convert mask to have 3 channels
WhiteBackground = np.full(WatermarkImage.shape, 255, dtype=np.uint8)
Background = cv2.bitwise_or(WhiteBackground, WhiteBackground, mask=MaskInversion)
ForGround = cv2.bitwise_or(WatermarkImage, WatermarkImage, mask=MaskInversion)

FinalROI = cv2.bitwise_or(ImageROI, ForGround)
LargerImage1 = DogImage
SmallerImage1 = FinalROI

LargerImage1[yOffset:yOffset+SmallerImage1.shape[0], xOffset:xOffset+SmallerImage1.shape[1]] = SmallerImage1

# Create named windows
cv2.namedWindow(winname='Blending Same Size Image', flags=cv2.WINDOW_NORMAL)
cv2.namedWindow(winname='Overlaying Different Size Image', flags=cv2.WINDOW_NORMAL)
cv2.namedWindow(winname='Blending Images of Different Sizes', flags=cv2.WINDOW_NORMAL)
cv2.moveWindow(winname='Blending Same Size Image', x=10, y=10)
cv2.moveWindow(winname='Overlaying Different Size Image', x=430, y=10)
cv2.moveWindow(winname='Blending Images of Different Sizes', x=840, y=10)

# Show Images
cv2.imshow(winname='Blending Same Size Image', mat=BlendedImage)
cv2.imshow(winname='Overlaying Different Size Image', mat=LargerImage)
cv2.imshow(winname='Blending Images of Different Sizes', mat=LargerImage1)
cv2.waitKey(0)


