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

def SumElements(n, m):
    sum = 0
    for i in range(n, m):
        sum += int(ticket_number[i])
    return sum

are_you_happy = False
while are_you_happy == False:
    ticket_number = input('\nВведите № билета Например: \n385916 - счастливый\nили \n123456 - нет --> ')
    while len(ticket_number) % 2 != 0:
        ticket_number = input('\nВведите число с четным количеством цифр--> ')
    sum1 = SumElements(0, len(ticket_number)//2)
    sum2 = SumElements(len(ticket_number)//2, len(ticket_number) )
    if sum1 == sum2:
        are_you_happy = True
        print('\nСупер! Вам достался счастивый билет!' +
            f' {ticket_number[:len(ticket_number)//2]} => {sum1}.' +
            f' {ticket_number[len(ticket_number)//2:len(ticket_number)]} => {sum2}.' +
            ' Приятного аппетита! :)\n')
    else:
        repeat = input(f'\nБилетик {ticket_number} не съедобный. Попробуйте ещё раз? ;)'
            '\nВведите любой символ + Enter для повторного ввода или "нет" для выхода --> ')
        if repeat.lower() == 'нет': are_you_happy = True