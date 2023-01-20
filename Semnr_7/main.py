import function as fn
import selection as sn
import os

f_bus = fn.filepath + 'bus.txt'
f_drv = fn.filepath + 'driver.txt'
f_rte = fn.filepath + 'route.txt'

def select_item (menu, questin):
    os.system('cls')
    for i in menu:
        print(i[0],i[1])
    action = input(f"\nЧто {questin}?  ")
    return action

menuitems = [
        ("1", "Показать"),
        ("2", "Добавить"),
        ("3", "Связка bus-drivers"),
        ("4", "Удалить"),
        ("0", "Выйти")]

submenuitems = [
        ("1", "Автобусы"),
        ("2", "Водителей"),
        ("3", "Маршруты"),
        ("0", "Выйти")]

os.system('cls')

c = ''
while True:
    if c != '': fn.screen_clear()
    text = select_item(menuitems, ',новый хозяин, надо')
    if text == '0':
        os.system('cls')
        # exit()
        break
    elif text == '1': # показать
        action = select_item(submenuitems, 'показать')
        match action:
            case "1":   # "Автобусы"
                os.system('cls')
                fn.print_data(fn.print_bus())                
            case "2":   # Водители
                os.system('cls')
                fn.print_data(fn.print_driver())                
            case "3":   # Маршруты        
                os.system('cls')
                fn.print_data(fn.print_route())        
            case "0":   # Выход
                os.system('cls')
                exit()                     
    elif text == '2': # Добавить
        action = select_item(submenuitems, 'добавить')
        match action:
            case "1":   # "Автобусы"
                os.system('cls')
                fn.add_bus()             
            case "2":   # Водители
                os.system('cls')
                fn.add_driver()               
            case "3":   # Маршруты        
                os.system('cls')
                fn.add_route()        
            case "0":   # Выход
                os.system('cls')
                exit()  
    elif text == '3': # вывести связку бас-драйвер
        os.system('cls')
        bus = fn.print_bus() 
        driver = fn.print_driver()
        route = fn.print_route()
        # try:
        sn.driver_bus(bus, driver, route)
        # except: print('Неверный ввод. Попробуйте снова' )
    elif text == '4':   # Удалить
        while True:
            action = select_item(submenuitems, 'удалить')
            try:
                match action:
                    case "1":   # "Автобусы"
                        os.system('cls')
                        bus = fn.print_bus()
                        sn.delete_data(bus, f_bus)             
                    case "2":   # Водители
                        os.system('cls')
                        driver = fn.print_driver()
                        sn.delete_data(driver, f_drv)               
                    case "3":   # Маршруты        
                        os.system('cls')
                        route = fn.print_route()
                        sn.delete_data(route, f_rte)        
                    case "0":   # Выход
                        os.system('cls')
                        break
            except: print('Неверный ввод. Попробуйте снова' )
    c = 'next'
