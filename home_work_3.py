# Завдання 1
# Відкрийте зображення data\lesson2\darken.png. Проведіть з
# ним наступні операції, переведіть його в HSV формат та
# обробіть канал Value наступними способами:
#  застосуйте вирівнювання гістограм
#  збільшіть значення десь на 20-50%, оскільки тут
# результат буде типу float32 та явно вийде за межі [0-255]
# застосуйте np.clip(value, 0, 255) та value.astype(np.uint8)
# Виведіть результати обох обробок на екран

import cv2
import numpy as np

image = cv2.imread("data/lesson2/darken.png")
image = cv2.resize(image, (500, 500))

print(image.dtype)
print(image.shape)

cv2.imshow("darken original", image)

# BGR -> HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
print(hsv)

# value histogram
# create a copy
image_hist_value = hsv.copy()

# channel value
value = image_hist_value[:, :, 2]

#equalize the histogram
value = cv2.equalizeHist(value)

# put new value to image
image_hist_value[:, :, 2] = value

# HSV -> BGR
image_hist_value = cv2.cvtColor(image_hist_value, cv2.COLOR_HSV2BGR)

cv2.imshow("darken histogram value", image_hist_value)

# value updating
# create a copy
image_value = hsv.copy()

# change type to float
value = image_value[:, :, 2].astype(np.float32)

# correct value
value *= 1.5

# corrects bounds
value = np.clip(value, 0, 255)

# change type to uint8
value = value.astype(np.uint8)

#new value
image_value[:, :, 2] = value

# HSV -> BGR
image_value = cv2.cvtColor(image_value, cv2.COLOR_HSV2BGR)

cv2.imshow("darken value", image_value)

cv2.waitKey(0)