# Задача 107 Создайте программу для игры в ""Крестики-нолики"" (Добавьте игру против бота)
import random
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import tracemalloc
tracemalloc.start(50)

os.system('cls')

cross_zero = {  # словарь для построения квадрата со значениями клеток
    'a1': '_',
    'a2': '_',
    'a3': '_',
    'b1': '_',
    'b2': '_',
    'b3': '_',
    'c1': '_',
    'c2': '_',
    'c3': '_'
}

bot_iq = {      # словарь соответствия items линий из reread_form() для бота
    'a1': 'a1',
    'a2': 'a2',
    'a3': 'a3',
    'b1': 'b1',
    'b2': 'b2',
    'b3': 'b3',
    'c1': 'c1',
    'c2': 'c2',
    'c3': 'c3',
    'c1': 'c1',
    'c2': 'c2',
    'c3': 'c3',
    'd1': 'a1',
    'd2': 'b2',
    'd3': 'c3',
    'g1': 'a3',
    'g2': 'b2',
    'g3': 'c1',
    '11': 'a1',
    '12': 'b1',
    '13': 'c1',
    '21': 'a2',
    '22': 'b2',
    '23': 'c2',
    '31': 'a3',
    '32': 'b3',
    '33': 'c3'
}

bot_phrases = {
    1 : 'Тааакс! Приступим',
    2 : 'Я, пожалуй, вот сюда. Ваш ход, коллега!',
    3 : 'Очень долго думаете, в отличие от меня ))',
    4 : 'Кто сказал, что у меня искусственный интеллект?',
    5 : 'Продолжим?',
    6 : 'Ooops',
    7 : 'I\'m winner! Сорян!',  
    8 : 'Yahoo!!! I\'m winner!', 
    9 : 'Признаю своё поражение',
    10: 'Вы выиграли' ,
    11: 'Хорошая игра' ,
    12: 'Вы достойный соперник',
    13: 'Ещё разок? /game'
}

def reread_form(): # Возвращает строку rez
    line_a = 'a', cross_zero['a1'], cross_zero['a2'], cross_zero['a3']
    line_b = 'b', cross_zero['b1'], cross_zero['b2'], cross_zero['b3']
    line_c = 'c', cross_zero['c1'], cross_zero['c2'], cross_zero['c3']
    line_1 = '1', cross_zero['a1'], cross_zero['b1'], cross_zero['c1']
    line_2 = '2', cross_zero['a2'], cross_zero['b2'], cross_zero['c2']
    line_3 = '3', cross_zero['a3'], cross_zero['b3'], cross_zero['c3']
    dgnl_d = 'd', cross_zero['a1'], cross_zero['b2'], cross_zero['c3']
    dgnl_g = 'g', cross_zero['a3'], cross_zero['b2'], cross_zero['c1']
    rez = (line_a, line_b, line_c, line_1, line_2, line_3, dgnl_d, dgnl_g)
    return rez

def watch_rez(game_rez): # отслеживает состояние rez и подводит итог шага
    for l in game_rez:
        l = ''.join (l) 
        if l.upper().count('X') == 3 or l.count('0') == 3:
            result = 'Game over!'
            return result
        elif '_' not in cross_zero.values():            
            result = 'Ничья'
            return result
    return

# def main_game():    # Основной скрипт игры на двоих humans
#     count = 1
#     while True:
#         if count == 1:
#             val = input('Привет! Кто первый? Выберите X или 0  ').upper()
#             while '0' != val != 'X':
#                 val = input(f'Aй-яй-яй! Кто ввел "{val}" ?!! Нужны eng X или 0  ').upper()     
#         ky = str()
#         while ky not in cross_zero.keys():
#             try:    
#                 ky = input(f'\nOk! Выбрать ячейку для {val}. Пример: "a1"  ').lower()
#                 while cross_zero[f'{ky}'] != '_':
#                     ky = input('Ууупссс. Клетка уже заполнена! Выберите новую  ' ).lower()
#             except: 
#                 print ('Несуществующая клетка. Повнимательней пожалуйста. Повторим')  
#                 continue 
#         cross_zero[f'{ky}'] = val
#         os.system('cls')
#         form(cross_zero)
#         rez = reread_form()
#         result = watch_rez(rez)
#         if result == 'Game over!':
#             return result,'Выиграл',val
#         elif result == 'Ничья':
#             return 'Game over!',result,''
#         if val == 'X':
#             val = '0'
#         else: val = 'X'
#         count = 2

