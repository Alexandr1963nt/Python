import os
import time

# Создать телефонный справочник 

# записываем в файл
def writeFile(fname, dct):
    with open(fname, 'w', encoding='utf8') as data:
        for key,val in dct.items():
            data.write('{}:{}\n'.format(key,val))        
        
# читаем словарь из файла как type = dict
def readFile(fname):
    result = {}
    with open(fname, 'r', encoding='utf8' ) as inp:
        for line in inp.readlines():
            key,val = line.strip().split(':')
            result[key] = val
    return result

def print_dict(fname):
    with open(fname, 'r', encoding='utf8' ) as inp:
        for line in inp.readlines():
            key,val = line.strip().split(':')
            print('{} - {}'.format(key, val))
            
def search_abonent(fname, abonent):
    abonent = abonent.upper()
    with open(fname, 'r', encoding='utf8' ) as inp:
        found_num = tuple(enumerate([line.strip().split(':') 
        for line in inp.readlines() if abonent in line.upper()], start = 1))
        for ind, [key, val] in found_num: 
            print('{}. {} - {}'.format(ind, key, val))
    return found_num
def del_founditem(found_num, fname, dict_phones, message):
    will_del_item = int(input(f'Выбрать № строчки - {message}  '))
    if input((f'{message} номер телефона' +
              f' {found_num[will_del_item -1][1][0]}? y/n  ')).upper() == 'Y':
        return delete_phone(fname, dict_phones, found_num[will_del_item -1][1][0])
    else:
        os.system('cls') 
        exit()

    

def add_item(fname, dict_phones, person=''):
    new_key = input('Новый телефон  ')
    if person == '': new_val = input('ФИО абонента  ')
    else: new_val = person
    other = [(new_key,new_val)]
    dict_phones.update(other) 
    writeFile(fname, dict_phones)
    
def delete_phone(fname, dict_phones, phone):
    redact_contact = dict_phones.pop(phone)
    writeFile(fname, dict_phones)
    return redact_contact

def found_empty():
    print ('Некорректный ввод')
    if input('\nПродолжим? - Y / Иное - выход:  ').upper() != 'Y':
        exit()
    os.system('cls') 
    

        #основной блок
def main_menu():        
    menu = ('1 - Показать все записи\n'+
            '2 - Добавить новый контакт\n'+
            '3 - Поиск по имени или телефону\n'+
            '4 - Найти и удалить контакт\n'+
            '5 - Удалить запись номеру телефона\n'+
            '6 - Изменить номер телефона у контакта\n'+
            '0 - Выход')
    while True:
        print(menu)
        action = input('Что сделать? -> ')
        match action:
            case "1":
                # Показать все записи
                os.system('cls')
                print_dict(filename)
                if input('\nПродолжим? - Y / Иное - выход:  ').upper() != 'Y':
                    exit()
                os.system('cls')
            case "2":
                # Добавить новый контакт
                read_phone = readFile(filename)
                os.system('cls')
                add_item(filename, read_phone)
                os.system('cls')
            case "3":
                # Поиск по имени или телефону
                os.system('cls')
                find = input('Кого ищем?  ')
                found = search_abonent(filename, find)
                if found == (): 
                    found_empty()
                if input('\nПродолжим? - Y / Иное - выход:  ').upper() != 'Y':
                    exit()
                os.system('cls')                
            case "4":
                # поиск для удаления
                os.system('cls')
                find = input('Кого ищем?  ')
                found_nums = search_abonent(filename, find)  
                if found_nums == (): 
                    found_empty()
                    continue                                  
                del_founditem(found_nums, filename, readFile(filename), 'Удалить')
                os.system('cls')
            case "5":
                # Удалить запись номеру телефона
                os.system('cls')
                print_dict(filename)
                del_phone = input('\nудалить телефон №  ')
                try:    
                    delete_phone(filename, readFile(filename), del_phone)
                    print('Исполнено') 
                except: 
                    print('Неверный номер. Повторите операцию') 
                time.sleep(1.5)
                os.system('cls')
            case "6":
                # Изменить номер телефона у контакта 
                read_phone = readFile(filename)
                os.system('cls')       
                find = input('Кого ищем?  ')
                found_nums = search_abonent(filename, find)
                if found_nums == (): 
                    found_empty()
                    continue    
                try:                              
                    person = del_founditem(found_nums, filename, read_phone, 'Изменить')
                    add_item(filename, read_phone, person) 
                    print('Слушаюсь и повинуюсь :)')  
                except:   
                    print('Некорректные действия. Попробуйте еще раз') 
                    exit()
                time.sleep(1.5)
                os.system('cls')                             
            case "0":
                exit()

filename = 'Semnr_6/phonesnumber.txt'
read_phone = readFile(filename)

os.system('cls')

main_menu()