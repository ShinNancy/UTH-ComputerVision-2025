"""plt.subplot trong Matplotlib"""

# Dùng để tạo nhiều biểu đồ (plots) trong cùng một hình (figure)
# giúp hiển thị nhiều hình ảnh hoặc đồ thị trong một bố cục lưới (grid).

# Cú pháp: plt.subplot(nrows, ncols, index)
# nrows: số hàng
# ncols: số cột     
# index: vị trí của subplot (bắt đầu từ 1, từ trái sang phải, từ trên xuống dưới)

import matplotlib.pyplot as plt
import numpy as np

# Tạo dữ liệu
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 5))  # Tạo figure với kích thước 10x5 inches

# Biểu đồ 1 (Sin)
plt.subplot(1, 2, 1)  # 1 hàng, 2 cột, vị trí 1
plt.plot(x, y1, 'r')  # Đường màu đỏ
plt.title("Sine Wave")

# Biểu đồ 2 (Cos)
plt.subplot(1, 2, 2)  # 1 hàng, 2 cột, vị trí 2
plt.plot(x, y2, 'b')  # Đường màu xanh
plt.title("Cosine Wave")

plt.show()  # Hiển thị tất cả
