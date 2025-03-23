# import libraries
import os
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Convert BGR to HSV
img_hsv=cv2.imread('assets_data/New_Zealand_Lake.jpg', cv2.COLOR_BGR2HSV)

# Split the image into the B,G,R components
h,s,v = cv2.split(img_hsv)

# Show the channels
plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(h, cmap="gray");plt.title("H Channel")
plt.subplot(142);plt.imshow(s, cmap="gray");plt.title("S Channel")
plt.subplot(143);plt.imshow(v, cmap="gray");plt.title("V Channel")

plt.show()