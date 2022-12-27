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


def check_simple_multiplier(N): # проверка числа на простоту
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
                while N % k == 0:
                    N = N // k
                if check_simple_multiplier(N):   
                    k = N           
            if k != N:  
                k += 1  

        m = sorted(set(m))
        return (list(m))


n = int(input('Введите число подлинней и разомнитесь, чай, кофе.. )) -> '))
start = time.time_ns()
print('Ok. Работаю')
print(f'\n{decompose_by_numbers_multipliers( n )}\n')
stop = (time.time_ns() - start) / 1000000
print(stop, 'ms\n')
