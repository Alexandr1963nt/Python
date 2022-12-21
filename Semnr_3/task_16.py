# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве
# и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 3

# 1 2 3 4 5
# Вывод: 1

import os
import time


def create_array(N):
    import random
    array = []
    for i in range(N):
        array.append(random.randint(1, int(N/2)))
    return array


def ending_word_times(n):
    if n % 10 in {2, 3, 4} and n % 100 not in {12, 13, 14}:
        return 'раза'
    else:
        return 'раз'


# унарный поиск вхождения искомого элемента в массив
def count_element_in_array(arr, element):
    count = 0
    for i in range(0, len(arr)):
        if arr[i] == element:
            count += 1
    return count

# Бинарныый поиск - прикольная штука - ооооочень быыыыстрый !!!!!!


def binary_search(array, item):
    if len(array) < 2 and array[0] == item: return 1
    elif len(array) < 2 and array[0] != item : return 0
    else:
        low = 0
        high = len(array) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = array[mid]
            if guess == item:
                array.pop(mid)
                return 1 + binary_search(array, item)
            if guess > item:
                high = mid - 1
            else:
                low = mid + 1
    return 0


os.system('cls')

N = int(input('Введите количество элементов в массиве N : '))
user_list = create_array(N)
# print(f'Сформирован {user_list}')
X = int(input('Введите число, которое необходимо проверить в массиве - X : '))

start1 = time.time_ns()
how_many_time_was_X_found = user_list.count(X)
end1 = (time.time_ns()-start1)/1000000
print('Поиск count(X) = ', end1, 'ms')

start = time.time_ns()
how_many_time_was_X_found = count_element_in_array(user_list, X)
end = (time.time_ns()-start)/1000000
print('Поиск в цикле = ', end, 'ms')

start2 = time.time_ns()
user_list.sort()
# print(user_list)
end2 = (time.time_ns()-start2)/1000000
print('array.sort() = ', end2, 'ms')

start3 = time.time_ns()
fast = binary_search(user_list, X)
print('fast = ', fast, 'раз' )
end3 = (time.time_ns()-start3)/1000000
print('binary_search = ', end3, 'ms')

if how_many_time_was_X_found > 0:
    print(
        f'Число {X} встречается в массиве {how_many_time_was_X_found} '
        f'{ending_word_times (how_many_time_was_X_found)}\n')
else:
    print(f'Числа {X} нет в массиве\n')

