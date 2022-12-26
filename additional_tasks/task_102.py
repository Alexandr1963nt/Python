# Задача 102
# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
## Задача 102 Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# (Основная теорема арифметики утверждает, что каждое натуральное число n>1 можно 
# факторизовать (разложить) в виде n= p1*...pk.
# Нахождение простых множителей числа 864. Сокращённый способ написания — 2**5 × 3**3)
# Первые: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37

import os
import time
os.system('cls')

def multiplier(N):
    i=2
    j=0
    while i*i <= N and j != 1:
        if N % i == 0:
            j = 1
        i += 1
    if j != 1:
        return N
    else :
        return None

# def multiplier_number(N):
#     m = list()
#     if N == 1 : 
#         return list()
#     else:
#         i = 2
#         while i in range(2,N+1):
#             if N % i == 0:
#                 m.append(i)
#                 N = N // i 
#                 while N % i == 0 :
#                     N = N // i
#             i += 1
#         for k in range(0,len(m)):
#             for j in range(k+1,len(m)): 
#                 if m[j] % m[k] == 0:
#                     m[j] = m[k]
#         m = set(m)
#         return(list(m)) 

def multiplier_number(N):
    m = list()
    if multiplier(N):
        m = [N]
        return m
    else :
        k = 2
        while k in range(2,N+1):
            if N % k == 0:
                m.append(k)
                N = N // k 
                while N % k == 0 :
                    N = N // k
            k += 1
        # for f in range(0,len(m)):
        #     for g in range(f+1,len(m)): 
        #         if multiplier(m[g]): 
        #             None
        #         elif m[g] % m[f] == 0:
        #             m[g] = m[f]
        m = sorted(set(m))
        return(list(m)) 

# def multiplier_number(N):
#     m = list()
#     if N == 1 : 
#         return list()
#     else:
#         i = 2
#         while i in range(2,N+1):
#             if N % i == 0:
#                 m.append(i)
#                 N = N // i 
#                 while N % i == 0 :
#                     N = N // i
#             i += 1
#         for k in range(0,len(m)):
#             for j in range(k+1,len(m)): 
#                 if m[j] % m[k] == 0:
#                     m[j] = m[k]
#         m = set(m)
#         return(list(m)) 
start = time.time_ns()
n = int(input('число -> '))
print(multiplier_number(n))
stop = (time.time_ns() - start) /1000000
print(stop)