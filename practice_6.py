# Завдання 1
# Отримайте перший кадр з файлу data\lesson8\animals.mp4
# та виведіть його на екран.
# Проведіть детекцію об’єктів зо допомогою YOLO та
# виведіть результати.
# Змініть параметри моделі conf та iou і подивіться як це
# впливає на результат.
# Отримайте рамки для кожного об’єкта, виріжіть їх та
# виведіть як окремі зображення

import cv2
import ultralytics

# створення моделі
# s -- small(розмір моделі)
model = ultralytics.YOLO("yolo11s.pt")

# отримати зображення з ввідео
cap = cv2.VideoCapture('data/lesson8/animals.mp4')

success, img = cap.read()

img = cv2.resize(img, None, fx=0.5, fy=0.5)
print(img.shape)

cv2.imshow("orig", img)

# застосування моделі
# модель може одночасно обробити декілька зображень [img1, img2, img3, ..]
# на виході results -- список результів [result1, result2, result3, ..]
results = model.predict(
    img,  # зображення
    device="mps",  # процесор де робити обчисдення
                # cpu --звичайний процесор
                # cuda -- графічний процесор(gpu) на Windows\Linux
                # mps -- графічний процесор(gpu) на MacOS

    conf=0.35,   # мінімальна ймовірність для об'єктів,
                # все що менше відсіюється

    iou=0.7,   # наскільки сильно можуть перетинаться рамки,
               # якщорамки перетинаються сильніше то залишаєму ту
                # в якої більшо ймовірність

    #classes=[0, 1],  # класи які враховувати(див result.names)
)
print(type(results))
print(results)

# results -- список з одним елементом
# отримати результ
result = results[0]

print(result)

# отримати назви класів(об'єкти які вмієме визначати модель)
names = result.names
print(type(names))
print(names)


# самі об'єкти
boxes = result.boxes
print(type(boxes))
print(boxes)

# візуалізація результів (слоники, пташка)
res_img = result.plot()
cv2.imshow("result", res_img)

# ймовірності
conf = boxes.conf
print(type(conf))

# відключити від графічного процесора
conf = conf.cpu()

# перевести в масив numpy
conf = conf.numpy()

print(conf)
print(conf.shape)
print(conf.dtype)

# # рамка(box)
# box_1 = boxes[0]  # дані першого обєкта - слон
#
# print(box_1)
# print(box_1.conf)
# print(box_1.cls)  # індекс класу
# print(box_1.xyxy)  # координати меж
#
#
# # вивести назву та ймовірність
# conf_1 = box_1.conf
# conf_1 = conf_1.cpu().numpy()
# print(f"Ймовірність першого обєкта {conf_1[0]}")
#
# cls_1 = box_1.cls
# cls_1 = cls_1.cpu().numpy()
# print(f"Індекс класу першого обєкта {cls_1[0]}")
#
# class_id_1 = int(cls_1[0])
# class_name_1 = names[class_id_1]
# print(f"Клас першого обєкта {class_name_1}")
#
# # рамка(box)
# box_4 = boxes[3]  # дані четвертого обєкта - пташка
#
# print(box_4)
# print(box_4.conf)
# print(box_4.cls)  # індекс класу
# print(box_4.xyxy)  # координати меж
#
#
# # вивести назву та ймовірність
# conf_4 = box_4.conf
# conf_4 = conf_4.cpu().numpy()
# print(f"Ймовірність четвертого обєкта {conf_4[0]}") # в box це перший і єдиний обʼєкт, тому  0
#
# cls_4 = box_4.cls
# cls_4 = cls_4.cpu().numpy()
# print(f"Індекс класу четвертого обєкта {cls_4[0]}")
#
# class_id_4 = int(cls_4[0])
# class_name_4 = names[class_id_4]
# print(f"Клас четвертого обєкта {class_name_4}")
#
#
# # рамка(box)
# box_3 = boxes[2]  # дані третього обєкта - третього слона
#
# print(box_3)
# print(box_3.conf)
# print(box_3.cls)  # індекс класу
# print(box_3.xyxy)  # координати меж
#
#
# # вивести назву та ймовірність
# conf_3 = box_3.conf
# conf_3 = conf_3.cpu().numpy()
# print(f"Ймовірність третього обєкта {conf_3[0]}") # в box це перший і єдиний обʼєкт, тому  0
#
# cls_3 = box_3.cls
# cls_3 = cls_3.cpu().numpy()
# print(f"Індекс класу третього обєкта {cls_3[0]}")
#
# class_id_3 = int(cls_3[0])
# class_name_3 = names[class_id_3]
# print(f"Клас третього обєкта {class_name_3}")
#
# # координати третього обʼєкта (слона)
# xyxy = box_3.xyxy
# print(xyxy)
#
# # переведення координат в int
# xyxy = xyxy.cpu().numpy()
# xyxy = xyxy.astype(int)
#
# print(xyxy)
#
#
# # вирізати об'єкт з всього зображення
# x1, y1, x2, y2 = xyxy[0]
#
# # region of interest
# # x - стовпчики
# # y - рядочки
# roi = img[y1:y2, x1:x2]
#
# cv2.imshow(f"roi {class_name_3 = } {conf_3[0]*100:.2f}%", roi)

# boxes = result.boxes
# for box in boxes:
#
#     conf = box.conf
#     conf = conf.cpu().numpy()
#     xyxy = box.xyxy
#     print(xyxy)
#
#     # номер класу
#     cls = box.cls.cpu().numpy()
#     class_id = int(cls[0])
#     class_name = result.names[class_id]
#
#     # переведення координат в int
#     xyxy = xyxy.cpu().numpy()
#     xyxy = xyxy.astype(int)
#
#     # вирізати об'єкт з всього зображення
#     x1, y1, x2, y2 = xyxy[0]
#
#     # region of interest
#     # x - стовпчики
#     # y - рядочки
#     roi = img[y1:y2, x1:x2]
#
#     cv2.imshow(f"roi {class_name = } {conf[0] * 100:.2f}%", roi)

# # відео
while True:
    success, frame = cap.read()

    if not success:
        break

    frame = cv2.resize(frame, None, fx=0.5, fy=0.5)

    results = model.predict(frame)
    result = results[0]

    cv2.imshow("results", result.plot())

    boxes = result.boxes

    for i in range(len(boxes)):
        box = boxes[i]
        conf = box.conf
        conf = conf.cpu().numpy()
        xyxy = box.xyxy
        print(xyxy)

        # номер класу
        cls = box.cls.cpu().numpy()
        class_id = int(cls[0])
        class_name = result.names[class_id]

        # переведення координат в int
        xyxy = xyxy.cpu().numpy()
        xyxy = xyxy.astype(int)

        # вирізати об'єкт з всього зображення
        x1, y1, x2, y2 = xyxy[0]

        # region of interest
        # x - стовпчики
        # y - рядочки
        roi = frame[y1:y2, x1:x2]

        names = result.names

        cv2.imshow(f"{class_name} - {i}", roi)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.waitKey(0)