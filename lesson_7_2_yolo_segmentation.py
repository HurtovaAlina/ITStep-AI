import ultralytics
from ultralytics import YOLO
import numpy as np
import cv2
#
# # модель для сегментації
# model = YOLO("yolo11s-seg.pt")
#
# img = cv2.imread("data/lesson_seg/human.jpg")
#
# cv2.imshow("orig", img)
#
#
# results = model.predict(
#     img,
#     device="cpu"
# )
# result = results[0]
#
# res = result.plot()
# cv2.imshow("result", res)
#
#
# print(result)
#
#
# masks = result.masks
# print(masks)
#
#
# masks_data = masks.data
# masks_data = masks_data.cpu().numpy()
#
#
# # маска третього об'єкта
# mask3 = masks_data[2]
#
# # зміна розміру до оригінального
# height, width, colors = img.shape
#
# mask3 = cv2.resize(mask3, (width, height))
#
# # зміна типів даних
#
# mask3_bool = mask3.astype(bool)
#
#
# mask3_uint = mask3.astype(np.uint8)
# mask3_uint *= 255
#
#
# cv2.imshow("mask", mask3_uint)
#
# # все що не відповідає масці замінити на 0
# img[~mask3_bool] = 0
# cv2.imshow("with mask", img)
#
#
# cv2.waitKey(0)

# перебрати маски без циклу
# model = YOLO("data/lesson_seg/crop-seg.pt")
# img = cv2.imread("data/lesson_seg/crop3.jpg")
#
#
# results = model.predict(
#     img,
#     device="cuda",
# )
# result = results[0]
#
# masks = result.masks
# masks_data = masks.data
#
# masks_data = masks_data.cpu().numpy()
#
# # знайди площу(суму) кожнох маски
# # axis=(1, 2) - параметр видає суму для кожного набора даних,  як список значень
# masks_area = masks_data.sum(axis=(1, 2))
#
# # індекс найбільшої площі - функція argmax() не само і максимальное, а для максимального єлемента
# i = masks_area.argmax()
#
# print(masks_area)
# print(i)

#
#
# # тренування моделі
# model = ultralytics.YOLO("yolo11s.pt")
#
# model.train(
#     data="data/yolo_dataset/dataset.yaml",
#     device="cuda",
#     batch=6,   # кількість зображень які модель бічить за 1 раз(розмір порції)
#     hsv_h=0.7
# )
#
#
# # використання натренованої нефромережі
#
# model = YOLO("runs/detect/train2/weights/best.pt")
#
# results = model.predict(
#     "data/yolo_dataset/images/train/0000068_03388_d_0000010.jpg",
#     device="cuda"
# )
# result = results[0]
# res = result.plot()
#
# cv2.imshow("train", res)
#
# results = model.predict(
#     "data/yolo_dataset/images/val/0000023_00868_d_0000010.jpg",
#     device="cuda"
# )
# result = results[0]
# res = result.plot()
#
# cv2.imshow("val", res)
cv2.waitKey(0)