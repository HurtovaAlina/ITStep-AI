# Завдання 1
# Відкрийте зображення data/lesson2/marbles.png.
# Використайте кольорову сегментацію для отримання масок до
# кульок:
#  синього кольору
#  зеленого і червоного
#  чорного
#  білого
#  усіх кульок
import cv2
import numpy as np

# image = cv2.imread("data/lesson2/marbles.png")
# image = cv2.resize(image, (500, 500))
#
# print(image.dtype)
# print(image.shape)
# print(image[0, 0])
#
# cv2.imshow("color marbles", image)
#
# # перевести з bgr в hsv
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#
# # межі для синього кольору в hsv
#
#
# # h -- 40 - 80  # колір(кути ділимо на два)
# # s -- 150 - 255  # насиченість
# # v -- 150 - 255  # скравість кольору
#
#
# # lower = (100, 125, 108)  # нижні межі
# # upper = (130, 255, 255)  # верхні межі
# #
# #
# #  отримати маску для правильних піксесів
# # mask = cv2.inRange(hsv, lower, upper)
# #
# # cv2.imshow("mask_blue", mask)
#
# # межі для зелений і червоного кольору в hsv
#
# # h -- 40 - 80  # колір(кути ділимо на два)
# # s -- 150 - 255  # насиченість
# # v -- 150 - 255  # скравість кольору
#
# # # зелений
# # lower = (35, 95, 80)  # нижні межі
# # upper = (90, 255, 255)  # верхні межі
# # mask_green = cv2.inRange(hsv, lower, upper)
# # cv2.imshow("mask_green", mask_green)
# #
# # # червоний
# # lower = (0, 100, 160)  # нижні межі
# # upper = (8, 255, 255)  # верхні межі
# # mask_red = cv2.inRange(hsv, lower, upper)
# # cv2.imshow("mask_red", mask_red)
# #
# # r_g_mask = cv2.bitwise_or(mask_green, mask_red)
# # cv2.imshow("r_g_mask", r_g_mask)
#
# #  чорного
# # lower = (0, 0, 0)  # нижні межі
# # upper = (180, 185, 40)  # верхні межі
# # mask_black = cv2.inRange(hsv, lower, upper)
# # cv2.imshow("mask_black", mask_black)
#
#
# #  білого
# lower = (0, 0, 215)  # нижні межі
# upper = (180, 30, 255)  # верхні межі
# mask_white = cv2.inRange(hsv, lower, upper)
# cv2.imshow("mask_white", mask_white)
#
# #  усіх кульок
#
# cv2.waitKey(0)


# Завдання 2
# Відкрийте зображення data/lesson2/cell.png. Покращте
# зображення за допомогою вирівнювання гістограми. Оскільки
# зображення кольорове, вам доведеться зробити наступні
# кроки:
#  перевести зображення в LAB
#  розбити зображення на канали l, a та b
#  вирівняти гістограму для l
#  зібрати канали назад в зображення
#  перевести результат назад в BGR
# Порівняйте результати для 2 алгоритмів.

image = cv2.imread("data/lesson2/cell.png")
image = cv2.resize(image, (500, 500))

print(image.dtype)
print(image.shape)
print(image[0, 0])

cv2.imshow("color cell", image) # in bgr

# перевести з bgr в lab

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB) # l = lightness, a = green-red, b = blue-yellow

l, a, b = cv2.split(lab)

new_l = cv2.equalizeHist(l)

# l = l.astype(np.uint64)

# l+= 40
#
# l = np.clip(l, 0, 255) # corrects bounds
#
# l = l.astype(np.uint8)

new_lab = cv2.merge([new_l, a, b])

new_image = cv2.cvtColor(new_lab, cv2.COLOR_LAB2BGR)

cv2.imshow("new cell", new_image)


cv2.waitKey(0)