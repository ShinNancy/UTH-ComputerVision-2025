# import libraries
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Read image as a gray scale
cb_img = cv2.imread("assets_data/checkerboard_18x18.png", 0)

# Set color map to gray scale for proper rendering
plt.imshow(cb_img, cmap='gray')
# print(cb_img)

"""MODIFYING IMAGE PIXELS"""
# Modify the pixel values of the image
cb_image_copy = cb_img.copy()
cb_image_copy[2,2] = 200
cb_image_copy[2,3] = 200
cb_image_copy[3,2] = 200
cb_image_copy[3,3] = 200

# Same as above, but using slicing => cb_image_copy[2:3, 2:3] = 200

plt.imshow(cb_image_copy, cmap='gray')
# print(cb_image_copy)

"""------------------------------------------------------------------------------------------------------"""

"""CROPPING IMAGES"""

# Cropping an image is simply achieved by selecting a specific (pixel) region of the image.

img_NZ_bgr =  cv2.imread('assets_data/New_Zealand_Boat.jpg', cv2.IMREAD_COLOR)
img_NZ_rgb = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2RGB)

cropped_img_region = img_NZ_rgb[200:400, 300:600]
plt.imshow(cropped_img_region)

# plt.imshow(img_NZ_rgb)
print(img_NZ_rgb)
plt.axis('off')
plt.show()

"""------------------------------------------------------------------------------------------------------"""

"""RESIZING IMAGES"""

# Resizing an image is achieved by changing the dimensions of the image.
# The dimensions can be changed by specifying the width and height of the image.
# Syntax: dst = resize( src, dsize[, dst[, fx[, fy[, interpolation]]]] )
# src: input image
# dsize: output image size
# fx: scale factor along the horizontal axis
# fy: scale factor along the vertical axis
# interpolation: interpolation method

# Method 1: Specifying Scaling Factor using fx and fy

img_NZ_bgr = cv2.imread('assets_data/New_Zealand_Boat.jpg', cv2.IMREAD_COLOR)
resize_img = cv2.resize(img_NZ_bgr, None, fx=0.5, fy=0.5)

cv2.imshow('Resized Image', resize_img)
cv2.waitKey(0)

# Method 2: Specifying Output Image Size
resize_img_2 = cv2.resize(img_NZ_bgr, (200, 200))
cv2.imshow('Resized Image 2', resize_img_2)
cv2.waitKey(0)

"""------------------------------------------------------------------------------------------------------"""

"""FLIPPING IMAGES"""

# Flipping an image is achieved by changing the orientation of the image.
# Syntax: dst = flip(src, flipCode)
# src: input image
# flipCode: a flag to specify how to flip the image
# flipCode = 0: flip vertically; flipCode > 0: flip horizontally; flipCode < 0: flip both vertically and horizontally

img_NZ_rgb_flipped_horz = cv2.flip(img_NZ_rgb, 1)
img_NZ_rgb_flipped_vert = cv2.flip(img_NZ_rgb, 0)
img_NZ_rgb_flipped_both = cv2.flip(img_NZ_rgb, -1)

# Show the images
plt.figure(figsize=(18, 5))
plt.subplot(141);plt.imshow(img_NZ_rgb_flipped_horz);plt.title("Horizontal Flip")
plt.subplot(142);plt.imshow(img_NZ_rgb_flipped_vert);plt.title("Vertical Flip")
plt.subplot(143);plt.imshow(img_NZ_rgb_flipped_both);plt.title("Both Flipped")
plt.subplot(144);plt.imshow(img_NZ_rgb);plt.title("Original")

plt.imshow()