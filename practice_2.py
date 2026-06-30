# Завдання 1
# Відкрийте зображення data/Lenna.png. Виведіть на екран
# розмір зображення, тип даних, максимальну та мінімальну
# інтенсивність пікселів, саме зображення з підписом.
from pickletools import uint8

import cv2
import numpy as np
#
# image = cv2.imread(
#     "data/lesson1/Lenna.png",  # шлях до файлу
#     cv2.IMREAD_GRAYSCALE,   # прапорець як читати зображення(чорнобіле)
# )
#
# print(type(image))
# print(image.shape)
# print(image.dtype)   # uint8  (0 - 255)
# print(image)
# print(image.max()) # max інтенсивність пікселів - найбільше значення яскравості (від 0 до 255).
# print(image.min()) # min інтенсивність пікселів - найменше значення яскравості
#
# # показати зображення
# cv2.imshow(
#     "Lenna",  # назва для зображення
#     image           # саме зображення
# )
# cv2.waitKey(0)
#
# # Завдання 2
# # Відкрийте зображення data/Lenna.png. Виведіть на екран
#
# image = cv2.imread(
#     "data/lesson1/Lenna.png",  # шлях до файлу
#     cv2.IMREAD_GRAYSCALE,   # прапорець як читати зображення(чорнобіле)
# )
#
# cv2.imshow(
#     "Lenna",  # назва для зображення
#     image           # саме зображення
# )
#
#
# # такі зображень:
# #  Верхній лівий кут розміром 100х50
# segment = image[0:100, 0:50]
# print(segment.shape)
# print(segment.dtype)
# cv2.imshow("segment", segment)
#
#
# #  Центральний квадрат розміром 100х100
# segment = image[78:178, 78:178]
# print(segment.shape)
# print(segment.dtype)
# cv2.imshow("square segment", segment)
#
#
# #  Верхню половину
# segment = image[0:128, 0:255]
# print(segment.shape)
# print(segment.dtype)
# cv2.imshow("upper half segment", segment)
#
#
# # Нижню половину
# segment = image[128:255, 0:255]
# print(segment.shape)
# print(segment.dtype)
# cv2.imshow("bottom half segment", segment)
#
#
# #  Ліву половину
# segment = image[0:255, 0:128]
# print(segment.shape)
# print(segment.dtype)
# cv2.imshow("left half segment", segment)
#
#
# #  Праву половину
# segment = image[0:255, 128:255]
# print(segment.shape)
# print(segment.dtype)
# cv2.imshow("right half segment", segment)
#
# cv2.waitKey(0)
#
# # Завдання 3
# # Відкрийте зображення data/Lenna.png. Створіть наступні
# # зображення
#
# image = cv2.imread(
#     "data/lesson1/Lenna.png",  # шлях до файлу
#     cv2.IMREAD_GRAYSCALE,   # прапорець як читати зображення(чорнобіле)
# )
#
# cv2.imshow(
#     "Lenna",  # назва для зображення
#     image           # саме зображення
# )
#
# image[0:15, :] = 0
# image[241:255, :] = 255
#
# print(image.shape)
# print(image.dtype)
# cv2.imshow("image black white border", image)
# cv2.waitKey(0)
#
# image[:, 0:15] = 0
# image[:, 240:255] = 0
#
# print(image.shape)
# print(image.dtype)
# cv2.imshow("image black borders vertical", image)
# cv2.waitKey(0)
#
# image[:, 0:46] = 0
# image[:, 210:256] = 0
# image[0:46, :] = 0
# image[210:256, :] = 0
#
#
# print(image.shape)
# print(image.dtype)
# cv2.imshow("image black borders vertical", image)
# cv2.waitKey(0)
#
# # Завдання 4
# # Відкрийте зображення data/Lenna.png. Створіть маску для
# # пік селів з інтенсивністю більше 128 та виведіть її. Також
# # виведіть заперечення цієї маски.
# # На оригінальному зображенні, усі пікселі які не
# # відповідають масці замініть на 0 та виведіть результат
#
# image = cv2.imread(
#     "data/lesson1/Lenna.png",  # шлях до файлу
#     cv2.IMREAD_GRAYSCALE,   # прапорець як читати зображення(чорнобіле)
# )
#
# cv2.imshow(
#     "Lenna",  # назва для зображення
#     image           # саме зображення
# )
# cv2.waitKey(0)
#
# # Створіть маску для
# # пік селів з інтенсивністю більше 128 та виведіть її. Також
# # виведіть заперечення цієї маски.
#
# mask = image > 128
#
# cv2.imshow(
#     "mask",
#     mask.astype(np.uint8) * 255
# )
#
# cv2.imshow(
#     "negative mask",
#     (~mask).astype(np.uint8) * 255
# )
#
# # На оригінальному зображенні, усі пікселі які не
# # відповідають масці замініть на 0 та виведіть результат
#
# result = image.copy()
# result[~mask] = 0
#
# cv2.imshow("Result", result)
#
# cv2.waitKey(0)


# gamma correction
image = cv2.imread(
    "data/lesson1/Lenna.png",  # шлях до файлу
    cv2.IMREAD_GRAYSCALE,   # прапорець як читати зображення(чорнобіле)
)

cv2.imshow(
    "Lenna",
    image
)

new_image = ((image/255)**1.5)*255 #gamma correction changes every pixel
new_image= new_image.astype(np.uint8) # getting float -> convert to uint8
cv2.imshow(
    "Lenna with increased bright", new_image)
cv2.waitKey(0)

new_image = ((image/255)**0.8)*255
new_image= new_image.astype(np.uint8) # getting float -> convert to uint8
cv2.imshow(
    "Lenna with decreased bright", new_image)
cv2.waitKey(0)