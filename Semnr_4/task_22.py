# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются
# в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)

# Output: 11 6
# 6 12
import os
os.system('cls')


def create_array(n, mn, mx):
    import random
    array = [random.randint(mn, mx) for _ in range(n)]
    return array


n = int(input('Кол-во элементов первого набора? -> '))
m = int(input('Кол-во элементов второго набора? -> '))
listing_1 = create_array(n, 2, 13)
listing_2 = create_array(m, 2, 13)
print(listing_1)
print(listing_2)

set_1 = set(listing_1)
set_2 = set(listing_2)

result = set_1 & set_2
print('Пересечение множеств - ', sorted(result), '\n')
