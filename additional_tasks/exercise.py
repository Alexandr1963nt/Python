import os
import time
os.system('cls')

def product_list_elements(lst) :
    product = 1
    for i in lst :
        if type(i) == str:
            product *= int(i.partition('**')[0])**int(i.partition('**')[2])
        else :
            product *= i
    return product
        

l = ['3**3', 41, 312199, 289312860898216427]     

print(product_list_elements(l))   