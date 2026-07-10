# Завдання 1
# Відкрийте відео з файлу data\lesson8\meetings.mp4
# Застосуйте детекцію та виведіть результат, підберіть
# параметри
# Можете змінити розмір кадру для кращої візуалізації
# cv2.resize()


import cv2
import ultralytics

# # створення моделі
# model = ultralytics.YOLO("yolo11s.pt")
#
# # відкрити відео
# cap = cv2.VideoCapture("data/lesson8/meetings.mp4")
#
# # отримати перший кадр
# success, img = cap.read()
#
# # змінити розмір
# img = cv2.resize(img, None, fx=0.7, fy=0.7)
#
# cv2.imshow("original", img)
#
# # детекція
# results = model.predict(
#     img,
#     device="mps",      # Mac
#     conf=0.3,
#     iou=0.7
# )
#
# result = results[0]
#
# # показати результат
# cv2.imshow("result", result.plot())
#
# # назви класів
# print(result.names)
#
# # рамки
# boxes = result.boxes
#
# for i in range(len(boxes)):
#     box = boxes[i]
#
#     # ймовірність
#     conf = box.conf.cpu().numpy()[0]
#
#     # клас
#     cls = int(box.cls.cpu().numpy()[0])
#     class_name = result.names[cls]
#
#     # координати
#     xyxy = box.xyxy.cpu().numpy().astype(int)
#     x1, y1, x2, y2 = xyxy[0]
#
#     print(f"{i}: {class_name}, conf={conf:.2f}")
#
#     # вирізати знайдений об'єкт
#     roi = img[y1:y2, x1:x2]
#
#     if roi.size > 0:
#         cv2.imshow(f"{class_name}_{i}", roi)
#
#
# #  відео
# cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
#
# while True:
#     success, frame = cap.read()
#
#     if not success:
#         break
#
#     frame = cv2.resize(frame, None, fx=0.7, fy=0.7)
#
#     results = model.predict(
#         frame,
#         device="mps",
#         conf=0.3,
#         iou=0.7
#     )
#
#     result = results[0]
#
#     cv2.imshow("Meetings", result.plot())
#
#     boxes = result.boxes
#
#     for i in range(len(boxes)):
#         box = boxes[i]
#
#         cls = int(box.cls.cpu().numpy()[0])
#         class_name = result.names[cls]
#
#         xyxy = box.xyxy.cpu().numpy().astype(int)
#         x1, y1, x2, y2 = xyxy[0]
#
#         roi = frame[y1:y2, x1:x2]
#
#         if roi.size > 0:
#             cv2.imshow(f"{class_name}_{i}", roi)
#
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
#
# cap.release()
# cv2.destroyAllWindows()

# Завдання 2
# Відкрийте відео з файлу data\lesson8\meetings.mp4
# Застосуйте детекцію та почніть показувати відео з
# моменту, коли людей стало 5

import cv2
import ultralytics

# модель
model = ultralytics.YOLO("yolo11s.pt")

# відео
cap = cv2.VideoCapture("data/lesson8/meetings.mp4")

show_video = False

while True:
    success, frame = cap.read()

    if not success:
        break

    # зменшити кадр
    frame = cv2.resize(frame, None, fx=0.7, fy=0.7)

    # детекція
    results = model.predict(
        frame,
        device="mps",
        conf=0.3,
        iou=0.7
    )

    result = results[0]
    boxes = result.boxes

    # підрахунок людей
    people_count = 0

    for box in boxes:
        cls = int(box.cls.item())
        class_name = result.names[cls]

        if class_name == "person":
            people_count += 1

    print("Людей:", people_count)

    # якщо людей стало 5 або більше,
    # почати показувати відео
    if people_count >= 5:
        show_video = True

    if show_video:
        cv2.imshow("Meetings", result.plot())

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()