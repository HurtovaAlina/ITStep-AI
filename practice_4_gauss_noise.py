# Завдання 1
# Відкрийте зображення data/lesson3/notes.png. Проведіть
# наступні дії:
#  проведіть бінарізацію(звичайну та адаптивну)
#  застосуйте розмиття(гаусове) візьміть ядра 3, 5, 11 та
# sigmaX 0, 2, 10
#  повторіть бінарізацію, але перед тим застосуйте bilateral
# filter
import cv2
#
#
# img = cv2.imread("data/lesson3/notes.png")
#
# img = cv2.resize(img, (600, 600))
#
# cv2.imshow("original", img)
#
# gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# cv2.imshow("gray", gray_image)
# #
# # threshold = 128
# #
# # mask = gray_image < threshold
# #
# # gray_image[mask] = 0
# # gray_image[~mask] = 255
# #
# # cv2.imshow("binary", gray_image)
#
# # gauss = cv2.GaussianBlur(
# #     gray_image,  # зображення з шумом
# #     (3, 3),   # розмір фільтру(ядра)
# #     sigmaX=1.8,    # наскільки важливими є далекі пікселі 0 - adaptive value
# # )
# #
# # cv2.imshow("gauss", gauss)
#
# # # двосторонній фільтр
# bilat = cv2.bilateralFilter(
#     gray_image,  # зображення з шумом
#     d=5,    # розмір фільтру
#     sigmaColor=75,   # наскільки важливі пікселі іншого кольору
#     sigmaSpace=50,   # наскільки важливими є далекі пікселі
# )
#
# cv2.imshow("bilat", bilat)
#
#
#
# #adaptive
#
# res = cv2.adaptiveThreshold(
#     bilat,   # зображення з текстом(чорнобіле)
#     255,    #  білий колір
#     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # фільтр для обрахунку порогу(гаус)
#     cv2.THRESH_BINARY,   # це просто треба вказати
#     7,   # розмір фільтру
#     3,          # наскільки піксель має відрізнятися від порогу
# )
#
# cv2.imshow("adaptive", res)
#
#
# cv2.waitKey(0)
#
# cv2.destroyAllWindows()

# Завдання 2
# Відкрийте зображення data/lesson3/sudoku.jpg. Проведіть
# для нього бінарізацію, а саме
#  CLAHE
#  гаусове розмиття
#  адаптивна бінарізація
#  NLMean
# Самостійно підберіть параметри, збережіть результат.
# Порівняйте результати для гаусової та середньої адаптивної
# бінарізації

# Основний принцип  - очистка шуму, потім бінаризація

img = cv2.imread("data/lesson3/sudoku.jpg")

img = cv2.resize(img, (600, 600))

cv2.imshow("original", img)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray_image)

# Очистка від шуму за допомогою CLAHE

# Створення об'єкта CLAHE - як гістограма, але не така контрастна
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

# Застосування
result = clahe.apply(gray_image)

cv2.imshow("CLAHE Result", result)

# очистка від шуму за допомогою gauss

gauss = cv2.GaussianBlur(
    gray_image,  # зображення з шумом
    (3, 3),   # розмір фільтру(ядра)
    sigmaX=1.8,    # наскільки важливими є далекі пікселі 0 - adaptive value
)

cv2.imshow("gauss", gauss)

# CLAHE + adaptive

res = cv2.adaptiveThreshold(
    result,   # зображення з текстом(чорнобіле)
    255,    #  білий колір
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # фільтр для обрахунку порогу(гаус)
    cv2.THRESH_BINARY,   # це просто треба вказати
    9,   # розмір фільтру
    9,          # наскільки піксель має відрізнятися від порогу
)

cv2.imshow("adaptive+CLAHE", res)

# gauss  + adaptive

res1 = cv2.adaptiveThreshold(
    gauss,   # зображення з текстом(чорнобіле)
    255,    #  білий колір
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # фільтр для обрахунку порогу(гаус)
    cv2.THRESH_BINARY,   # це просто треба вказати
    7,   # розмір фільтру
    3,          # наскільки піксель має відрізнятися від порогу
)

cv2.imshow("adaptive+gauss", res1)

# прибрали шум за допомогою nlmean

result_nlmean = cv2.fastNlMeansDenoising(gray_image, None, h=10, templateWindowSize=7, searchWindowSize=21)


# nlmean + adaptive
res_nlmean = cv2.adaptiveThreshold(
    result_nlmean,   # зображення з текстом(чорнобіле)
    255,    #  білий колір
    cv2.ADAPTIVE_THRESH_MEAN_C,   # фільтр для обрахунку порогу(гаус)
    cv2.THRESH_BINARY,   # це просто треба вказати
    9,   # розмір фільтру
    2,          # наскільки піксель має відрізнятися від порогу
)

cv2.imshow("adaptive+nlmean", res_nlmean)



cv2.waitKey(0)
cv2.destroyAllWindows()



