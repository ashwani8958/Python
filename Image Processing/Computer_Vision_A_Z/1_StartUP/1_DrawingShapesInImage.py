import cv2
import matplotlib.pyplot as plt
import numpy as np

# Create a blank image
BlankImg = np.zeros(shape=(512, 512, 3), dtype=np.int16)

# Rectangle in image
# Pt1 Vertex of the rectangle, Pt2 Vertex of the rectangle opposite to Pt1
cv2.rectangle(img=BlankImg, pt1=(384, 0), pt2=(510, 128), color=(0, 255, 0), thickness=5)
cv2.rectangle(img=BlankImg, pt1=(200, 200), pt2=(300, 300), color=(255, 0, 0), thickness=5)

# Circle in image
cv2.circle(img=BlankImg, center=(100, 100), radius=50, color=(0, 0, 255), thickness=5)
cv2.circle(img=BlankImg, center=(400, 400), radius=50, color=(0, 0, 255), thickness=-1)  # solid circle

# Line in image
cv2.line(img=BlankImg, pt1=(0, 0), pt2=(511, 511), color=(102, 255, 255), thickness=5)

# Write text in image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img=BlankImg, text='Hello', org=(10, 500), fontFace=font, fontScale=4, color=(255, 255, 255), thickness=2,
            lineType=cv2.LINE_AA)

# Draw polygons
# Create a blank image
BlankImg2 = np.zeros(shape=(512, 512, 3), dtype=np.int16)
vertices = np.array([[100, 300], [200, 200], [400, 300], [200, 400]], np.int32)
pts = vertices.reshape((-1, 1, 2))
cv2.polylines(BlankImg2, [pts], isClosed=True, color=(255, 0, 0), thickness=5)

plt.figure(figsize=(5, 5))

# Show image
plt.subplot(1, 2, 1)
plt.imshow(BlankImg)
plt.title("Blank Image 1")

plt.subplot(1, 2, 2)
plt.imshow(BlankImg2)
plt.title("Blank Image 1")

plt.show()
