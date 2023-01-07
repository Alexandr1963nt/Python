# Задача 103 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл file1.txt многочлен степени k.
import random
import os

os.system('cls')


def multiplier_с(mn, mx):
    multiplier_с = str(random.randint(mn, mx))
    return multiplier_с


def polynomial(k, c):
    # print (c,'*x**', k)
    if k == 0:
        if c == '0':
            row = ' = 0'
        else:
            row = ' + ' + c + ' = 0'
    elif k == 1:
        if c == '0':
            row = polynomial(k-1, multiplier_с(0, 100))
        elif c == '1':
            row = ' + ' + 'x' + polynomial(k-1, multiplier_с(0, 100))
        else:
            row = ' + ' + c + '*x' + polynomial(k-1, multiplier_с(0, 100))
    else:
        if c == '0':
            row = polynomial(k-1, multiplier_с(0, 100))

        elif c == '1':
            row = ' + ' + 'x**' + \
                str(k) + polynomial(k-1, multiplier_с(0, 100))

        else:
            row = ' + ' + c + '*x**' + \
                str(k) + polynomial(k-1, multiplier_с(0, 100))
    return row

k1 = int(input('Степень полинома №1  '))
k2 = int(input('Степень полинома №2  '))
polynom_1 = polynomial(k1, multiplier_с(1, 100))[3:]
polynom_2 = polynomial(k2, multiplier_с (1, 100))[3:]
print('\nСозданы полиномы\n')
print (polynom_1, polynom_2, sep='\n')

with open('additional_tasks/polynom_1.txt', 'w') as data:
    data.writelines(polynom_1)
with open('additional_tasks/polynom_2.txt', 'w') as data:
    data.writelines(polynom_2)
print('\nЗаписаны в файлы и считаны полиномы\n')
for i in range(1,3):
    path = 'additional_tasks/polynom_' + str(i) + '.txt'
    polynom = open(path, 'r')
    print(polynom.read())
    polynom.close()
