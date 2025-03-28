import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Đọc ảnh với chế độ grayscale (0)
img = cv2.imread("assets_data/Apollo_11_Launch.jpg", 0)

# Kiểm tra nếu ảnh đã được đọc đúng
if img is None:
    print("Lỗi: Không thể đọc ảnh. Hãy kiểm tra đường dẫn!")
else:
    plt.imshow(img, cmap='gray')  # Hiển thị ảnh xám đúng cách
    plt.axis("off")  # Ẩn trục tọa độ
    plt.show()  # Hiển thị ảnh
