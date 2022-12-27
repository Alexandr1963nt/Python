# Задача 102
# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
# Задача 102 Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
# (Основная теорема арифметики утверждает, что каждое натуральное число n>1 можно
# факторизовать (разложить) в виде n= p1*...pk.
# Нахождение простых множителей числа 864. Сокращённый способ написания — 2**5 × 3**3)
# Первые: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37

import os
import time
os.system('cls')


def check_simple_multiplier(N):  # проверка числа на простоту
    i = 2
    j = 0
    while i*i <= N and j != 1:
        if N % i == 0:
            j = 1
        i += 1
    if j != 1:
        return N
    else:
        return None


def decompose_by_numbers_multipliers(N):
    m = list()
    n = N
    if check_simple_multiplier(N):
        m = [N]
        return m
    else:
        k = 2
        while k in range(2, N+1):
            if N % k == 0:
                m.append(k)
                N = N // k
                degree_index = 1
                while N % k == 0:
                    N = N // k
                    degree_index += 1
                if degree_index > 1:
                    m.append(f'{m.pop()}**{degree_index}')
                if check_simple_multiplier(N):
                    k = N
            if k != N:
                k += 1
        return (m)


def product_list_elements(lst):  # произведение элементов массива
    product = 1
    for i in lst:
        if type(i) == str:
            product *= int(i.partition('**')[0])**int(i.partition('**')[2])
        else:
            product *= i
    return product


n = int(input('Введите число подлинней и разомнитесь, чай, кофе.. )) -> '))
start = time.time_ns()
print('Ok. I\'m trying.... Just a moment please!')
multipliers_list = decompose_by_numbers_multipliers(n)
print(f'\nThe number\'s multipliers are - {multipliers_list}\n')
stop = (time.time_ns() - start) / 1000000
print(f'Даже чайник не вскипел )) - ', stop, 'ms\n')

print(f'There is checking the solution. '
      f'Your number is {product_list_elements(multipliers_list)}\nAm I right?\n')
