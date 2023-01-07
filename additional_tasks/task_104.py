# Задача 104. Даны два файла file1.txt и file2.txt, в каждом из которых находится
# запись многочлена (полученные в результате работы программы из задачи 103).
# Необходимо сформировать файл file_sum.txt, содержащий сумму многочленов.

import random
import os

os.system('cls')

def kj(row):
    k = int(row[row.rfind('*')+1:])
    return k

filo = open('additional_tasks/polynom_1.txt', 'r')
polynom_1 = filo.read()
filo.close()
print(polynom_1)

filo = open('additional_tasks/polynom_2.txt', 'r')
polynom_2 = filo.read()
filo.close()
print(polynom_2)

spl_1 = polynom_1[:-4].split(' + ')
spl_2 = polynom_2[:-4].split(' + ')

if len(spl_1) >= len(spl_2):
    l1 = spl_1
    l2 = spl_2
else:
    l1 = spl_2
    l2 = spl_1
result = [0]
count = 0
# result.append(0)
for i in [l1, l2]:
    for j in i:
        if j.find('x') == -1:           # строим элемент result[-1]
            count = 1
            result[0] += int(j)
            i.remove(j)
if result[0] == 0:  None #result[0] = ''
elif result[0] > 0:
    result[0] = str(result[0])            
for i in [l1, l2]:
    for j in i:
        if j.find('x') == len(j)-1:   # строим елемент result[-2]
            if count == 1:
                result.insert(0, 0)
                count = 2
            if j == 'x':
                result[0] += 1
                i.remove(j)
            else:
                j = j.split('*')
                result[0] += int(j[0])
                j = j[0]+'*x'
                i.remove(j)
if result[0] == 0:    result.pop(0)
elif result[0] == 1:    result[0] = 'x'
else :    
    result[0] = str(result[0]) + '*x'
 
k = max(int(l1[0][l1[0].rfind('*')+1:]), int(l2[0][l2[0].rfind('*')+1:]) )
for n in range(2, k+1):
    result.insert(0,0)
    for i in [l1, l2]:
        for j in i:
            Kj = kj(j)
            if n == kj(j):
                if j == 'x**' + str(n)   :
                    result[0] += 1
                    i.remove(j)
                else:
                    mplr = j.split('*x**')
                    result[0] += int(mplr[0])
                    i.remove(j)
    if result[0] == 0:   result.pop(0)
    elif result[0] == 1:
        result[0] = 'x**' + str(n)
    else:              
        result[0] = str(result[0]) + '*x**' + str(n)                
                    
result = ' + '  . join(result) + ' = 0'
print  (result)      

