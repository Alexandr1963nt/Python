# Done! Congratulations on your new bot. 
# You will find it at t.me/trfim63_bot 
import random
import time
import os
import crosszero as cz
import tracemalloc
tracemalloc.start()
import calculate as clt
os.system('cls')

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}\n'
                                    'Вам доступны команды\n/help\n/go\n/calc')

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
    await update.message.reply_text ('Крестики /X - Нолики /0\n'
                                    'Чем будете играть ?')


async def form (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    cr = cz.cross_zero
    await update.message.reply_text (   'Ок! Let\'s go! \n\n'
                                        f"| {cr['a1']} | {cr['a2']} | {cr['a3']} |\n"
                                        f"| {cr['b1']} | {cr['b2']} | {cr['b3']} |\n"
                                        f"| {cr['c1']} | {cr['c2']} | {cr['c3']} |\n\n"
                                    
                                    'Куда ставите?\n\n'
                                     f"| /a1 | /a2 | /a3 |\n"
                                     f"| /b1 | /b2 | /b3 |\n"
                                     f"| /c1 | /c2 | /c3 |")
    
async def start_game (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text
    mess = list(message)
    val = mess[1].upper()    
    count = 1
    # while True:
    if count == 1:
            (bot, val) = cz.hello_bot (val)
            player = update.effective_user.first_name
            if val == 'X':
                val_bot = '0'
            else: val_bot = 'X'
            if bot == 'pl_1':
                rez = cz.reread_form()
                (ky, phrase) = cz.bot_brain (rez, count, val_bot, bot)
                cz.cross_zero[f'{ky}'] = val_bot
                await update.message.reply_text(f'One moment! {cz.bot_phrases.get(random.randint(1,5))}')
                cr = cz.cross_zero
                await update.message.reply_text (   f'Бот сходил {phrase} \n\n'
                                        f"| {cr['a1']} | {cr['a2']} | {cr['a3']} |\n"
                                        f"| {cr['b1']} | {cr['b2']} | {cr['b3']} |\n"
                                        f"| {cr['c1']} | {cr['c2']} | {cr['c3']} |\n\n"
                                    
                                     f'{player}, клетка?\n\n'
                                     f"| /a1 | /a2 | /a3 |\n"
                                     f"| /b1 | /b2 | /b3 |\n"
                                     f"| /c1 | /c2 | /c3 |")                
                
                
                # form(update, context )
                # print(phrase)
                phrase = str()
                rez = cz.reread_form()
            
            count = 2    
            invitation = f'Выберите ячейку для {val}. Пример: "a1"'
            
            
    # ky = str()    
        # while ky not in cz.cross_zero.keys():
        #     try:    
        #         ky = input(f'\nOk! {invitation}  ').lower()
        #         while cz.cross_zero[f'{ky}'] != '_':
        #             ky = input('Ууупссс. Клетка уже заполнена! Выберите новую  ' ).lower()
        #     except: 
        #         print ('Несуществующая клетка. Повнимательней пожалуйста. Повторим')  
        #         continue 
        # invitation = f'Куда ставить {val}? '
    cz.cross_zero[f'{ky}'] = val
    cr = cz.cross_zero
    await update.message.reply_text (   'Ок! Let\'s go! \n\n'
                                        f"| {cr['a1']} | {cr['a2']} | {cr['a3']} |\n"
                                        f"| {cr['b1']} | {cr['b2']} | {cr['b3']} |\n"
                                        f"| {cr['c1']} | {cr['c2']} | {cr['c3']} |\n\n"
                                    
                                    'Куда ставите?\n\n'
                                     f"| /a1 | /a2 | /a3 |\n"
                                     f"| /b1 | /b2 | /b3 |\n"
                                     f"| /c1 | /c2 | /c3 |")                
                        
        
    #     os.system('cls')
    #     # form(update, context )
    #     rez = cz.reread_form()
    #     human_result = cz.watch_rez(rez)
    #     if human_result :
    #         message = cz.result_message (human_result)       
    #         # return message, player
    # # Следующим играет бот        
    #     (ky, phrase) = cz.bot_brain (rez, count, val_bot, bot)
    #     cz.cross_zero[f'{ky}'] = val_bot
    #     print(f'One moment! {cz.bot_phrases.get(random.randint(1,5))}')
    #     time.sleep(1.6)
    #     os.system('cls')
    #     form(val_bot, context )
    #     print(phrase)
    #     phrase = str()
    #     rez = cz.reread_form()
    #     bot_result = cz.watch_rez(rez)        
    #     if bot_result :
    #         message = cz.result_message (bot_result)       
    #         # return message,''
    #     count = 2
    # await update.message.reply_text(f'Result = ')   
    
    
async def help (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hi\n/go\n/calc')    

app = ApplicationBuilder().token("5631657109:AAGR7QLBm6fOXWGSRR2H6oRTR1CTEMtyrDM").build()
print("Server start")

app.add_handler(CommandHandler("hi", hello))
app.add_handler(CommandHandler("go", go))
app.add_handler(CommandHandler("calc", calc))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("game", quest))
app.add_handler(CommandHandler("x", start_game))
app.add_handler(CommandHandler("0", start_game))
app.add_handler(CommandHandler("a1", form))
app.add_handler(CommandHandler("a2", form))
app.add_handler(CommandHandler("a3", form))
app.add_handler(CommandHandler("b1", form))
app.add_handler(CommandHandler("b2", form))
app.add_handler(CommandHandler("b3", form))
app.add_handler(CommandHandler("c1", form))
app.add_handler(CommandHandler("c2", form))
app.add_handler(CommandHandler("c3", form))

app.run_polling()
print("Server stop")