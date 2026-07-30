# Завдання 1
# Відкрийте зображення data/lesson_seg/crop3.jpg
# Проведіть сегментацію зображення використовуючи
# модель data/lesson_seg/crop-seg.jpg
# Покажіть усі маски рослин з підписами назви цієї
# рослини.
# Покажіть також самі рослини, для цього застосуйте
# маску, і всі зайві пікселі замініть на 255(зробити білий фон)

from ultralytics import YOLO
import numpy as np
import cv2


# img = cv2.imread("data/lesson_seg/crop3.jpg")
#
# cv2.imshow("orig", img)
#
# model = YOLO("data/lesson_seg/crop-seg.pt")
#
# results = model.predict(
#     img,
#     device="mps"
# )
#
# result = results[0]
# print(result)
#
# res_img = result.plot()
# cv2.imshow("res", res_img)
#
# masks = result.masks
# print(masks)
#
# #дістати маску
# masks_data = masks.data
# masks_data = masks_data.cpu().numpy()
#
# height,width,color = img.shape
#
# for i in range(len(masks_data)):
#     mask = masks_data[i]
#     mask = cv2.resize(mask, (width, height))
#     mask = mask.astype(bool)
#
#     new_image = img.copy()
#
#     new_image[~mask] = 255
#     cv2.imshow(f"plant {i}", new_image)
#
# cv2.waitKey(0)

# Завдання 2
# Відкрийте зображення data/lesson_seg/crop3.jpg
# Проведіть сегментацію зображення
# Порахуйте розмір кожної рослини(площа маски)
# Покажіть найбільшу рослину кожного виду

img = cv2.imread("data/lesson_seg/crop3.jpg")

cv2.imshow("orig", img)

model = YOLO("data/lesson_seg/crop-seg.pt")

results = model.predict(
    img,
    device = "mps"
)

result = results[0]
print(result)

res_img = result.plot()

cv2.imshow("result", res_img)

masks = result.masks
# print(masks)

#маска кожного обʼєкту
masks_data = masks.data
masks_data = masks_data.cpu().numpy()

height, width, color = img.shape

mask_list = []
for mask in masks_data:
    sum = mask.sum()
    mask_list.append(sum)
print(mask_list)

max_mask = max(mask_list)

print(f"Max mask = {max(mask_list)}")

for i in range(len(mask_list)):
    if max_mask == mask_list[i]:
        break
print(i)

mask3 = masks_data[i]
# зміна розміру до оригінального
height, width, colors = img.shape
mask3 = cv2.resize(mask3, (width, height))

# зміна типів даних
mask3_bool = mask3.astype(bool)

mask3_uint = mask3.astype(np.uint8)
mask3_uint *= 255

cv2.imshow("max_mask", mask3_uint)

cv2.waitKey(0)