import cv2
import numpy as np
import time

print("""  GOING INVISIBLE!!  """)

cap = cv2.VideoCapture(0) #initiates camera launch and capturing
time.sleep(3)             #time for camera
background = 0           #setting up background
for i in range(30):
    ret, background = cap.read()  #getting the background image

background = np.flip(background, axis=1)       #lateral flip, optional

while (cap.isOpened()):    #image opens
    ret, img = cap.read()


    img = np.flip(img, axis=1)                          # Flipping the image (Can be uncommented if needed)


    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)                # Converting image to HSV color space.
    value = (35, 35)

    blurred = cv2.GaussianBlur(hsv, value, 0)


    lower_red = np.array([0, 120, 70])                      # Defining lower range for red color detection.
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)


    lower_red = np.array([170, 120, 70])                     # Defining upper range for red color detection
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)


    mask = mask1 + mask2                    # Addition of the two masks to generate the final mask.
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))


    img[np.where(mask == 255)] = background[np.where(mask == 255)]       # Replacing pixels corresponding to cloak with the background pixels.
    cv2.imshow('Display', img)
    k = cv2.waitKey(10)
    if k == ord("t"):
        break