# Задача 101 Вычислить число π c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141    0.1 ≤ d ≤ 0.00000000001

import os
os.system('cls')


def Leibniz_series(d):        # ряд Лейбница не более 7 - сильно тормозит
    rate = 10**d
    pi = 0
    pi_next = pi
    k = 1
    i = 1
    try:
        while True:  # pi != π:
            if k == 1:
                pi_next += 4/i
                k = 2
            else:
                pi_next -= 4/i
                k = 1
            if pi*rate//1 != pi_next*rate//1:
                i += 2
                pi = pi_next
            else:
                break
        return i, pi_next
    except:
        print('Leibniz_series не шмогла ...')
        return i, pi_next

# ряд Нилаканта Nilacanta row
# π_Nilacanta_ряд = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - 4/(12*13*14)
def π_Nilacanta_row(d):
    rate = 10**d
    π = 3
    π_next = π
    i = 2
    k = 1
    try:
        while True:
            divisor = i*(i+1)*(i+2)
            if k == 1:
                π_next += 4/divisor
                k = 2
            else:
                π_next -= 4/divisor
                k = 1
            if π*rate//1 != π_next*rate//1:
                i += 2
                π = π_next
            else:
                break
        return i, π_next
    except:
        print('Упссс ... Nilacanta ряд не сдюжил')
        return i, π_next


π = 3.1415926535897932384626433832795
d = int(input('Введите требуемую точность расчёта в '
              'диапазоне 1 ≤ d ≤ 14 знаков после запятой -> '))
if d > 14:
    if input(f'Введенное начение {d} превышает установленное ограничение ≤ 14.\n'
         'Продолжим без гарантии точности расчёта ради любопытства?  Y/N  ').upper() == 'Y': 
        print(f'\nOk! Всё для Вас! Пытаюсь вычислить "π" c точностью до {d} знака\n')
    else: 
        print('Выхожу! А Вы попробуйте перезапустить программу с новым условием. До скрой встречи!')
        exit()    

print(f'\nOk! Вычисляю "π" c точностью до {d} знака\n')

j, π_Nilacanta = π_Nilacanta_row(d)
print(f'Из википедии  π = {round(π, d)}\n'
      f'Моё π Nilacanta = {round(π_Nilacanta, d)} на {j} шаге ряда Нилаканта')
if d > 7:
    print('\nРяд Лейбница для разрядности > 7 сильно тормозит, поэтому соответствующая функция не вызвана\n')
else:
    i, π_Leibniz = Leibniz_series(d)
    print(f'Моё  πи Leibniz = {round(π_Leibniz, d)} на {i} шаге ряда Лейбница\n')
