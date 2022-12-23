# Задача 28:
# Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
import os
os.system('cls')

def sum_ab(a, b):
    if      a == 0 :    return b
    elif    b == 0 :    return a
    elif    a < 0  :    return -1 + sum_ab(a+1, 0) + 1 + sum_ab(0, b-1)
    elif    b < 0  :    return  1 + sum_ab(a-1, 0) - 1 + sum_ab(0, b+1)
    else :              return  1 + sum_ab(a-1, 0) + 1 + sum_ab(0, b-1)
    
print('Функция работает для положительных и отрицательных чисел\n')
num1 = int(input('Число №1 ?  '))
num2 = int(input('Число №2 ?  '))

c = sum_ab(num1, num2)
# print(f'\nСумма чисел ({num1}), ({num2}) составляет ({c})\n')

print(f'Сумма чисел "{num1}", "{num2}" составляет "{c}"\n')
    
