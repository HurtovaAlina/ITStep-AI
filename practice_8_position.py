# Завдання 1
# Відкрийте відео data/lesson_pose/sitting.mp4
import cv2
import ultralytics




# відкрити відео
cap = cv2.VideoCapture(r'data/lesson_pose/sitting.mp4')  # шлях до файлу з відео або 0 для відеокамери комп'ютер)
success, img = cap.read()

# Отримайте перший кадр
# Покажіть його, за потреби змініть розмір
cv2.imshow("orig", img)



# інформація про відео
# розмір кадрів
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width)
print(height)




# Завдання 2
# Застосуйте модель YOLO Pose
# Отримайте результати (result) та виведіть їх на екран
# Використайте параметри device

model = ultralytics.YOLO("yolo11s-pose.pt")

results = model.predict(img,
                        device = "mps")

result = results[0]

print(result)

# Завдання 3
# Користуючись методом plot() отримайте зображення з
# рамками та підписами і покажіть його.

result_img = result.plot()

cv2.imshow("result", result_img)

# Завдання 4
# ● Отримайте інформацію про ключові точки(keypoints)

# ключові точки
keypoints = result.keypoints

# ● Виведіть її на екран
print(keypoints)

# ● Отримайте координати точок(xy)
# координати xy
xy = keypoints.xy

# ● Виведіть координати на екран разом з типом даних та
# розміром(позбудьтесь тензорів за допомогою cpu() та
# numpy())
# позбутися tensor device
xy = xy.cpu().numpy()
print(xy)
print(xy.dtype)
print(xy.shape)
#(2, 17, 2) - 2 objects, 17 points, 2 coordinates


# Завдання 5
# дістаємо точки для першого об'єкта
xy = xy[0]

# змінити тип даних на int
xy = xy.astype(int)  # 17 точок
print(xy)

# # ● Отримайте координати для лівого коліна,
# x_left_knee, y_left_knee = xy[14]
#
# print(x_left_knee, y_left_knee)
#
# # намалювати коло на зображення
# # ● Намалюйте ці точки на зображенні
# # ○ ліве коліно – зелений
# # ○ ліва рука – червоний
# # ○ права рука – білий
# cv2.circle(
#     result_img,   # зображення де малювати коло
#     center=(x_left_knee, y_left_knee),   # координати центру
#     radius=10,   # радіус в пікселях
#     color=(0, 255, 0),  # колір в BGR(green)
#     thickness=-1,   # товщина ліній, -1 означає повністю заповнити кольором
# )
#
# # лівої руки,
# x_left_hand, y_left_hand = xy[9]
#
# print(x_left_hand, y_left_hand)
#
# # намалювати коло на зображення
# cv2.circle(
#     result_img,   # зображення де малювати коло
#     center=(x_left_hand, y_left_hand),   # координати центру
#     radius=10,   # радіус в пікселях
#     color=(0, 0, 255),  # колір в BGR(red)
#     thickness=-1,   # товщина ліній, -1 означає повністю заповнити кольором
# )
#
# # правої руки для першого об’єкта
# x_right_hand, y_right_hand = xy[10]
#
# print(x_right_hand, y_right_hand)
#
# # намалювати коло на зображення
# cv2.circle(
#     result_img,   # зображення де малювати коло
#     center=(x_right_hand, y_right_hand),   # координати центру
#     radius=10,   # радіус в пікселях
#     color=(255, 255, 255),  # колір в BGR(білий)
#     thickness=-1,   # товщина ліній, -1 означає повністю заповнити кольором
# )
#
#
# cv2.imshow("result", result_img)

# Завдання 6
# Для кожного кадру на відео намалюйте координати для
# лівого коліна, лівої руки, правої руки
# Беріть координати для першого об’єкта
#
total_sitting = 0
is_sitting = True

while True:

    success, frame = cap.read()

    if not success:
        break

    results = model.predict(frame,
                            device="mps")

    result = results[0]

    keypoints = result.keypoints

    xy = keypoints.xy
    xy = xy.cpu().numpy()
    xy = xy[0]
    xy = xy.astype(int)
    x_left_knee, y_left_knee = xy[14]
    cv2.circle(
        frame,  # зображення де малювати коло
        center=(x_left_knee, y_left_knee),  # координати центру
        radius=10,  # радіус в пікселях
        color=(0, 255, 0),  # колір в BGR(green)
        thickness=-1,  # товщина ліній, -1 означає повністю заповнити кольором
    )

    x_right_knee, y_right_knee = xy[13]
    cv2.circle(
        frame,  # зображення де малювати коло
        center=(x_right_knee, y_right_knee),  # координати центру
        radius=10,  # радіус в пікселях
        color=(255, 0, 0),  # колір в BGR(blue)
        thickness=-1,  # товщина ліній, -1 означає повністю заповнити кольором
    )

    x_left_hand, y_left_hand = xy[9]
    cv2.circle(
        frame,  # зображення де малювати коло
        center=(x_left_hand, y_left_hand),  # координати центру
        radius=10,  # радіус в пікселях
        color=(0, 0, 255),  # колір в BGR(red)
        thickness=-1,  # товщина ліній, -1 означає повністю заповнити кольором
    )

    x_right_hand, y_right_hand = xy[10]
    cv2.circle(
        frame,  # зображення де малювати коло
        center=(x_right_hand, y_right_hand),  # координати центру
        radius=10,  # радіус в пікселях
        color=(255, 255, 255),  # колір в BGR(білий)
        thickness=-1,  # товщина ліній, -1 означає повністю заповнити кольором
    )




# Завдання 7
# Під час відео обраховуйте кількість присідань.
# Вважайте що людина присіла якщо рука опустилась
# нижче коліна.
# Кількість присідань відображайте на кадрі(cv2.putText)

    if y_right_knee < y_right_hand and is_sitting:
        total_sitting += 1

    if y_right_knee < y_left_hand:
        is_sitting = False
    else:
        is_sitting = True

    cv2.putText(
        frame,  # зображення де пишемо текстq
        f"Total_sitting: {total_sitting}, sitting: {is_sitting}",  # текст
        (40,40),  # позиція, лівий нижній кут
        cv2.FONT_HERSHEY_SIMPLEX,  # шрифт
        1,  # розмір шрифту
        (255, 255, 255),  # колір в BGR
        2  # товщина ліній
    )


# Завдання 8
# Модифікуйте код щоб кількість присідань виводилась
# правильно. Для цього вам потрібно визначати чи людина
# зараз присідає чи піднімається за правилом:
# ● якщо рука нижче коліна то людина встає
# ● якщо рука вище коліна – присідає
# Рахуйте лише ті присідання які відбулись коли людина
# присідає та рука опинилась нижче коліна.
# Разом з кількістю присідань відображайте чи людина
# присідає чи встає

    result_img = result.plot()
    cv2.imshow("result", result_img)

    cv2.imshow("video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Завдання 9
# ● Отримайте 258 кадр з відео
# ● Застосуйте модель
# ● Отримайте результати(result)

# ● Отримайте дані про рамки(boxes)
print("рамки(boxes)")
print(result.boxes)

# ● Отримайте дані про рамку для першого об’єкта та
# виведіть їх
# xywh: tensor([[313.6138, 213.9492, 193.1806, 425.3339],
#         [537.9261, 228.3599,  36.3821, 118.3159]], device='mps:0')

# ● Відобразіть результати(метод plot())
# ● Зробіть висновки
cv2.waitKey(0)
