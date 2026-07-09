# Завдання 1
# Відкрийте відео з файлу data\lesson7\meter.mp4.
# Проведіть бінарізацію кадрів та збережіть в новий файл.
# Можливо очистіть від шуму або наведіть різкість через
# bilateralFilter
import cv2

# відкрити відео
cap = cv2.VideoCapture(
    "data/lesson7/meter.mp4",   # шлях до файлу з відео
)
# збереження відео
# кодек(розширення файлу(mp4, avi, xvd))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out_writer = cv2.VideoWriter(
    "result_home_work_5.mp4",   # файл куди зберігати відео
    fourcc,      # кодек
    30,         # частота кадрів в секунду
    (600, 600),   # розмір (ширина, висота)
    isColor=False,   # чи є зображення кадрів кольоровими
)

while True:
    # отримати наступний кадр
    success, frame = cap.read()

    # перевірка чи вдалось отримати кадр
    if not success:
        break

    new_frame = cv2.resize(frame, (600, 600))

    cv2.imshow("original", new_frame)

    gray = cv2.cvtColor(new_frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", gray)

    # двосторонній фільтр - фільтр прибирає дрібний шум, але не розмиває межі цифр або шкали лічильника.
    # Завдяки цьому після бінаризації контури залишаються чіткішими.
    bilat = cv2.bilateralFilter(
        gray,
        d=9,  # розмір фільтру
        sigmaColor=75,  # наскільки важливі пікселі іншого кольору
        sigmaSpace=75,  # наскільки важливими є далекі пікселі
    )

    cv2.imshow("bilat", bilat)

    # бінарізація
    binary = cv2.adaptiveThreshold(
        bilat,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        1.7
    )

    cv2.imshow("binary_video", binary)


    # морфологічна очистка шуму
    res = cv2.dilate(binary, (3, 3), iterations=1)
    res = cv2.erode(res, (3, 3), iterations=4)

    cv2.imshow("res", res)

    out_writer.write(res)

    cv2.waitKey(10)
# в кінці все закрити
out_writer.release()
cap.release()


