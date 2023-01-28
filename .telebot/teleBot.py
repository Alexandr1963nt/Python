# Done! Congratulations on your new bot. 
# You will find it at t.me/trfim63_bot 
import random
import os
import crosszero as cz
import tracemalloc
tracemalloc.start()
import calculate as clt
os.system('cls')

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

bot = ''
count = 1
val = ''
val_bot = ''
player = ''

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}\n'
                                    'Вам доступны команды\n/help\n/go\n/calc\n/game')

async def go(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Ok! Let\'s go together! {update.effective_user.first_name}')

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
    await update.message.reply_text ('Крестики /X - Нолики /0\n'
                                    f'Чем будете играть, {player}?')
    
async def start_game (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text
    mess = list(message)
    global val
    val = mess[1].upper()
    global val_bot  
    global count  
    if count == 1:
        (bot, val) = cz.hello_bot (val)
        if val == 'X':
            val_bot = '0'
        else: val_bot = 'X'
        if bot == 'pl_1':
            rez = cz.reread_form()
            (ky, phrase) = cz.bot_brain (rez, count, val_bot, bot)
            cz.cross_zero[f'{ky}'] = val_bot
            await update.message.reply_text(f'Бот первый! {phrase}')
            count = 2  
        count = 2
        cr = cz.cross_zero
        await update.message.reply_text(f'Ок! Let\'s go! {player}, Ваш ход.\n\n'
                                        f"|{cr['a1']}|{cr['a2']}|{cr['a3']}|\n"
                                        f"|{cr['b1']}|{cr['b2']}|{cr['b3']}|\n"
                                        f"|{cr['c1']}|{cr['c2']}|{cr['c3']}|\n\n"
                           f'{player}, куда ставим?\n\n'
                            f"|/a1|/a2|/a3|\n"
                            f"|/b1|/b2|/b3|\n"
                            f"|/c1|/c2|/c3|")                


async def step (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = list(update.message.text)
    ky = ''.join(mess[1:])    
    global val
    cz.cross_zero[f'{ky}'] = val
    rez = cz.reread_form()
    human_result = cz.watch_rez(rez)
    if human_result == 'Ничья':
        cr = cz.cross_zero# надо бы остановить  программу, но незнаю как ))
        await update.message.reply_text(f"|{cr['a1']}|{cr['a2']}|{cr['a3']}|\n"
                                        f"|{cr['b1']}|{cr['b2']}|{cr['b3']}|\n"
                                        f"|{cr['c1']}|{cr['c2']}|{cr['c3']}|\n\n"
                        f'Удачи! {player}. {cz.bot_phrases.get(random.randint(11,13))}\n\n')
    elif human_result : # Если тут конц - выводим результат. If нет - пропускаем
        cr = cz.cross_zero
        await update.message.reply_text(f'Поздравляю! {cz.bot_phrases.get(random.randint(9,13))}\n\n'
                                        f"|{cr['a1']}|{cr['a2']}|{cr['a3']}|\n"
                                        f"|{cr['b1']}|{cr['b2']}|{cr['b3']}|\n"
                                        f"|{cr['c1']}|{cr['c2']}|{cr['c3']}|\n\n")
        message = cz.result_message (human_result) 
        mes = ' '.join(message)      
        await update.message.reply_text(f'/{mes} {player}')
        
    else: # Следующим играет бот 
        rez = cz.reread_form()      
        (ky, phrase) = cz.bot_brain (rez, count, val_bot, bot)
        cz.cross_zero[f'{ky}'] = val_bot
        await update.message.reply_text(f'One moment! {phrase}\n')
        rez = cz.reread_form()
        bot_result = cz.watch_rez(rez)
        
        if bot_result == 'Ничья': # надо бы остановить  программу
            cr = cz.cross_zero# надо бы остановить  программу, но незнаю как ))
            await update.message.reply_text(f"|{cr['a1']}|{cr['a2']}|{cr['a3']}|\n"
                                            f"|{cr['b1']}|{cr['b2']}|{cr['b3']}|\n"
                                            f"|{cr['c1']}|{cr['c2']}|{cr['c3']}|\n\n"
                            f'{player}. {cz.bot_phrases.get(random.randint(5,6))} Ничья! /game\n\n')
        elif bot_result == 'Game over!' :
            cr = cz.cross_zero
            await update.message.reply_text(f'Супер! {cz.bot_phrases.get(random.randint(6,8))}\n\n'
                                            f"|{cr['a1']}|{cr['a2']}|{cr['a3']}|\n"
                                            f"|{cr['b1']}|{cr['b2']}|{cr['b3']}|\n"
                                            f"|{cr['c1']}|{cr['c2']}|{cr['c3']}|\n\n")
            message = cz.result_message (bot_result)
            mes = ' '.join(message)      
            await update.message.reply_text(f'/{mes} {player}')
        else:
            cr = cz.cross_zero
            await update.message.reply_text (   f'Ок! {cz.bot_phrases.get(random.randint(1,5))} \n\n'
                                                f"|{cr['a1']}|{cr['a2']}|{cr['a3']}|\n"
                                                f"|{cr['b1']}|{cr['b2']}|{cr['b3']}|\n"
                                                f"|{cr['c1']}|{cr['c2']}|{cr['c3']}|\n\n"
                                            
                                            f'Куда ходим, {player}?\n\n'
                                            f"|/a1|/a2|/a3|\n"
                                            f"|/b1|/b2|/b3|\n"
                                            f"|/c1|/c2|/c3|")                
    
    
async def help (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hi\n/go\n/calc\n/game')    

app = ApplicationBuilder().token("TOKEN").build()
print("Server start")

app.add_handler(CommandHandler("hi", hello))
app.add_handler(CommandHandler("go", go))
app.add_handler(CommandHandler("calc", calc))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("game", quest))
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

app.run_polling()
print("Server stop")