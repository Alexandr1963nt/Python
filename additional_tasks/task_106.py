# Задача 106 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# (Добавьте игру против бота)
import random
import os
import time

os.system('cls')


def sweets_demo(candies, max_handful):
    print('Игроки вводят свои имена, происходит жеребьёвка очередности хода')
    sweets = candies
    pl_1 = 'Игрок 1'
    print(f'Очень приятно, {pl_1}!')
    pl_2 = 'Игрок 2'
    print(f'Привестствую, {pl_2}!\n')
    print(f"Итак! На кону {sweets} конфет. Погнали!")
    portion = random.randint(1, max_handful)
    print(f'{pl_2} и {pl_1} передоговорились брать не более {portion} за раз')
    print(f'Для победы 1 игроку рекомендуется взять {sweets % (portion + 1)} шт.')
    player1 = sweets % (portion + 1)
    print(f"{pl_1} взял {player1} шт.")
    sweets -= player1
    print(f"Осталось {sweets} конфет")
    
    while sweets > 0:
        player2 = random.randint(1, portion)
        print(f"{pl_2} взял {player2} шт.")
        sweets -= player2
        if sweets == 0 : winner = pl_2
        print(f"Осталось {sweets} конфет")
        player1 = sweets % (portion + 1)
        print(f'{pl_1} взял от оставшихся конфет {player1} шт.')
        sweets -= player1
        if sweets == 0 : winner = pl_1
    return sweets, winner

def sweets_two (candies, max_handful):
    sweets = candies
    player1 = str(random.randint(1,2)).join(['pl_',''])
    if player1 == 'pl_1':
        player2 = 'pl_2'
    else:     
        player2 = 'pl_1'
    globals()[player1] = input('Здравствуйте! Как Вас зовут? Смелей! ')
    print(f'Очень приятно, {globals()[player1]}!')
    globals()[player2] = input('Кто следующий сластёна? Не стесняйтесь, '
                               'представьтесь пожалуйста! ')
    print(f'Привестствую Вас, {globals()[player2]}!\n')
    portion = max_handful
    print(f'{pl_2} и {pl_1}, напоминаю, вы договорились брать не более {portion} за раз')
    print(f'Для победы 1 игроку рекомендуется взять {sweets % (portion + 1)} шт.')
    print(f"По результатам жеребьёвки, право первого хода получает  ", end='')
    for i in range(8):
        i = time.sleep(.2), print('.',end='')
    print (f' {pl_1}!')
    print(f"Итак! На кону {sweets} конфет. Погнали!")
    
    # while True :
    #     score_1 = int(input(f'{pl_1}, cколько конфет берете?  '))
    #     if score_1 > portion :
    #         print(f'Упссс. {pl_1}, можно взять не более {portion}! Верните лишние ))')
    #     else: break
    # print(f"{pl_1} взял {score_1} шт.")
    # sweets -= score_1
    # print(f"Осталось {sweets} конфет")
    # if sweets == 0 : 
    #     winner = pl_1
    #     return sweets, winner
    
    while sweets > 0:
        while True :
            score_1 = int(input(f'{pl_1}, Ваш ход. Берите конфеты  '))
            if score_1 > portion or sweets - score_1 < 0 :
                print(f'{pl_1}, можно взять максимум {min(portion,sweets)} шт! ))')
            else: break
        print(f'{pl_1} взял от оставшихся конфет {score_1} шт.')
        sweets -= score_1
        if sweets == 0 : 
            winner = pl_1
            break
        print(f"Осталось {sweets} конфет")        
        
        while True :
            score_2 = int(input(f'{pl_2}, Вы следующий. Берите конфеты  '))
            if score_2 > portion or sweets - score_2 < 0 :
                print(f'{pl_2}, доступно не более {min(portion,sweets)} шт! Верните лишние ))')
            else: break
        print(f"{pl_2} взял {score_2} шт.")
        sweets -= score_2
        if sweets == 0 : 
            winner = pl_2
            break
        print(f"Осталось {sweets} конфет")
        

    return sweets, winner


def sweets_bot (candies, max_handful):
    sweets = candies
    pl_1 = input('Смелей! Представьтесь. Как Вас зовут? ')
    pl_2 = 'Ваш Компъютер' 
    print(f'Очень приятно, {pl_1}! Я, {pl_2}, приветствую Вас!\n')
    print(f"Итак! На кону {sweets} конфет. Погнали!")
    portion = max_handful
    print(f'Мы договорились брать не более {portion} за раз. Уступаю Вам первый ход')
    print(f'И даже подскажу Вам взять {sweets % (portion + 1)} шт. конфет для победы')
    while True :
        player1 = int(input(f'{pl_1}, сколько конфет берёте?  '))
        if player1 > portion :
            print(f'Упссс. Договаривались не более {portion}! Верните лишние ))')
        else: break
    sweets -= player1
    print(f"Вы оставили {sweets} конфет на столе")
    
    while sweets > 0:
        player2 = random.randint(1, portion)
        print(f"Тааакс, я беру {player2} шт. {pl_1}, Ваш ход.")
        sweets -= player2
        if sweets == 0 : 
            winner = pl_2
            break
        print(f"Всё ещё есть {sweets} конфет. Думайте хорошо, чайник греется")
        
        player1 = int(input(f'{pl_1}, советую Вам взять {sweets % (portion + 1)} шт.\n'
                            'Сколько берёте? '))
        sweets -= player1
        if sweets == 0 : 
            winner = pl_1
            break
        
        player2 = sweets % (portion + 1)
        print(f"Угу.. осталось {sweets}. Мы с фиксиками попробуем {player2} шт. Они любят сладкое ))")
        sweets -= player2
        if sweets == 0 : 
            winner = pl_2
            break
        print(f"Осталось {sweets} шт. Берите быстрей, а то фиксики чаю с конфетами очень хотят!")

        player1 = int(input(f'{pl_1}, я бы взял {sweets % (portion + 1)}, а Вы сколько берёте? '))
        sweets -= player1
        if sweets == 0 : 
            winner = pl_1
            break
        print(f"В сладком остатке {sweets} шт. Неужели моя видеокарта зря кипятилась!")
        
    return sweets, winner

candies = int(input('Сколько конфет разыгрывается? '))
portion = int(input('Максимум можно взять за раз ? '))

mode = int(input ('Выбрать  режим игры: Демо - 1 / На двоих - 2 / С ботом - 3  '))
if mode == 1:
    cort = sweets_demo (candies, portion)
elif mode == 2:
    cort = sweets_two (candies, portion)
else:
    cort = sweets_bot (candies, portion)
    
candies, winner, loser = cort
print(f'Поздравляем! {winner} выиграл.\n'
      f'{loser} не грусти, {winner} поделится с тобой своими {candies} конфетами.\n')