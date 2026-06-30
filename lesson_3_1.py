# колір
import cv2

# # читати як чорно біле
# image = cv2.imread("data/lesson2/lego.jpg", cv2.IMREAD_GRAYSCALE)
# image = cv2.resize(image, (500, 500))
#
# print(image.dtype)
# print(image.shape)
# print(image[0, 0])
#
# cv2.imshow("gray", image)
#
# # читати як кольорове
# # за замовчуванням читає як кольорове
# image = cv2.imread("data/lesson2/lego.jpg")
# image = cv2.resize(image, (500, 500))
#
# print(image.dtype)
# print(image.shape)
# print(image[0, 0])
#
# cv2.imshow("color", image)

# формат(кольорові простори)
# bgr -- blue green red

# import utils
# utils.lesson2_bgr_range()



# дістати колір з зображення
image = cv2.imread("data/lesson2/lego.jpg")
image = cv2.resize(image, (500, 500))

print(image.shape) # (рядки, стовпчики, колір)

# # отримати червоний канал(bgr)
# red = image[:, :, 2]
#
#
# # imshow сприймає як чорноюіле зображення
# print(red.shape)
# cv2.imshow("red", red)


# # правильний спосіб
# red = image.copy()
#
# # зберігаємо червоний колір, все інше в 0
#
# # синій
# red[:, :, 0] = 0
#
# # зелений
# red[:, :, 1] = 0
#
#
# print(red.shape)
# cv2.imshow("red", red)


# # збільшити червоного на 10
# image[:, :, 2] += 10
#
# cv2.imshow(",ore red", image)


# кольоровий простір hsv
# import utils
# utils.lesson2_hsv_range()
#
#
# cv2.waitKey(0)



# отримати пікселі жовтого кольору

cv2.imshow("orig", image)

# межі для кольору в hsv

# h -- 40 - 80  # колір(кути ділимо на два)
# s -- 150 - 255  # насиченість
# v -- 150 - 255  # скравість кольору


lower = (40, 100, 100)  # нижні межі
upper = (80, 255, 255)  # верхні межі


# перевести з bgr в hsv
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# отримати маску для правильних піксесів
mask = cv2.inRange(
    hsv,
    lower,
    upper
)

cv2.imshow("mask", mask)


cv2.waitKey(0)