import os
filepath = 'Semnr_7/'

def screen_clear():
    if input('\nПродолжим? - Y / Иное - выход:  ').upper() != 'Y':
        os.system('cls') 
        exit()
    os.system('cls')    
    
    
    
def read_data_from_file(name):
    result = []
    with open(name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n').split(','))
        return result
    
def print_data(read_data):
    for i in enumerate(read_data, 1):
        print(f'{i[0]}. ',end='' )
        print(' -'.join(i[1]))        
        
        # for j in i[1]:
        #     print('{} '.format(j), end='')  
        # print() 

def save_data_to_file(name, data_list):
    with open(name, 'a', encoding='utf8') as datafile:
        datafile.write(data_list +'\n')

def write_data (name, data_list):
    with open(name, 'w', encoding='utf8') as datafile:
        for element in data_list:
            datafile.write(','.join(element)+'\n')
            # datafile.write('{}\n'.format(element)) 


def print_bus():
    return read_data_from_file(filepath + 'bus.txt')

def add_bus():
    save_data_to_file(filepath + 'bus.txt', input("Введите параметры автобуса: "))
    
def print_driver():
    return read_data_from_file(filepath + 'driver.txt')

def add_driver():
    save_data_to_file(filepath + 'driver.txt', input("Введите водителя: "))

def print_route():
    return read_data_from_file(filepath + 'route.txt')

def add_route():
    save_data_to_file(filepath + 'route.txt', input("Введите маршрут: "))




