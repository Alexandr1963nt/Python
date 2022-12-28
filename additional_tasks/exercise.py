import os
import time
os.system('cls')
import random

player1 = str(random.randint(1,2)).join(['pl_',''])
if player1 == 'pl_1':
        player2 = 'pl_2'
else:     
        player2 = 'pl_1'
locals()[player1] = input('Здравствуйте! Как Вас зовут? Смелей! ')
print(f'Очень приятно, {locals()[player1]}!')
locals()[player2] = input('Кто следующий сластёна? Не стесняйтесь, '
                               'представьтесь пожалуйста! ')
print(f'Привестствую Вас, {locals()[player2]}!\n')
portion = 5
print(f'{pl_2} и {pl_1}, напоминаю, вы договорились брать не более {portion} за раз')
