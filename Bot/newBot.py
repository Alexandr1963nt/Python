import telebot
import os
import time
# import candies as sw
os.system('cls')

mybot = telebot.TeleBot("token") # <--  сюда вставить токен
print("Server start")
player = ''
game = ''
candies = 0
portion = 0


@mybot.message_handler(commands=['start', 'hello', 'hi', 'Hi', 'Hello'])
def start(message):
    global player
    player = message.from_user.first_name
    mybot.send_message(message.chat.id, f'Привет, *{player}*\n'
                       'отправьте любой символ\n' 
                       'для получения информации\n'
                       'о доступных функциях', parse_mode='Markdown')

@mybot.message_handler(commands=['Sweet', 'here'])
def sweet(message):
    global player
    global candies
    global game
    player = message.from_user.first_name
    if game == '': 
        mybot.send_message(message.chat.id, f'Поиграем с конфетами, *{player}*\n'
                       'излагаю правила игры\nбла-бла-бла', parse_mode='Markdown')
        game = 'start'
    if candies == 0:
        mybot.send_message(message.chat.id,'Сколько конфет разыгрывается?')
    
    
@mybot.message_handler()
def get_user_text (message):
    global player
    global candies
    global game
    global portion
    player = message.from_user.first_name
    if message.text.lower() == 'sweet':
        sweet(message)
    elif game == 'start':
        if message.text.isdigit():
            if candies == 0:
                candies = int(message.text)
                mybot.send_message(message.chat.id,'Сколько max конфет можно '
                                   'взять за раз?')
            elif portion == 0:
                portion = int(message.text)
                mybot.send_message(message.chat.id, f"Итак! На кону {candies} конфет\n"
                                   f'Брать не более {portion} за раз.\n'
                                   'Уступаю Вам первый ход. Погнали!\n'
                                   'Сколько конфет берёте?')
            else:
                score = int(message.text)
                candies -= score
                if candies == 0: 
                    mybot.send_message(message.chat.id,f"{player}, Вы взяли последние конфеты и выиграли!")
                    player = ''
                    game = ''
                    candies = 0
                    portion = 0
                else:
                    mybot.send_message(message.chat.id,f"ОК. Вы оставили {candies} конфет на столе")
                    mybot.send_message(message.chat.id,f"Мне надо подумать.\nОчень есть хочется ))")
                    time.sleep(2)
                    if candies <= portion: 
                        score = candies
                    else:
                        score = candies % (portion + 1)
                        if score == 0: score = 1
                    candies -= score
                    if candies == 0: 
                        mybot.send_message(message.chat.id,f"{player}, я взял последние конфеты!\nОтдавайте все свои")
                        player = ''
                        game = ''
                        candies = 0
                        portion = 0
                    
                    else:
                        mybot.send_message(message.chat.id,f"Тааакс, я взял {score} шт.\n"
                                        f'Осталось {candies}. Ваш ход\n'
                                        "Сколько берёте")
    else:
        mybot.send_message(message.chat.id, f'Что желаете, _{player}_?\n'
                       'Здесь можно поиграть:\n'
                       'отправьте мне слово Sweet\n'
                       'или нажмите /here', parse_mode='Markdown')
    
mybot.polling(none_stop = True)
# print ('player', player)
print("Server stop")