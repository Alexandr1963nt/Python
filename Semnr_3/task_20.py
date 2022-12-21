# # Задача 20:
# # В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# # Напишите программу, которая вычисляет стоимость введенного пользователем слова.

# # Ввод: ноутбук
# # Вывод: 12
# dictnry = {
#     'A': 1,
#     'E': 1,
#     'I': 1,
#     'O': 1,
#     'U': 1,
#     'L': 1,
#     'N': 1,
#     'S': 1,
#     'T': 1,
#     'R': 1,
#     'D': 2,
#     'G': 2,
#     'B': 3,
#     'C': 3,
#     'M': 3,
#     'P': 3,
#     'F': 4,
#     'H': 4,
#     'V': 4,
#     'W': 4,
#     'Y': 4,
#     'K': 5,
#     'J': 8,
#     'X': 8,
#     'Q': 10,
#     'Z': 10,
#     'А': 1,
#     'В': 1,
#     'Е': 1,
#     'И': 1,
#     'Н': 1,
#     'О': 1,
#     'Р': 1,
#     'С': 1,
#     'Т': 1,
#     'Д': 2,
#     'К': 2,
#     'Л': 2,
#     'М': 2,
#     'П': 2,
#     'У': 2,
#     'Б': 3,
#     'Г': 3,
#     'Ё': 3,
#     'Ь': 3,
#     'Я': 3,
#     'Й': 4,
#     'Ы': 4,
#     'Ж': 5,
#     'З': 5,
#     'Х': 5,
#     'Ц': 5,
#     'Ч': 5,
#     'Ш': 8,
#     'Э': 8,
#     'Ю': 8,
#     'Ф': 10,
#     'Щ': 10,
#     'Ъ': 10,
# }
# Задача 20: по настольной игре Скрабл (Scrabble)
import os
def scrabble(dictionary, word):
    keys = word.upper()
    word_cost = 0
    for i in keys:
        word_cost += dictionary.get(i, 0)
    return word_cost

def create_dictionary(language, points):
    dictionary = dict()
    for k, v in zip(language, points):
        dop = dict.fromkeys(k, v)
        # print(dop)
        dictionary.update(dop)
        # print(dictionary)
    return dictionary

def identify_language(string):
    if set(string).issubset(set(english)):
        return (eng, string)
    elif set(string).issubset(set(russian)):
        return (rus, string)
    else:
        print('уууппссс.. Некорректный ввод! попробуйте ещё раз')
        word = input('Введите слово повесомей на русском или английском :)) ')
        return (False, word)

e1 = 'AEIOULNSTR'   # - 1 очко;
e2 = 'DG'           # - 2 очка;
e3 = 'BCMP'         # - 3 очка;
e4 = 'FHVWY'        # - 4 очка;
e5 = 'K'            # - 5 очков;
e8 = 'JX'           # - 8 очков;
e10 = 'QZ'          # - 10 очков.

r1 = 'АВЕИНОРСТ'    # – 1 очко;
r2 = 'ДКЛМПУ'       # – 2 очка;
r3 = 'БГЁЬЯ'        # – 3 очка;
r4 = 'ЙЫ'           # – 4 очка;
r5 = 'ЖЗХЦЧ'        # – 5 очков;
r8 = 'ШЭЮ'          # – 8 очков;
r10 = 'ФЩЪ'         # – 10 очков.
russian = r1 + r2 + r3+r4+r5+r8+r10
english = e1 + e2 + e3+e4+e5+e8+e10
eng = (e1, e2, e3, e4, e5, e8, e10)
rus = (r1, r2, r3, r4, r5, r8, r10)
points_set = (1, 2, 3, 4, 5, 8, 10)

os.system('cls')

word = input('Введите слово на русском или английском : ')

language = False
result = (language, word)  # кортеж

while result[0] == False:
    result = identify_language(word.upper())
    language, word = result
    
dictnry = create_dictionary(language, points_set)

print(f'Весомый аргумент! Целых {scrabble (dictnry, word)} баллов\n')
