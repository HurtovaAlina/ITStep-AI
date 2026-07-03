# Завдання 1
# Відкрийте зображення data/lesson3/sonet.png. Проведіть
# бінарізацію.
# Обов’язково використайте:
#  розмиття або наведення різкості
#  адаптивну бінарізацію
#  очищеня шумів
import cv2


img = cv2.imread("data/lesson3/sonet.png")

img = cv2.resize(img, (700,700))

cv2.imshow("original", img)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray_image)

# histogram

histogram = cv2.equalizeHist(gray_image)

cv2.imshow("histogram", histogram)

# Gauss blur gray_image

gauss =  cv2.GaussianBlur(
    gray_image,  # зображення з шумом
    (3, 3),   # розмір фільтру(ядра)
    sigmaX=2,    # наскільки важливими є далекі пікселі 0 - adaptive value
)

cv2.imshow("gauss", gauss)


# gauss  + adaptive threshold gauss

res_adaptive = cv2.adaptiveThreshold(
    gauss,   # зображення з текстом(чорнобіле)
    255,    #  білий колір
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # фільтр для обрахунку порогу(гаус)
    cv2.THRESH_BINARY,   # це просто треба вказати
    7,   # розмір фільтру
    1.9,          # наскільки піксель має відрізнятися від порогу
)

cv2.imshow("adaptive+gauss", res_adaptive)

# histogram + adaptive threshold

res_adaptive_hist = cv2.adaptiveThreshold(
    histogram,   # зображення з текстом(чорнобіле)
    255,    #  білий колір
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # фільтр для обрахунку порогу(гаус)
    cv2.THRESH_BINARY,   # це просто треба вказати
    5,   # розмір фільтру
    1.8,          # наскільки піксель має відрізнятися від порогу
)

cv2.imshow("histogram adaptive+gauss", res_adaptive_hist)

# прибрали шум для hist за допомогою nlmean

result_nlmean = cv2.fastNlMeansDenoising(res_adaptive_hist, None, h=11, templateWindowSize=7, searchWindowSize=21)

cv2.imshow("hist+nlmean (noise)", result_nlmean)



cv2.waitKey(0)


# Завдання 2
# Відкрийте зображення data/lesson3/sonnet_noised.png.
# Проведіть бінарізацію. Застосуйте код з завдання 1 та
# спробуйте покращити результат

img_1 = cv2.imread("data/lesson3/sonet_noised.png")
img_1 = cv2.resize(img_1, dsize=(700, 700))

cv2.imshow("original", img_1)

gray_image = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)

cv2.imshow("gray", gray_image)


# прибираємо шум
# 1. двосторонній фільтр
bilat = cv2.bilateralFilter(
    gray_image,  # зображення з шумом
    d=9,    # розмір фільтру
    sigmaColor=75,   # наскільки важливі пікселі іншого кольору
    sigmaSpace=75,   # наскільки важливими є далекі пікселі
)

cv2.imshow("bilat", bilat)

# 2. nlmean
nlmean = cv2.fastNlMeansDenoising(gray_image, None, h=10,  templateWindowSize=7, searchWindowSize=21)


cv2.imshow("nlmean", nlmean)

# 3. gauss

gauss = cv2.GaussianBlur(
    gray_image,  # зображення з шумом
    (7, 7),   # розмір фільтру(ядра)
    sigmaX=1.6,    # наскільки важливими є далекі пікселі
)

cv2.imshow("gauss", gauss)

# адаптивна бінаризація
res_adaptive_nlmean = cv2.adaptiveThreshold(
    nlmean,   # зображення з текстом(чорнобіле)
    255,    #  білий колір
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # фільтр для обрахунку порогу(гаус)
    cv2.THRESH_BINARY,   # це просто треба вказати
    7,   # розмір фільтру
    2,          # наскільки піксель має відрізнятися від порогу
)

cv2.imshow("adaptive+nlmeam", res_adaptive_nlmean)


# адаптивна бінаризація bilat
res_adaptive = cv2.adaptiveThreshold(
    bilat,   # зображення з текстом(чорнобіле)
    255,    #  білий колір
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # фільтр для обрахунку порогу(гаус)
    cv2.THRESH_BINARY,   # це просто треба вказати
    9,   # розмір фільтру
    1.8,          # наскільки піксель має відрізнятися від порогу
)

cv2.imshow(" bilat adaptive", res_adaptive)

# адаптивна бінаризація gauss
res_adaptive_gauss = cv2.adaptiveThreshold(
    gauss,   # зображення з текстом(чорнобіле)
    255,    #  білий колір
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # фільтр для обрахунку порогу(гаус)
    cv2.THRESH_BINARY,   # це просто треба вказати
    5,   # розмір фільтру
    2,          # наскільки піксель має відрізнятися від порогу
)

cv2.imshow("gauss adaptive", res_adaptive_gauss)


cv2.waitKey(0)