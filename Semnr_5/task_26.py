# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
import os
os.system('cls')


# моя функция для возведения в степень
def raise_to_degree(base, index):
    if index == 0:
        return 1
    elif index < 0:
        return 1 / base * raise_to_degree(base, index + 1)
    else:
        return base * raise_to_degree(base, index - 1)


def negative_sign(x, y):
    if x > 0 : return '0.0'
    elif x == 0 : return 'Деление на 0 cannot be raised to a negative power'
    else:
        if y % 2 == 0: return '0.0'
        else: return '-0.0'


print('Функция годится как для положительных так и отрицательных чисел\nAre you ready', end='?')
if input(" (y/n) - ").upper() != 'Y':
    exit()
print()
A = int(input("Основание степени  A = "))
B = int(input("Показатель степени B = "))
try:
    print(f'\nРезультат {A} ** {B} = {raise_to_degree(A, B)} \n')
except:
    print(f'\nРезультат {A} ** {B} = {negative_sign(A, B)} \n')

print(f'Для сравнения стандартная pow ( {A} , {B} ) = {pow(A,B)}\nЯ был в шоке! )))\n')