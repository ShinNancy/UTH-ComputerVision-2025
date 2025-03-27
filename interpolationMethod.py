"""Các phương pháp nội suy (interpolation) trong OpenCV

1. cv2.INTER_NEAREST: Phương pháp nội suy gần nhất
2. cv2.INTER_LINEAR: Phương pháp nội suy tuyến tính
3. cv2.INTER_CUBIC: Phương pháp nội suy Cubic   
4. cv2.INTER_LANCZOS4: Phương pháp nội suy Lanczos4
"""

# 1. INTER_NEAREST (Phương pháp nội suy gần nhất)

"""
Nguyên tắc: Lấy giá trị pixel gần nhất từ pixel gốc
Ưu điểm: Nhanh chóng, dễ hiểu, ít tốn tài nguyên
Nhược điểm: Chất lượng ảnh kém, không mượt khi phóng to
Dùng cho: Ảnh có biên sắc nét (pixel art, bản đồ nhiệt)
"""

# 2. INTER_LINEAR (Phương pháp nội suy tuyến tính)

"""

Nguyên tắc: Lấy trung bình trọng số của 4 pixel xung quanh
Ưu điểm: Nhanh chóng, chất lượng ảnh tốt, mượt khi phóng to
Nhược điểm: Chất lượng không cao khi phóng to nhiều lần
Dùng cho: Khi thu nhỏ ảnh hoặc phóng to ảnh mà không yêu cầu quá sắc nét.
"""

# 3. INTER_CUBIC (Phương pháp nội suy Cubic)

"""
Nguyên tắc: Lấy trung bình trọng số của 16 pixel xung quanh bằng phép nội suy bậc 3
Ưu điểm: Chất lượng ảnh cao, mượt khi phóng to nhiều lần
Nhược điểm: Tốn tài nguyên, chậm hơn so với INTER_LINEAR
Dùng cho: Khi cần phóng to ảnh nhưng vẫn giữ được chất lượng tốt.
"""

# 4. INTER_LANCZOS4 (Phương pháp nội suy Lanczos4)
"""
Nguyên tắc: Sử dụng 8 x 8 pixel xung quanh để nội suy theo hàm sinc
Ưu điểm: Chất lượng ảnh cao, mượt khi phóng to nhiều lần
Nhược điểm: Tốn tài nguyên, chậm hơn so với INTER_CUBIC
Dùng cho: Khi cần chất lượng ảnh cao nhất có thể
"""

import cv2

img = cv2.imread('assets_data/New_Zealand_Boat.jpg', cv2.IMREAD_COLOR)

nearest = cv2.resize(img,(200,200), interpolation = cv2.INTER_NEAREST)
linear = cv2.resize(img,(200,200), interpolation = cv2.INTER_LINEAR)
cubic = cv2.resize(img,(200,200), interpolation = cv2.INTER_CUBIC)
lanczos4 = cv2.resize(img,(200,200), interpolation = cv2.INTER_LANCZOS4)

cv2.imshow('Nearest', nearest)
cv2.imshow('Linear', linear)    
cv2.imshow('Cubic', cubic)  
cv2.imshow('Lanczos4', lanczos4)

cv2.waitKey(0)
cv2.destroyAllWindows()