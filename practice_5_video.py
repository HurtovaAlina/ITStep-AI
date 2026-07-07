# Завдання 1
# Виведіть відео з файлу data\lesson7\text.mp4 на екран та
# збережіть в новий файл.
# Змініть розмір зображення.
import cv2

# # відкрити відео
# cap = cv2.VideoCapture(
#     "data/lesson7/text.mp4",   # шлях до файлу з відео або 0 для відеокамери комп'ютери
# )
#
#
# # інформація про відео
# # розмір кадрів
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#
# print(width)
# print(height)
#
# # FPS -- кількість кадрів у секунду
# fps = int(cap.get(cv2.CAP_PROP_FPS))
# print(fps)
#
# # збереження відео
# # кодек(розширення файлу(mp4, avi, xvd))
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out_writer = cv2.VideoWriter(
#     "result_practice_5.mp4",   # файл куди зберігати відео
#     fourcc,      # кодек
#     fps,         # частота кадрів в секунду
#     (600, 600),   # розмір (ширина, висота)
#     isColor=True,   # чи є зображення кадрів кольоровими
# )
#
#
# while True:
#     # отримати наступний кадр
#     success, frame = cap.read()
#
#     # перевірка чи вдалось отримати кадр
#     if not success:
#         break
#
#     new_frame = cv2.resize(frame, (600, 600))
#
#     cv2.imshow("resized_frame", new_frame)
#     out_writer.write(new_frame)
#     cv2.waitKey(4)
#
# # в кінці все закрити
# out_writer.release()
# cap.release()

# Завдання 2
# Відкрийте відео з файлу data\lesson7\text.mp4. Проведіть
# бінарізацію кадрів та збережіть в новий файл.

# відкрити відео
cap = cv2.VideoCapture(
    "data/lesson7/text.mp4",   # шлях до файлу з відео або 0 для відеокамери комп'ютери
)

# інформація про відео
# розмір кадрів
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(width)
print(height)

# FPS -- кількість кадрів у секунду
fps = int(cap.get(cv2.CAP_PROP_FPS))
print(fps)

# збереження відео
# кодек(розширення файлу(mp4, avi, xvd))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out_writer = cv2.VideoWriter(
    "result_practice_5_2.mp4",   # файл куди зберігати відео
    fourcc,      # кодек
    fps,         # частота кадрів в секунду
    (700, 700),   # розмір (ширина, висота)
    isColor=False,   # чи є зображення кадрів кольоровими
)


while True:
    # отримати наступний кадр
    success, frame = cap.read()

    # перевірка чи вдалось отримати кадр
    if not success:
        break

    new_frame = cv2.resize(frame, (700, 700))

    # перевести в чорнобіле
    gray = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", gray)

    # розмиття гауса
    # blured = cv2.GaussianBlur(
    #     gray,
    #     (3, 3),
    #     sigmaX=1.8
    # )
    # cv2.imshow("blured", blured)

    # двосторонній фільтр - better result
    bilat = cv2.bilateralFilter(
        gray,  # зображення з шумом
        d=9,    # розмір фільтру
        sigmaColor=75,   # наскільки важливі пікселі іншого кольору
        sigmaSpace=75,   # наскільки важливими є далекі пікселі
    )

    cv2.imshow("bilat", bilat)


    binary = cv2.adaptiveThreshold(
        bilat,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        3
    )

    cv2.imshow("binary_video", binary)
    out_writer.write(binary)

    cv2.waitKey(30)

# в кінці все закрити
out_writer.release()
cap.release()


# Завдання 3
# Відкрийте відео з файлу data\lesson7shapes.mp4.
# Проведіть виділення кольорів на кадрах та збережіть в новий
# файл.

# відкрити відео
# cap = cv2.VideoCapture(
#     "data/lesson7/shapes.mp4",   # шлях до файлу з відео або 0 для відеокамери комп'ютери
# )
#
# # збереження відео
# # кодек(розширення файлу(mp4, avi, xvd))
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out_writer = cv2.VideoWriter(
#     "result_practice_5_3.mp4",   # файл куди зберігати відео
#     fourcc,      # кодек
#     30,         # частота кадрів в секунду
#     (600, 600),   # розмір (ширина, висота)
#     isColor=False,   # чи є зображення кадрів кольоровими
# )
#
# while True:
#     # отримати наступний кадр
#     success, frame = cap.read()
#
#     # перевірка чи вдалось отримати кадр
#     if not success:
#         break
#
#     new_frame = cv2.resize(frame, (600, 600))
#
#     cv2.imshow("video_all_colors", new_frame)
#
#     # take green color -> create mask
#
#     # # перевести з bgr в hsv h - colour, s - saturation, v - brightness
#
#     hsv = cv2.cvtColor(new_frame, cv2.COLOR_BGR2HSV)
#
#     # see color on diagram (div on 2 -> can't take 365 we have only 0-255 range)
#
#     lower = (40, 75, 40)  # нижні межі
#     upper = (65, 255, 255)  # верхні межі
#
#     mask_green = cv2.inRange(hsv, lower, upper)
#     cv2.imshow("mask_green", mask_green)
#
#     out_writer.write(mask_green)
#
#     cv2.waitKey(20)
#
# # в кінці все закрити
# out_writer.release()
# cap.release()
