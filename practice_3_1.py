import cv2
import numpy as np

# image = cv2.imread(
#     "data/lesson1/Lenna.png"
# )
#
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #  -> to hsv
#
#
# cv2.imshow("Lenna", image)
# #
# # h = hsv[:, :, 0]
# # s = hsv[:, :, 1]
# # v = hsv[:, :, 2]
#
# h, s, v = cv2.split(hsv)
#
# # increase brightness
#
# # decrease saturation
# # consider bounds uint 8
#
# s = s.astype(np.uint64) #->  take more bits
#
# s -= 40
#
# # check bounds 0-255
#
# mask_s = s < 0
# s[mask_s] = 0
#
# s = s.astype(np.uint8)
#
# # v = v.astype(np.uint64)
# # v += 40
# #
# # mask_v = v > 255
# # v[mask_v] = 255
# #
# # v = v.astype(np.uint8)
#
#
# # merge channels, new image
# new_hsv = cv2.merge([h, s, v])
#
# # show result -> to bdr
#
# new_image = cv2.cvtColor(new_hsv, cv2.COLOR_HSV2BGR)
#
# cv2.imshow("new Lenna", new_image)
#
# cv2.waitKey(0)


# import cv2
#
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
# lower = (0, 100, 160)  # нижні межі
# upper = (8, 255, 255)  # верхні межі
#
# # отримати маску для правильних піксесів
# mask_red = cv2.inRange(hsv, lower, upper)
#
#
# cv2.imshow("mask_red", mask_red)
#
# mask_bool = mask_red.astype(bool)
#
# image[~mask_bool] = 0
#
# cv2.imshow("color mask", image)
#
# cv2.waitKey(0)

#lab - use for change lightness
#
# import utils
# utils.lesson2_lab_range()

image = cv2.imread("data/lesson2/evening2.jpg")

cv2.imshow("color evening", image)

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB) # l = lightness, a = green-red, b = blue-yellow

l, a, b = cv2.split(lab)

l = l.astype(np.uint64)

l+= 60

l = np.clip(l, 0, 255) # corrects bounds

l = l.astype(np.uint8)

new_lab = cv2.merge([l, a, b])

new_image = cv2.cvtColor(new_lab, cv2.COLOR_LAB2BGR)

cv2.imshow("new evening", new_image)

cv2.waitKey(0)

