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

def SumElements(n, m):                    # - 1 вариант решения для str
    sum = 0                               # - 1 вариант решения для str
    for i in range(n, m):                 # - 1 вариант решения для str
        sum += int(ticket_number[i])      # - 1 вариант решения для str
    return sum                            # - 1 вариант решения для str

# def sum_number_digitals (number):                                   # 2 вариант для int
#     if (number // 10 == 0) : return number % 10                     # 2 вариант для int
#     else : return sum_number_digitals (number//10) + number % 10    # 2 вариант для int

are_you_happy = False
while are_you_happy == False:
    ticket_number = input('\nВведите № билета Например: \n385916 - счастливый\nили \n123456 - нет --> ')
    while len(ticket_number) % 2 != 0:
        ticket_number = input('\nВведите число с четным количеством цифр--> ')
    sum1 = SumElements(0, len(ticket_number)//2)                  # вычслить сумму цифр строки
    sum2 = SumElements(len(ticket_number)//2, len(ticket_number)) # по индексам в строке
    
    # ticket_num_int = int(ticket_number)                 # для варианта с int
    # sum1 = sum_number_digitals (ticket_num_int // 1000) # для варианта с int
    # sum2 = sum_number_digitals (ticket_num_int % 1000)  # для варианта с int

    if sum1 == sum2:
        are_you_happy = True
        print('\nСупер! Вам достался счастивый билет!' +
            f' {ticket_number[:len(ticket_number)//2]} => {sum1}. ' +
            f' {ticket_number[len(ticket_number)//2:len(ticket_number)]} => {sum2}.' +
            ' Приятного аппетита! :)\n')
    else:
        repeat = input(f'\nБилетик {ticket_number} не съедобный. Попробуйте ещё раз? ;)'
            '\nВведите любой символ + Enter для повторного ввода или "нет" для выхода --> ')
        if repeat.lower() == 'нет': are_you_happy = True