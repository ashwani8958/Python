import cv2
import numpy as np

# True if mouse is pressed
drawing = False
ix, iy = -1, -1


# Create a function to draw a circle based on the events
def DrawCircle(event, ptx, pty, flags, param):
    if cv2.EVENT_LBUTTONDOWN == event:
        cv2.circle(img=ImageCircle, center=(ptx, pty), radius=30, color=(0, 255, 0), thickness=-1)
    elif cv2.EVENT_RBUTTONDOWN == event:
        cv2.circle(img=ImageCircle, center=(ptx, pty), radius=30, color=(255, 0, 0), thickness=-1)


# Create a function to draw a rectangle based on the events
def DrawRectangle(event, ptx, pty, flags, param):
    global ix, iy, drawing
    if cv2.EVENT_LBUTTONDOWN == event:
        drawing = True  # click DOWN with left mouse button drawing is set to True
        ix, iy = ptx, pty  # Then take note of where that mouse was located

    elif cv2.EVENT_MOUSEMOVE == event:
        if drawing:  # Now the mouse is moving
            cv2.rectangle(ImageRectangle, (ix, iy), (ptx, pty), (0, 255, 0), -1)

    elif cv2.EVENT_LBUTTONUP == event:
        drawing = False
        cv2.rectangle(ImageRectangle, (ix, iy), (ptx, pty), (0, 255, 0), -1)


# Create a black image
ImageCircle = np.zeros(shape=(512, 512, 3), dtype=np.uint8)
ImageRectangle = np.zeros(shape=(512, 512, 3), dtype=np.uint8)

# Create named windows
cv2.namedWindow(winname='My Drawing Circles', flags=cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(winname='My Drawing Rectangle', flags=cv2.WINDOW_AUTOSIZE)
cv2.moveWindow(winname='My Drawing Circles', x=10, y=10)
cv2.moveWindow(winname='My Drawing Rectangle', x=550, y=10)

# Connects the mouse button to our callback function
cv2.setMouseCallback('My Drawing Circles', DrawCircle)
cv2.setMouseCallback('My Drawing Rectangle', DrawRectangle)

# Runs forever until we break with Esc key on keyboard
while True:
    cv2.imshow('My Drawing Circles', ImageCircle)
    cv2.imshow('My Drawing Rectangle', ImageRectangle)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
