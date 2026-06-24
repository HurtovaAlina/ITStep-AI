# Завдання 1
# Створіть масив:
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12
# 13 14 15 16
import numpy as np

array_1 = np.arange(1, 17).reshape(4, 4)
print(array_1)
print(array_1.shape)
print(array_1.dtype)

# Використовуючи індекси виведіть:
# ● число 14
print("число 14:", array_1[3,1])

# ● третій рядок
print("третій рядок:", array_1[2])

# ● перший стовпчик
print("перший стовпчик:", array_1[:,0])
# ● верхню половину
print("верхню половину:", array_1[:2])

# ● замініть числа в рядках 2-3 на 100
print("замініть числа в рядках 2-3 на 100:")
array_1[1:3]=100
print(array_1)

# ● зробіть другий рядок таким як останній рядок
array_1[1] = array_1[3]
print("зробіть другий рядок таким як останній рядок")
print(array_1)


# Завдання 2

array_1 = np.arange(1, 17).reshape(4, 4)
print(array_1)

# У масиві з попереднього завдання створіть маску для
# парних чисел.
mask = array_1 % 2 == 0
print(mask)

# З її допомогою
# ● виведіть самі числа
print(array_1[mask])

# ● замініть їх на 100
array_1[mask] = 100
print(array_1)


# Завдання 3
# Створіть 2 масиви типу uint8:
# Масив 1: 128 200 10
# Масив 2: 250 10 34

array_1 = np.array([128, 200, 10], dtype=np.uint8)
print(array_1)
print(array_1.shape)
print(array_1.dtype)

array_2 = np.array([250, 10, 34], dtype=np.uint8)
print(array_2)
print(array_2.shape)
print(array_2.dtype)

# Об’єднайте їх у пропорції 20% першого масив + 80%
# другого масиву. В результаті має бути тип даних uint8 та
# числа в діапазоні 0-255

united_array = (0.2*array_1 + 0.8*array_2).round().astype(np.uint8)
print(united_array)
print(united_array.shape)
print(united_array.dtype)

