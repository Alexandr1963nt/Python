# Done! Congratulations on your new mbot. 
# You will find it at t.me/trfim63_bot 
import random
import os
import time
import crosszero as cz
import calculate as clt
os.system('cls')
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, CallbackContext


mbot = ''
count = 1
val = ''
val_bot = ''
player = ''

game_sweet = ''
candies = 0
portion = 0

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('*Какое такое хайло? Я Бот )) \n'
                                    f'Здравия желаю, {update.effective_user.first_name}! \n'
                                    '/help - общий список команд*\n', parse_mode = "Markdown")

async def go(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"_Ok! Let\'s go together! {update.effective_user.first_name}_\n", parse_mode = "Markdown")


async def sweet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global player
    global candies
    global game_sweet
    player = update.effective_user.first_name
    if game_sweet == '': 
        await update.message.reply_text(f'Поиграем с конфетами, *{player}*\n'
'''*Условие игры*\nНа столе лежит N конфет.\n
Игроки договариваются сколько конфет можно взять за 1 раз по очереди.\n
Выигрывает сделавший последний ход и ему достаются все конфеты ))''', parse_mode='Markdown')
        game_sweet = 'start'
    if candies == 0:
        await update.message.reply_text('\nСколько конфет разыгрывается?')

async def user_says (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = update.message.text
    # await update.message.reply_text(f'введен текст {mess}!', parse_mode = "Markdown")
    global player
    global candies
    global game_sweet
    global portion
    player = update.effective_user.first_name
    if mess.lower() == 'sweet':
        await sweet(update, context)
    # print('функция отработала')  
    elif mess.lower() == 'crest':
        await quest(update, context)
    elif game_sweet == 'start':
        if mess.isdigit():
            if candies == 0:
                candies = int(mess)
                await update.message.reply_text('Сколько max конфет можно брать за раз?')
            elif portion == 0:
                portion = int(mess)
                await update.message.reply_text( f"Итак! На кону {candies} конфет\n"
                                   f'Брать не более {portion} за раз.\n'
                                   'Уступаю Вам первый ход!\n'
                                   'Сколько конфет берёте?')
            else:
                score = int(mess)
                if score <= portion and score <= candies:
                    candies -= score
                    if candies == 0: 
                        await update.message.reply_text(f"{player}, Вы взяли последние конфеты и выиграли!")
                        player = ''
                        game_sweet = ''
                        candies = 0
                        portion = 0
                    else:
                        await update.message.reply_text(f"ОК. Вы оставили {candies} конфет на столе")
                        await update.message.reply_text(f"Мне надо подумать.\nОчень есть хочется ))")
                        time.sleep(2)
                        if candies <= portion: 
                            score = candies
                        else:
                            score = candies % (portion + 1)
                            if score == 0: score = 1
                        candies -= score
                        if candies == 0: 
                            await update.message.reply_text(f"{player}, я взял последние конфеты!\nОтдавайте все свои")
                            player = ''
                            game_sweet = ''
                            candies = 0
                            portion = 0
                        
                        else:
                            await update.message.reply_text(f"Тааакс, я взял {score} шт.\n"
                                            f'Осталось {candies}. Ваш ход\n'
                                            "Сколько берёте")
                else: 
                    await update.message.reply_text(f"Ай-яй! {score} взять низя!\n"
                                            f'Осталось {candies}. Повторите ход\n'
                                            "Сколько берёте")
    else:
        await update.message.reply_text( f'Что желаете, _{player}_?\n'
                       'Здесь можно поиграть:\n'
                       'отправьте мне Sweet или Crest\n'
                       'или нажмите /help', parse_mode='Markdown')


async def calc (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = update.message.text
    items = mess.split()
    a = ''.join(items[1:])
    if a == '':
        await update.message.reply_text(f'Сорян... введите\n/calc "что посчитать"\n'
                                        'Пример: "/calc (2+2)^3"')
    else:
        await update.message.reply_text(f'Result = {clt.expression(a)}')
      
async def quest (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global count
    count = 1
    global player
    player = update.effective_user.first_name
    for k in cz.cross_zero:
        other = [(k,'_')]
        cz.cross_zero.update(other)
    global mbot
    mbot = ''
    global val
    val = ''
    global val_bot
    val_bot = ''
    await update.message.reply_text (f'Чем играете, {player}?\n\n'
                                     '/X    или может     /0  ?')
    
async def start_game (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text
    mess = list(message)
    global val
    val = mess[1].upper()
    global val_bot  
    global count  
    if count == 1:
        global mbot
        (mbot, val) = cz.hello_bot (val)
        if val == 'X':
            val_bot = '0'
        else: val_bot = 'X'
        # print('mbot =', mbot)
        if mbot == 'pl_1':
            # print(f'В этой точке впервые перед bot_brain count д.б.1 = {count} и mbot д.б. pl_1 =', mbot)
            rez = cz.reread_form()
            (ky, phrase) = cz.bot_brain (rez, count, val_bot, mbot)
            cz.cross_zero[f'{ky}'] = val_bot
            await update.message.reply_text(f'{phrase} Я первый!')
            count = 2  
        cr = cz.cross_zero
        await update.message.reply_text(f'Ок! Let\'s go! {player}, Ваш ход.\n\n'
                                        f"\v|\t{cr['a1']}\t|\t{cr['a2']}\t|\t{cr['a3']}\t|\n"
                                        f"\v|\t{cr['b1']}\t|\t{cr['b2']}\t|\t{cr['b3']}\t|\n"
                                        f"\v|\t{cr['c1']}\t|\t{cr['c2']}\t|\t{cr['c3']}\t|\n\n"
                                    f'{player}, куда ставим?\n\n'
                                        f"\v|\t/a1\t|\t/a2\t|\t/a3\t|\n"
                                        f"\v|\t/b1\t|\t/b2\t|\t/b3\t|\n"
                                        f"\v|\t/c1\t|\t/c2\t|\t/c3\t|" )

async def step (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = list(update.message.text)
    ky = ''.join(mess[1:])    
    global val
    cz.cross_zero[f'{ky}'] = val
    rez = cz.reread_form()
    human_result = cz.watch_rez(rez)
    if human_result == 'Ничья':
        cr = cz.cross_zero# надо бы остановить  программу, но незнаю как ))
        await update.message.reply_text(f"\nХм ... ничья. Ещё /Game ?\n\n\v|\t{cr['a1']}\t|\t{cr['a2']}\t|\t{cr['a3']}\t|\n"
                                        f"\v|\t{cr['b1']}\t|\t{cr['b2']}\t|\t{cr['b3']}\t|\n"
                                        f"\v|\t{cr['c1']}\t|\t{cr['c2']}\t|\t{cr['c3']}\t|\n\n"
                            f'Удачи! {player}. {cz.bot_phrases.get(random.randint(11,13))}\n\n')
    elif human_result : # Если тут конц - выводим результат. If нет - пропускаем
        cr = cz.cross_zero
        await update.message.reply_text(f'Поздравляю! {cz.bot_phrases.get(random.randint(9,13))}\n\n'
                                        f"\v|\t{cr['a1']}\t|\t{cr['a2']}\t|\t{cr['a3']}\t|\n"
                                        f"\v|\t{cr['b1']}\t|\t{cr['b2']}\t|\t{cr['b3']}\t|\n"
                                        f"\v|\t{cr['c1']}\t|\t{cr['c2']}\t|\t{cr['c3']}\t|\n\n")
        message = cz.result_message (human_result) 
        mes = ' '.join(message)      
        await update.message.reply_text(f'/{mes} {player}')
    else: # Следующим играет бот 
        rez = cz.reread_form()
        global count   
        global mbot 
        # print (f'тут - перед заходом впервые в мозг бота count д.б. =1 = {count}, если mbot="pl_2" = {mbot}')
        (ky, phrase) = cz.bot_brain (rez, count, val_bot, mbot)
        cz.cross_zero[f'{ky}'] = val_bot
        if count == 1 : 
            # print (f'тут count д.б. =1 = {count} если mbot=pl_2 = {mbot}')
            count = 2
            # print ('тут count должен стать =2 =',count)
        await update.message.reply_text(f'{phrase}\n')
        rez = cz.reread_form()
        bot_result = cz.watch_rez(rez)
        if bot_result == 'Ничья': # надо бы остановить  программу
            cr = cz.cross_zero# надо бы остановить  программу, но незнаю как ))
            bot_says = cz.bot_phrases.get(random.randint(3,5))
            while bot_says == phrase:
                bot_says = cz.bot_phrases.get(random.randint(3,5))              
            await update.message.reply_text(f"\nБот жаждет new /game ! /\n\n"
                                            f"\v|\t{cr['a1']}\t|\t{cr['a2']}\t|\t{cr['a3']}\t|\n"
                                            f"\v|\t{cr['b1']}\t|\t{cr['b2']}\t|\t{cr['b3']}\t|\n"
                                            f"\v|\t{cr['c1']}\t|\t{cr['c2']}\t|\t{cr['c3']}\t|\n\n"
                            f'Ничья, {player}. {bot_says}\n\n')
        elif bot_result == 'Game over!' :
            cr = cz.cross_zero
            bot_says = cz.bot_phrases.get(random.randint(7,8))
            while bot_says == phrase:
                bot_says = cz.bot_phrases.get(random.randint(7,8))            
            await update.message.reply_text(f'Супер! {bot_says}\n\n'
                                            f"\v|\t{cr['a1']}\t|\t{cr['a2']}\t|\t{cr['a3']}\t|\n"
                                            f"\v|\t{cr['b1']}\t|\t{cr['b2']}\t|\t{cr['b3']}\t|\n"
                                            f"\v|\t{cr['c1']}\t|\t{cr['c2']}\t|\t{cr['c3']}\t|\n\n")
            message = cz.result_message (bot_result)
            mes = ' '.join(message)      
            await update.message.reply_text(f'/{mes} {player}')
        else:
            cr = cz.cross_zero
            bot_says = cz.bot_phrases.get(random.randint(2,6))
            while bot_says == phrase:
                bot_says = cz.bot_phrases.get(random.randint(2,6))
            await update.message.reply_text (f'{bot_says} \n\n'
                                        f"\v|\t{cr['a1']}\t|\t{cr['a2']}\t|\t{cr['a3']}\t|\n"
                                        f"\v|\t{cr['b1']}\t|\t{cr['b2']}\t|\t{cr['b3']}\t|\n"
                                        f"\v|\t{cr['c1']}\t|\t{cr['c2']}\t|\t{cr['c3']}\t|\n\n"
                                            f'Куда ходим, {player}?\n\n'
                                        f"\v|\t/a1\t|\t/a2\t|\t/a3\t|\n"
                                        f"\v|\t/b1\t|\t/b2\t|\t/b3\t|\n"
                                        f"\v|\t/c1\t|\t/c2\t|\t/c3\t|")
    
async def help (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}\n'
                                    'Вам здесь доступны команды:\n'
                                    '/help - общий список команд\n'
                                    '/go - просто для теста\n'
                                    '/calc (6+4)/3^2*-1 и т.д\n'
                                    '/game - игра в X-0 с ботом\n'
                                    '/sweet - игра на конфеты с ботом')   


app = ApplicationBuilder().token("token").build()
print("Server start")

app.add_handler(CommandHandler("hi", help))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("go", go))
app.add_handler(CommandHandler("calc", calc))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("start", help))
app.add_handler(CommandHandler("game", quest))
app.add_handler(CommandHandler("sweet", sweet))
app.add_handler(CommandHandler("x", start_game))
app.add_handler(CommandHandler("0", start_game))
app.add_handler(CommandHandler("a1", step))
app.add_handler(CommandHandler("a2", step))
app.add_handler(CommandHandler("a3", step))
app.add_handler(CommandHandler("b1", step))
app.add_handler(CommandHandler("b2", step))
app.add_handler(CommandHandler("b3", step))
app.add_handler(CommandHandler("c1", step))
app.add_handler(CommandHandler("c2", step))
app.add_handler(CommandHandler("c3", step))
app.add_handler(MessageHandler(filters.TEXT , user_says))



app.run_polling()
print("Server stop")