# Завдання 1
# Створіть масив з числами від 1 до 10. Виведіть його, його
# розмір, тип даних.
# Змініть розмір масиву на (5, 2). Знову виведіть масив,
# розмір та тип даних
import numpy as np
#
# nums = np.arange(1,11)
# print(nums)
# print(nums.shape)
# print(nums.dtype)
#
# nums_reshaped = nums.reshape(5,2)
# print(nums_reshaped)
# print(nums_reshaped.shape)
# print(nums_reshaped.dtype)
#
# # # Створіть масив:
# # # 1 2 3 4
# # # 5 6 7 8
# # # 9 10 11 12
#
# nums = np.arange(1,13).reshape(3,4)
# print(nums)
#
# # # Використовуючи індекси виведіть:
# # # ● число 7
# print("число 7")
# print(nums[1,2])
#
# # # ● другий рядок
# print("другий рядок")
# print(nums[1])
#
# # # ● останній стовпчик
# print("останній стовпчик")
# print(nums[:, -1])
#
# # # ● праву половину
# print("праву половину")
# print(nums[:,2:4])
#
# # # ● жовту область
# print("жовту область")
# print(nums[1:3,1:3])
#
# # # ● замініть жовту область на -1
# print("замініть жовту область на -1")
# nums[1:3,1:3] = -1
# print((nums))
#
# # # ● зробіть перший стовпчик таким самим як і другий
# print("зробіть перший стовпчик таким самим як і другий")
# nums[:, 0] = nums[:, 1]
# print(nums)
#
# # У масиві з попереднього завдання
# nums = np.arange(1,13).reshape(3,4)
# print(nums)
# # створіть маску для чисел які більші за 6.
# mask = nums >6
# print(mask)
#
# print("створіть маску для чисел які більші за 6")
# print(nums[mask])
#
# #З її допомогою
# # ● виведіть кількість чисел більших за 6
# print("виведіть кількість чисел більших за 6")
# print(mask.sum())
#
# # ● виведіть самі числа
# print(nums[~mask])
#
# # ● до кожного числа яке відповідає масці додайте 10
# print("до кожного числа яке відповідає масці додайте 10")
# print(nums[mask]+10)
#
# # ● кожне число що не відповідає масці помножте на -1
# print("кожне число що не відповідає масці помножте на -1")
# print(nums[mask]*-1)
#
# # ● замініть ці числа які відповідають масці на відповідні їм з масиву
# # 1 0 1 0
# # 0 1 0 1
# # 1 0 1 0
#
# array = np.array([1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0]).reshape(3,4)
# print(array)
# print("замініть ці числа які відповідають масці на відповідні їм з масиву")
# nums[mask] = array[mask]
# print(nums)
#
# # Створіть масив
# # -10 24 35
# # 250 -6 7
# # 12 180 11
# # -2 -45 -26
# # Усі числа менші за 0 замініть на 0.
# # Усі числа більші за 100 замініть на 100
#
# my_array = np.array(
#     [[-10, 24, 35],
#     [250, -6, 7],
#     [12, 180, 11],
#     [-2, -45, -26]]
# )
#
# print(my_array)
# # Усі числа менші за 0 замініть на 0.
# print("Усі числа менші за 0 замініть на 0.")
# mask_1 = my_array < 0
# my_array[mask_1] = 0
# print(my_array)
#
# # Усі числа більші за 100 замініть на 100
# print("Усі числа більші за 100 замініть на 100")
# mask_2 = my_array > 100
# my_array[mask_2] = 100
# print(my_array)
#
# # Завдання 5
# # Створіть масив та виведіть його тип даних
# # 100 120 200 250 10
# # Додайте до кожного числа 50 та виведіть результат.
# # Створіть такий самий масив але з типом uint8
# # Знову додайте 50 та виведіть результат
# # Зробіть так щоб обчислення працювали правильно, якщо
# # число виходить більшим за 255 то зробіть його 255
#
# new_array_2 = np.array([100, 120, 200, 250, 10])
# print("Створіть масив та виведіть його тип даних")
# print(new_array_2+50)
# print(new_array_2.dtype)

# Завдання 6
# Створіть масив типу uint8
# 10 4 25 40 200
# |Помножте всі значення на 2. Результат має бути типу
# uint8 а всі значення в діапазоні 0-255
# Помножте всі значення на 1.5. Результат має бути типу
# uint8 а всі значення в діапазоні 0-255

my_array_3 = np.array([10, 4, 25, 40, 200])
my_array_3.astype(np.uint8) #int 8 only positive numbers 0..255 images
my_array_3 = my_array_3.astype(np.int64)

my_array_3 *=2
mask_array = my_array_3 > 255
print(mask_array)
my_array_3[mask_array] = 255

print(my_array_3)
print(my_array_3.dtype)
print(my_array_3.shape)

my_array_2 = my_array_3.astype(np.uint8)
print(my_array_3)
print(my_array_3.dtype)
print(my_array_3.shape)


my_array_3 = my_array_3 * 1.5
mask = my_array_3 > 255
print(mask)
my_array_3[mask] = 255
my_array_3 = my_array_3.astype(np.uint8)

print(my_array_3)
print(my_array_3)
print(my_array_3.dtype)
print(my_array_3.shape)

