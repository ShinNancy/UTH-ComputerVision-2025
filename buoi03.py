import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img = cv2.imread("assets_data/Apollo_11_Launch.jpg", 0)
plt.imshow(img, cmap='gray')
plt.axis("off")
plt.show()

"""DRAWING A LINE"""

# Syntax: img = cv2.line(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
# img: input 
# pt1: First point (x,y location) of the line segment
# pt2: Second point of the line segment
# color: Color of the line which will be drawn

# thickness (optional): Integer specifying the line thickness. Default value is 1.
# lineType (optional): Type of the line

imgLine = img.copy()

cv2.line(imgLine, (200,100), (400,100), (0,255,255), thickness=5, lineType=cv2.LINE_AA)
plt.imshow(imgLine[:,:,::-1])
plt.axis("off")
plt.show()

"""DRAWING A CIRCLE"""

# Syntax: img = cv2.circle(img, center, radius, color[, thickness[, lineType[, shift]]])

imgCircle = img.copy()

cv2.circle(imgCircle, (900, 500), 100, (0,0,255), thickness=5, lineType=cv2.LINE_AA)

plt.imshow(imgCircle, cmap='gray')
plt.axis("off")
plt.show()

"""DRAWING A RECTANGLE"""

# Syntax: img = cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
# pt1: Vertex of the rectangle. Usually we use the top-left vertex here.
# pt2: Vertex of the rectangle opposite to pt1. Usually we use the bottom-right vertex here.

imgRec =img.copy()
cv2.rectangle(imgRec, (500, 100), (700, 600), (255, 0, 255), thickness=5, lineType=cv2.LINE_8)

plt.imshow(imgRec, cmap='gray')
plt.axis("off")
plt.show()

"""ADDING TEXT"""

# Syntax: img = cv2.putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])

imageText = img.copy()
text = "Apollo, July 16, 1969"
fontScale = 2.3
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontColor = (0, 255, 0)
fontThickness = 2

cv2.putText(imageText, text, (200, 700), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA);
