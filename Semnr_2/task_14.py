# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.
N = int(input('Введите целое число -> '))
def list_2_to_N (y):
    str = list(range(y+1))
    for i in str:
        str[i] = pow(2, i)
    return str
import math 
print(list_2_to_N (math.floor(math.log2(N))))
