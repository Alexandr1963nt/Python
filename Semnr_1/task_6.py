# Задача 6
# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

are_you_happy = False
while are_you_happy == False:
    ticket_number = input('\nВведите № билета Например: \n385916 - счастливый\nили \n123456 - нет --> ')
    while len(ticket_number) % 2 != 0:
        ticket_number = input('\nВведите число с четным количеством цифр--> ')
    summa1 = 0
    summa2 = 0
    for i in range(len(ticket_number)//2):
        summa1 += int(ticket_number[i])
    for j in range(len(ticket_number)//2, len(ticket_number)):
        summa2 += int(ticket_number[j])
    if summa1 == summa2:
        are_you_happy = True
        print('\nСупер! Вам достался счастивый билет!' +
            f' {ticket_number[:len(ticket_number)//2]} => {summa1}.' +
            f' {ticket_number[len(ticket_number)//2:len(ticket_number)]} => {summa2}.' +
            ' Приятного аппетита! :)\n')
    else:
        repeat = input(f'\nБилетик {ticket_number} не съедобный. Попробуйте ещё раз? ;)'
            '\nВведите любой символ + Enter для повторного ввода или "нет" для выхода --> ')
        if repeat.lower() == 'нет': are_you_happy = True