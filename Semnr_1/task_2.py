# Задача 2
# Найдите сумму цифр трехзначного числа.
# Решение годится для числа любой разрядности
input_number = int(input('\nВведите целое число -> '))
if input_number < 0:    number = - input_number
else:    number = input_number
sum_number_digitals = 0
while number > 0:
    digital = number % 10
    sum_number_digitals += digital
    number //= 10
print(f'\nСумма цифр числа {input_number} равна {sum_number_digitals}\n')