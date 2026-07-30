from ultralytics import YOLO
import numpy as np
import cv2

# Завдання 1
# Відкрийте зображення data/lesson_seg/tumor1.jpg
# Проведіть сегментацію зображення використовуючи
# модель data/lesson_seg/brain-tumor-seg.jpg
# Визначте площу пухлини в пікселях.
# Визначте площу в
# (1 піксель – 0,0025
# )
# В залежності від площі присвойте пухлині певний тип
#  <10 – small
#  10-25 – middle
#  >25 – large
# Покажіть пухлину – за допомогою маски усі лишні
# пікселі зробіть 0, а як назву зображення використайте її тип

img = cv2.imread("data/lesson_seg/tumor1.jpg")

cv2.imshow("orig", img)

model = YOLO("data/lesson_seg/brain-tumor-seg.pt")

results = model.predict(
    img,
    device = "mps"
)

result = results[0]

res_img = result.plot()

cv2.imshow("detected oject", res_img)

masks = result.masks
print(masks)

#відображення маски
masks_data = masks.data
masks_data = masks_data.cpu().numpy()

masks_data = masks_data[0]
pixels_of_object = masks_data.sum()

print(pixels_of_object)

object_area = pixels_of_object*0.0025
object_name = result.names[0]
print(f"Area of {object_name} = {object_area}")

if object_area < 10:
    tumor_type = "small"
elif 10<= object_area <= 25:
    tumor_type = "middle"
else:
    tumor_type = "large"

# зміна розміру до оригінального
height, width, colors = img.shape
masks_data = cv2.resize(masks_data, (width, height))

mask_bool = masks_data.astype(bool)

# все що не відповідає масці замінити на 0
img[~mask_bool] = 0
cv2.imshow(tumor_type, img)

cv2.waitKey(0)