# Завдання 1
# Відкрийте відео data/lesson_pose/squat.mp4
# Ваша задача рахувати кількість присідань.
# Отримайте перший кадр та виділіть основні точки.
# Отримайте координати 3-ох точок ноги
# Визначте кут між цими трьома точками. Скористайтесь
# функцією utils.get_angle(x1, y1, x2, y2, x3, y3) де x2, y2 –
# координати коліна(центральна точка)
# Запустіть відео та добавте на сам кадр кут згинання ніг.
# Визначіть нижню межу кута(якщо людина опустилась
# нижче вважаємо що вона достатньо опустилась) та верхню
# межу кута(якщо людина піднялась вище вважаємо що вона
# достатньо піднялась)
# Добавте кількість присідань та
# кут на кожен кадр.
import cv2
import ultralytics

import utils

# відкрити відео
cap = cv2.VideoCapture("data/lesson_pose/squat.mp4")

success, img = cap.read()

upper_limit_angle = 155
lower_limit_angle = 60

total_sitting = 0
is_sitting = False

model = ultralytics.YOLO("yolo11s-pose.pt")

while True:

    success, frame = cap.read()

    if not success:
        break

    results = model.predict(frame,
                            device="mps")

    result = results[0]
    print(result)

    keypoints = result.keypoints

    xy = keypoints.xy

    xy = xy.cpu().numpy()
    # print(xy)
    # print(xy.dtype)
    # print(xy.shape)

    # дістаємо точки для першого об'єкта
    xy = xy[0]
    # змінити тип даних на int
    xy = xy.astype(int)  # 17 точок
    # print(xy)

    result_img = result.plot()

    x_right_knee, y_right_knee = xy[14]
    cv2.circle(
        result_img,  # зображення де малювати коло
        center=(x_right_knee, y_right_knee),  # координати центру
        radius=10,  # радіус в пікселях
        color=(0, 255, 0),  # колір в BGR(green)
        thickness=-1,  # товщина ліній, -1 означає повністю заповнити кольором
    )

    x_right_foot, y_right_foot = xy[16]
    cv2.circle(
        result_img,  # зображення де малювати коло
        center=(x_right_foot, y_right_foot),  # координати центру
        radius=10,  # радіус в пікселях
        color=(0, 255, 0),  # колір в BGR(green)
        thickness=-1,  # товщина ліній, -1 означає повністю заповнити кольором
    )

    x_right_hip, y_right_hip = xy[12]
    cv2.circle(
        result_img,  # зображення де малювати коло
        center=(x_right_hip, y_right_hip),  # координати центру
        radius=10,  # радіус в пікселях
        color=(0, 255, 0),  # колір в BGR(green)
        thickness=-1,  # товщина ліній, -1 означає повністю заповнити кольором
    )

    current_angle = utils.get_angle(x_right_hip, y_right_hip, x_right_knee, y_right_knee, x_right_foot, y_right_foot)

    if current_angle >= upper_limit_angle and is_sitting == True:
        is_sitting = False


    if current_angle <= lower_limit_angle and is_sitting == False:
        total_sitting += 1
        is_sitting = True


    cv2.putText(
        result_img,  # зображення де пишемо текстq
        f"angle: {current_angle}, sittings: {total_sitting}",  # текст
        (40, 40),  # позиція, лівий нижній кут
        cv2.FONT_HERSHEY_SIMPLEX,  # шрифт
        1,  # розмір шрифту
        (255, 255, 255),  # колір в BGR
        2  # товщина ліній
    )

    cv2.imshow("result", result_img)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break