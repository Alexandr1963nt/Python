# Задача 107 Создайте программу для игры в ""Крестики-нолики"" (Добавьте игру против бота)
import random
import os

os.system('cls')

def form(dct):
    cz = dct
    print(' ', end='')
    for i in range(1, 4):
        print('', i, end='')
    for i in 'abc':
        print(f'\n{i}|', end='')
        for j in range(1,4):
            print(f"{cz[f'{i}{j}']}|", end='')
    print('\n')

cross_zero = {
    'a1': '1',
    'a2': '2',
    'a3': '3',
    'b1': '4',
    'b2': '5',
    'b3': '6',
    'c1': '7',
    'c2': '8',
    'c3': '9'
}

line_a = cross_zero['a1'], cross_zero['a2'], cross_zero['a3']
line_b = cross_zero['b1'], cross_zero['b2'], cross_zero['b3']
line_c = cross_zero['c1'], cross_zero['c2'], cross_zero['c3']
line_1 = cross_zero['a1'], cross_zero['b1'], cross_zero['c1']
line_2 = cross_zero['a2'], cross_zero['b2'], cross_zero['c2']
line_3 = cross_zero['a3'], cross_zero['b3'], cross_zero['c3']
dgnl_1 = cross_zero['a1'], cross_zero['b2'], cross_zero['c3']
dgnl_2 = cross_zero['a3'], cross_zero['b2'], cross_zero['c1']

rez = line_a, line_b, line_c, line_1, line_2, line_3, dgnl_1, dgnl_2

for l in rez:
    print(''.join (l) )  
 
# while True:
#     form(cross_zero)
#     cell = input('Укаать ячейку со значением через пробел. Пример: "a1 X"  ' ).split()
#     ky, val = cell
#     if cross_zero[f'{ky}'] != ' ':
#         cross_zero[f'{ky}'] = val
#     else: 
#         print('Ууупссс. Клетка заполнена. переход хода ))')
print(''.join (line_a) )
