import cv2

img = cv2.imread("data/lesson4/j.png", cv2.IMREAD_GRAYSCALE)


cv2.imshow("orig", img)

# морфологічні оператори (очистка шуму на бінарних зображеннях)
# якщо в рамці є хоча б 1 білий піквель - то робимо його білим

dilate = cv2.dilate(img, (3,3),
iterations=1 # скільки разів застосувати
)

cv2.imshow("dilate", dilate)

# якщо в рамці є хоча б 1 чорний піквель - то робимо його чорним
erode = cv2.erode(img, (3,3), iterations=1) # скільки разів застосувати)

cv2.imshow("erode", erode)

# обидва
res = cv2.dilate(img, (3,3), iterations=1)
res = cv2.erode(res, (3,3), iterations=4)

cv2.imshow("res", res)


cv2.waitKey(0)