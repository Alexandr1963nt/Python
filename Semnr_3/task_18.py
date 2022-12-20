# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве
# и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент.
# Если есть несколько элементов, которые равноудалены от X, выведите наименьший.

# Ввод: 5
# Ввод: 6
# 1 2 0 4 7
# Вывод: 7

import os

def create_array_N(N):
    import random
    array = []
    for i in range(N):
        array.append(random.randint(1, N))
    return array

os.system('cls')

N = int(input('Введите количество элементов в массиве N : '))
user_list = create_array_N(N)
print(user_list)
X = int(input('Введите число, которое необходимо проверить в массиве - X : '))
if X >= N:
    Y = X
    while Y > 0:
        try:
            if user_list.index(Y) in range(N):
                print(
                    f'Ближайшее к {X} число {user_list[user_list.index(Y)]} '
                    f'содержится в массиве на индексе {user_list.index(Y)}\n')
                break
        except:
            # print(f'Числа {X} нет в заданном массиве')
            Y -= 1
else:
    i = 0
    while True:
        try:
            Y = X-i
            if user_list.index(Y) in range(N):
                print(
                    f'Ближайшее к {X} число {user_list[user_list.index(Y)]} '
                    f'содержится в массиве на индексе {user_list.index(Y)}\n')
                break
        except:
            Y = X+i
            try:
                if user_list.index(Y) in range(N):
                    print(
                        f'Ближайшее к {X} число {user_list[user_list.index(Y)]} '
                        f'содержится в массиве на индексе {user_list.index(Y)}\n')
                    break
            except:
                i += 1
