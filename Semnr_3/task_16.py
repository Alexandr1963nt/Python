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


os.system('cls')

N = int(input('Введите количество элементов в массиве N : '))
user_list = create_array(N)
print(f'Сформирован {user_list}')
X = int(input('Введите число, которое необходимо проверить в массиве - X : '))
how_many_time_was_X_found = user_list.count(X)
if how_many_time_was_X_found > 0:
    print(
        f'Число {X} встречается в массиве {how_many_time_was_X_found} '
        f'{ending_word_times (how_many_time_was_X_found)}\n')
else:
    print(f'Числа {X} нет в массиве\n')