def result_message (result):     # скрипт сообщений для игры с ботом  
    if result == 'Game over!':
        return result,'Ура!'
    elif result == 'Ничья':
        return 'Game over!',result

def bot_brain (gamerez, count, V, step):
    if V == 'X' : NV = '0'
    else        : NV = 'X'
    game_rez = list(gamerez)    # convert to list for next row 
    random.shuffle(game_rez)    # ибо (tuple - не перемешивается) 
    if count == 1:              # САмый первый  ход
        if step == 'pl_2':
            for line in game_rez:    
                if line.count('_') == 2 and line.count(NV) == 1:
                    if      line.index(NV) == 1:
                        ind = 3
                    elif    line.index(NV) == 3:
                        ind = 1
                    else:
                        ind = line.index('_') 
            
            # тут надо бы вставить условие о наличии NV в соответствущеё строке чтоб впенююрить  туда 
            
                    key_cell = ''.join((line[0], str(ind))) 
                    qu = bot_iq.get(key_cell)               # Продолжение
        
        # рандомно выбрать cell на первом щаге
        else:
            qu = ''.join((random.choices('abc')[0],str(random.randint(1,3))))
            while cross_zero[f'{qu}'] != '_':
                qu = ''.join((random.choices('abc')[0],str(random.randint(1,3))))
        message = bot_phrases.get(random.randint(1,1))
        return (qu, message)
    
    for line in game_rez:       # Все последующие ходы
        if line.count('_') == 1 and line.count(V) == 2:
            ind = line.index('_')
            key_cell = ''.join((line[0], str(ind)))
            qu = bot_iq.get(key_cell)               # Куда ставить WIN
            message = bot_phrases.get(random.randint(8,8))
            return (qu, message)
    for line in game_rez:    
        if line.count('_') == 1 and line.count(NV) == 2:
            ind = line.index('_')
            key_cell = ''.join((line[0], str(ind))) 
            qu = bot_iq.get(key_cell)               # Где навредить сопернику
            message = bot_phrases.get(random.randint(6,7))
            return (qu, message)
    for line in game_rez:    
        if line.count('_') == 2 and line.count(NV) == 1:
            if      line.index(NV) == 1:
                ind = 3
            elif    line.index(NV) == 3:
                ind = 1
            else:
                ind = line.index('_') 
            
            # тут надо вставить условие о наличии NV в соответствущеё строке чтоб впенююрить  туда 
            
            key_cell = ''.join((line[0], str(ind))) 
            qu = bot_iq.get(key_cell)               # Продолжение
            message = bot_phrases.get(random.randint(2,5))
            return (qu, message)          
          # добавлять новые условия здесь  
          #
    for line in game_rez:
        if line.count('_') == 2 and line.count(V) == 1:
            ind = line.index('_')
            key_cell = ''.join((line[0], str(ind))) 
            qu = bot_iq.get(key_cell)               # Где продолжить 
            message = bot_phrases.get(random.randint(2,5))
            return (qu, message)
    for line in game_rez:
        if line.count('_') == 3:
            ind = line.index('_')
            key_cell = ''.join((line[0], str(ind))) 
            qu = bot_iq.get(key_cell)               # Где начать
            message = bot_phrases.get(random.randint(2,5))
            return (qu, message) 
    for line in game_rez:
        if line.count('_') == 1:
            ind = line.index('_')
            key_cell = ''.join((line[0], str(ind))) 
            qu = bot_iq.get(key_cell)               # На всякий случай
            message = 'Ну... бывает...'
            return (qu, message) 
    # if count != 1: # рандомно выбрать
    #     qu = ''.join((random.choices('abc')[0],str(random.randint(1,3))))
    #     while cross_zero[f'{qu}'] != '_':
    #         qu = ''.join((random.choices('abc')[0],str(random.randint(1,3))))
    #     message = 'Ну... бывает. Требую реванша!'    
    # return (qu, message) 


def hello_bot (val): # для телеги
    human = str(random.randint(1,2)).join(['pl_',''])
    if human == 'pl_1':
        bot = 'pl_2'
    else:     
        bot = 'pl_1'
    globals()[bot] = 'Super-Puper-Bot'
    result = (bot, val)
    return result
        
