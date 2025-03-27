import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

img_NZ_bgr = cv2.imread('assets_data/New_Zealand_Boat.jpg', cv2.IMREAD_COLOR)
resize_img = cv2.resize(img_NZ_bgr, None, fx=0.2, fy=0.2)

cv2.imshow('Resized Image', resize_img)
cv2.waitKey(0)