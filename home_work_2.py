# Завдання 1
# Відкрийте зображення data/Lenna.png. Прочитайте маски
# data/mask1.png та data/mask2.png.
# Об’єднайте дві маски в одну, скористайтесь cv2.bitwise_or()
# та виведіть результат
# Виведіть ту частину зображення, яка відповідає:
#  mask1
#  mask2
#  mask1 і mask2
# Усі пікселі які не відповідають маскам замінити на 0, перед
# застосуванням змініть тип даних у масці на bool
import cv2

image = cv2.imread(
    "data/lesson1/Lenna.png",
    cv2.IMREAD_GRAYSCALE,
)

cv2.imshow("Lenna", image)

# Прочитайте маски
# data/mask1.png та data/mask2.png.

mask1 = cv2.imread(
    "data/lesson1/mask1.png",
    cv2.IMREAD_GRAYSCALE,
)
cv2.imshow("mask1", mask1)

mask2 = cv2.imread(
    "data/lesson1/mask2.png",
    cv2.IMREAD_GRAYSCALE,
)
cv2.imshow("mask2", mask2)

# Об’єднайте дві маски в одну, скористайтесь cv2.bitwise_or()
# та виведіть результат
result = cv2.bitwise_or(mask1, mask2)
cv2.imshow("Result of mask1 united with mask2", result)

# Виведіть ту частину зображення, яка відповідає:
#  mask1
mask1_bool = mask1.astype(bool)
result1 = image.copy()
result1[~mask1_bool] = 0

cv2.imshow("Lenna with mask1", result1)

#  mask2
mask2_bool = mask2.astype(bool)
result2 = image.copy()
result2[~mask2_bool] = 0

cv2.imshow("Lenna with mask2", result2)

#  mask1 і mask2
united_masks = result.astype(bool)
result3 = image.copy()
result3[~united_masks] = 0

cv2.imshow("Lenna with mask1 and united mask2", result3)

cv2.waitKey(0)


# Завдання 2
# Домашнє завдання
# Виведіть зображення. Підберіть самостійно межі

image = cv2.imread(
    "data/lesson1/baboo.jpg",
    cv2.IMREAD_GRAYSCALE,
)

cv2.imshow("baboo", image)


segment = image[10:50, 50:205]
print(segment.shape)
print(segment.dtype)
cv2.imshow("baboo segment", segment)

cv2.waitKey(0)
