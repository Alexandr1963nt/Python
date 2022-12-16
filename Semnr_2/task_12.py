# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
def search_x(S, P, max):
    for i in range(1, max):
        if S-i == P/i : 
            y = i
            x = S - y
            m = [x, y]
    return m

def square_equations_roots (A, B, C):
    import math
    roots = []
    a = A
    b = B
    c = C
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = int((-b + math.sqrt(discr)) / (2 * a))
        x2 = int((-b - math.sqrt(discr)) / (2 * a))
        return roots + [x1, x2]
    elif discr == 0:
        return roots + [-b / (2 * a)]
    else:
        print("Корней нет")
    
import random
max_range = 1000
x = random.randint(1,max_range)
y = random.randint(1,max_range)
print(f'\nПетя загадал числа {x}, {y}, подсказал Кате их сумму {x+y} и произведение {x*y}')  
nums = search_x (x+y, x*y, max_range)
print (f'\n"Катя" всю ночь подбирала числа, для которых S = {sum(nums)}, P = {nums[0]*nums[1]} -> {nums} \n')
print(f'А под утро вспомнила забытую за 40 лет алгебру и решила квадратное уравнение ))\n{square_equations_roots (-1, x+y, -x*y)}\n')
