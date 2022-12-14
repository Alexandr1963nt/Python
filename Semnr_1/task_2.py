# Задача 2
# Найдите сумму цифр трехзначного числа.
# Решение годится для числа любой разрядности
input_number = int(input('\nВведите целое число -> '))  # Общая часть
if input_number < 0:    number = - input_number         # Общая часть
else:    number = input_number                          # Общая часть
# Первый вариант решения через рекурсию
def sum_number_digitals (number):
    if (number // 10 == 0) : return number % 10
    else : return sum_number_digitals (number//10) + number % 10
print(f'\nСумма цифр числа {input_number} рекурсией равна {sum_number_digitals(number)}')
# Второй вариант решения через while
sum_number_digit_while = 0
while number > 0:
    digital = number % 10
    sum_number_digit_while += digital
    number //= 10
print(f'\nСумма цифр числа {input_number} циклом while равна {sum_number_digit_while}\n')   
