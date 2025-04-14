import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = cv2.imread("assets_data/New_Zealand_Coast.jpg", cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

"""ADDITION OR BRIGHTNESS"""

# The results in increasing or decreasing the brightness of the image

matrix = np.ones(img_rgb.shape, dtype="uint8") * 50

img_rgb_brighter = cv2.add(img_rgb, matrix)
img_rgb_darker = cv2.subtract(img_rgb, matrix)

# Show the images
plt.figure(figsize=[18, 5])
plt.subplot(131); plt.imshow(img_rgb_brighter); plt.title('Brighter')
plt.subplot(132); plt.imshow(img_rgb); plt.title("Original")
plt.subplot(133); plt.imshow(img_rgb_darker); plt.title("Darker")

plt.show()

"""MULTIPLICATION OR CONTRAST"""

matrix1 = np.ones(img_rgb.shape)*0.8
matrix2 = np.ones(img_rgb.shape)*1.2

img_rgb_dark = np.uint8(cv2.multiply(np.float64(img_rgb), matrix1))
img_rgb_bright = np.uint8(cv2.multiply(np.float64(img_rgb), matrix2))

plt.figure(figsize=[18,5])
plt.subplot(121); plt.imshow(img_rgb_dark); plt.title("Lower contrast")
plt.subplot(122); plt.imshow(img_rgb); plt.title("Original")
plt.subplot(123); plt.imshow(img_rgb_bright); plt.title("Higher Contrast")
plt.show()

"""IMAGE THRESHOLDING"""

# Change the gray image (grayscale) into binary image (black: 0 and white: 1 or 255)

# Object Segmentation; Create mask...

# Syntax: retval, dst = cv2.threshold( src, thresh, maxval, type[, dst] )
# src: input image
# thresh: threshold value.
# maxval: maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types.
# type: thresholding type

img_read = cv2.imread("assets_data/building-windows.jpg", cv2.IMREAD_GRAYSCALE)
retval, img_thresh = cv2.threshold(img_read, 100, 255, cv2.THRESH_BINARY)

plt.figure(figsize=[10,5])
plt.subplot(121); plt.imshow(img_read, cmap="gray"); plt.title("Original")
plt.subplot(122); plt.imshow(img_thresh, cmap="gray"); plt.title("Threshold")
plt.axis("off")
plt.show()

""""""