import os
import function as fu
import time

# bus = fu.print_bus() 
# driver = fu.print_driver()
# route = fu.print_route()

def driver_bus (buses, drivers, routes):
    print('Список закрепления автобусы-водители\n')
    bus_num = input('Введите гос.номер автобуса  ').upper()
    print()
    bus = [ b for b in buses if b[1].strip() == bus_num]
    routes_bus = [(bus[0][1],r[2:]) for r in routes if r[2].strip() == bus[0][0]]  
    result = []
    for r in routes_bus:
        res_bus = r[0].strip()
        for d in drivers:
            if r[1][1].strip() == d[0]:
                res_drv = d[1]
                result.append((res_bus, res_drv))
    for p in result:    
        print('{} {}'.format(p[0], p[1]))
        
        
def delete_data(read_data, filename):
    fu.print_data(read_data)
    delete = int(input('№ удаляемой записи?  '))-1
    if input (f'{",".join(read_data.pop(delete))} будет удален. Y/N ?  ').upper() != 'Y':
        print('\nОк. Не будем торопиться ))')
        time.sleep(2)
        return
    else: fu.write_data (filename, read_data)