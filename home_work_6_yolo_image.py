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

import cv2 #Імпортує бібліотеку OpenCV, яка використовується для роботи із зображеннями та відео.
import ultralytics #Імпортує бібліотеку Ultralytics, яка містить модель YOLO для розпізнавання об'єктів.

# модель
#Створює модель YOLO.
# "yolo11s.pt" — файл із вже натренованою моделлю.
# Після цього через model можна знаходити об'єкти на зображенні або відео.
model = ultralytics.YOLO("yolo11s.pt")

# відео
#Відкриває відеофайл.
#cap — об'єкт, через який можна читати кадри відео один за одним.
cap = cv2.VideoCapture("data/lesson8/meetings.mp4")


#Створює змінну-прапорець.
# Спочатку вона має значення False, тобто відео не показується.
# Коли людей стане 5 або більше, змінна стане True.
show_video = False

#Починається нескінченний цикл.
#Він буде читати кадри, поки відео не закінчиться або користувач не натисне q.
while True:
    #Метод read() повертає два значення:
    # success — чи вдалося прочитати кадр (True або False).
    # frame — сам кадр у вигляді масиву NumPy.
    success, frame = cap.read()

    if not success:
        break

    # зменшити кадр
    #Зменшує розмір кадру.
    # None означає, що новий розмір буде обчислено автоматично.
    # fx=0.7 — ширина стане 70%.
    # fy=0.7 — висота стане 70%.
    # Менше зображення → швидша робота YOLO.
    frame = cv2.resize(frame, None, fx=0.7, fy=0.7)

    # детекція
    #Запускає пошук об'єктів на кадрі.
    # Параметри:
    # frame - Кадр, який потрібно проаналізувати.
    # device="mps"- Використовує графічний процесор Apple (Metal).
    # conf=0.3
    # Мінімальна впевненість моделі.
    # Наприклад: person   0.95
    # dog      0.82
    # chair    0.28
    #0.28 < 0.3 - стілець не буде показаний.
    #iou=0.7
    # IOU (Intersection over Union) використовується для видалення однакових рамок.
    # Якщо дві рамки сильно перекриваються (>70%), залишиться лише одна.
    results = model.predict(
        frame,
        device="mps",
        conf=0.3,
        iou=0.7
    )

    #predict() повертає список результатів. Беремо перший елемент.
    result = results[0]
    #Отримує всі знайдені рамки.
    #Наприклад:
    #Person
    # Person
    # Laptop
    # Chair
    # Dog
    boxes = result.boxes

    # підрахунок людей
    #Створюємо лічильник людей. Спочатку людей ще не пораховано.

    people_count = 0

    #Перебираємо всі знайдені об'єкти. Наприклад: box1 box2 box3
    for box in boxes:
        #У кожної рамки є номер класу. Наприклад: 0, 2, 16, 56. item() дістає число з тензора.
        #int() перетворює його на звичайне ціле число.
        cls = int(box.cls.item())
        #Перетворює номер класу на назву.
        class_name = result.names[cls]
        #Перевіряє, чи знайдений об'єкт є людиною.
        if class_name == "person":
            people_count += 1

    print("Людей:", people_count)

    # якщо людей стало 5 або більше,
    # почати показувати відео
    if people_count >= 5:
        show_video = True
    #Як тільки людей стало 5, прапорець змінюється.
    #починаємо показувати відео.
    if show_video:
        #Відображає кадр.
        # "Meetings" — назва вікна.
        # result.plot() малює:
        # рамки,
        # назви класів,
        # відсоток впевненості.
        # Без plot() показувався б звичайний кадр без розмітки.
        cv2.imshow("Meetings", result.plot())
        #Чекає 1 мілісекунду на натискання клавіші.
        #Якщо натиснули клавішу q, умова стане істинною.
        #0xFF використовується для коректного читання коду натиснутої клавіші на різних операційних системах.
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
#Закриває відеофайл та звільняє ресурси.
cap.release()
#Закриває всі вікна OpenCV.
cv2.destroyAllWindows()