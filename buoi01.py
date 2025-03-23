# import libraries
import os
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# display image directly from file
img = Image.open('assets_data/checkerboard_18x18.png')
img.show()

"""READING IMAGES USING OPENCV"""
# Function syntax: cv2.imread(path, flag)
# flag: cv2.IMREAD_COLOR (default, 1), cv2.IMREAD_GRAYSCALE (0), cv2.IMREAD_UNCHANGED (-1)

# Read image as gray scale
img_cb = cv2.imread('assets_data/checkerboard_color.png', cv2.IMREAD_GRAYSCALE)

# print image data (pixel values), element of 2D numpy array 
print(img_cb)

"""DISPLAYING IMAGES ATTRIBUTES"""
# print the size of the image
print("Image size (height, width):", img_cb.shape)

"""DISPLAYING IMAGES USING MATPLOTLIB"""
# Display image
plt.imshow(img_cb, cmap='gray')
plt.axis('off')
plt.show()

"""-----------------------------------------------------------------------------------------------------------------"""

""""WORKING WITH COLOR IMAGES"""
# Read and display Coca-Cola logo.
Image("assets_data/coca-cola-logo.png")

# Read and display color image
coke_img = cv2.imread('assets_data/coca-cola-logo.png', cv2.IMREAD_COLOR)

# print the size of the image
print("Image size (height, width, channels):", coke_img.shape)

# OpenCV reads images in BGR format, we need to convert it to RGB format
coke_img_rgb = cv2.cvtColor(coke_img, cv2.COLOR_BGR2RGB) #coke_img_channels_reversed = coke_img[:, :, ::-1]

plt.imshow(coke_img_rgb)
plt.axis('off')
plt.show()

"""-----------------------------------------------------------------------------------------------------------------"""

"""SPLITTING AND MERGING COLOR CHANNELS"""
# cv2.split() function splits the image into its color channels
# cv2.merge() function merges the color channels back into an image

# Split the image into the B, G, R channels
img_NZ_bgr=cv2.imread('assets_data/New_Zealand_Lake.jpg', cv2.IMREAD_COLOR)
b,g,r = cv2.split(img_NZ_bgr)

# Show the 4 images with its channels
plt.figure(figsize=(5, 20))

plt.subplot(141); plt.imshow(r, cmap='gray'); plt.title('Red channel'); plt.axis('off')
plt.subplot(142); plt.imshow(g, cmap='gray'); plt.title('Green channel'); plt.axis('off')
plt.subplot(143); plt.imshow(b, cmap='gray'); plt.title('Blue channel'); plt.axis('off')

# Merge channels back into BGR
imgMerged = cv2.merge((b, g, r))

# Convert BGR to RGB before displaying
plt.subplot(144)
plt.imshow(cv2.cvtColor(imgMerged, cv2.COLOR_BGR2RGB))
plt.title("Merged Output")
plt.axis('off')

"""Note: Matplotlib does not always render plots automatically, depending on the environment (e.g., scripts vs Jupyter Notebook).
   Fix: Add plt.show() at the end of the code to display the plot.
"""
plt.show()

"""-----------------------------------------------------------------------------------------------------------------"""

"""CONVERTING TO DIFFERENT COLOR SPACES"""

# Function syntax: cv2.cvtColor(src, code)
# src: input image
# code: color space conversion code

"""ColorConversionCodes:
   BGR -> RGB: cv2.COLOR_BGR2RGB
   RGB -> BGR: cv2.COLOR_RGB2BGR
   BGR -> HSV: cv2.COLOR_BGR2HSV
   ...
"""

# Convert BGR to HSV (Hue, Saturation, Value)
img_hsv=cv2.imread('assets_data/New_Zealand_Lake.jpg', cv2.COLOR_BGR2HSV)

# Split the image into the B,G,R components
h,s,v = cv2.split(img_hsv)

# Show the channels
plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(h, cmap="gray");plt.title("H Channel")
plt.subplot(142);plt.imshow(s, cmap="gray");plt.title("S Channel")
plt.subplot(143);plt.imshow(v, cmap="gray");plt.title("V Channel")

plt.show()

"""-----------------------------------------------------------------------------------------------------------------"""
"""SAVING IMAGES"""

# Function syntax: cv2.imwrite(filename, img)
# filename: name of the file to which the image is saved 
# img: image to be saved

# Save the image
cv2.imwrite('assets_data/New_Zealand_Lake_HSV.jpg', img_hsv)
Image(filename='assets_data/New_Zealand_Lake_HSV.jpg')   # Display the saved image