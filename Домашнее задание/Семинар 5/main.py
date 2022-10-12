# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def del_text (list_string):
    list_string = list(filter(lambda a: 'абв' not in a, list_string.split()))
    return ' '.join(list_string)

text = 'аист забвение поворот зимбабве'
text = del_text(text)
print(text)

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# from random import randint


text = 'Игра с конфетами!'
print(text)

def player_vs_player():
    lolly_count = 50
    max_pull = 28
    the_lot = 0
    gamer_1 = input('Имя первого игрока: ')
    gamer_2 = input('Имя второго игрока: ')

    lot = random.randint(0, 2)
    if lot == 1:
        win = gamer_1
        lose = gamer_2
    else:
        win = gamer_2
        lose = gamer_1
    print(f'{win} ходит первым')

    while lolly_count > 0:
        if the_lot == 0:
            take = int(input(f'{win}, возьмите до 28 конфет: '))
            if take > lolly_count or take > max_pull:
                take = int(input('Возьмите правильное количество: '))
            lolly_count -= take
        if lolly_count > 0:
            print(f'Осталось {lolly_count} конфет')
            the_lot = 1
        else:
            print('Конфеты закончились!')
    
        if the_lot == 1:
            take = int(input(f'{lose}, возьмите до 28 конфет: '))
            if take > lolly_count or take > max_pull:
                take = int(input('Возьмите правильное количество: '))
            lolly_count -= take
        if lolly_count > 0:
            print(f'Осталось {lolly_count} конфет')
            the_lot = 0
        else:
            print('Конфеты закончились!')
    
    if the_lot == 1:
        print(f'{lose} победитель!')
    if the_lot == 0:
        print(f'{win} победитель!')

player_vs_player()


# a) Добавьте игру против бота

import random

text = 'Игра с конфетами!'
print(text)

def player_vs_bot():
    lolly_count = 50
    maxx = 28
    min = 1
    man = input('Имя игрока: ')
    bot = 'Bot'

    lot = random.choice([man, bot])
    if lot == bot:
        print(f'{bot} ходит первым')
    else:
        print(f'{man} ходит первым')
    
    while lolly_count > 0:
        if lot == bot:
            if lolly_count <= maxx:
                take = lolly_count
                lolly_count -= take
            else:
                take = random.randint(min, maxx)
                print(f'{bot} взял {take} конфет')
                lolly_count -= take
            print(f'{lolly_count} осталось!')
            lot = man
        else:
            take = int(input('Возьмите до 28 конфет: '))
            if take > maxx or take < min:
                take = int(input('Введите верное количество: '))
            lolly_count -= take
            print(f'{lolly_count} осталось!')
            lot = bot
    print(f'{lot} = победитель!')

player_vs_bot()
# # b) Подумайте как наделить бота ""интеллектом""


# # 3. Создайте программу для игры в ""Крестики-нолики"".

map = list(range(1, 10))

def print_map():
    print(map[0], end=' ')
    print(map[1], end=' ')
    print(map[2])
    
    print(map[3], end=' ')
    print(map[4], end=' ')
    print(map[5])
    
    print(map[6], end=' ')
    print(map[7], end=' ')
    print(map[8])

variable = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
def result():
    win = ''
    for i in variable:
        if map[i[0]] == 'X' and map[i[1]] == 'X' and map[i[2]] == 'X':
            win = 'X'
        if map[i[0]] == 'O' and map[i[1]] == 'O' and map[i[2]] == 'O':
            win = 'O'
    return win

def step_map(step, char):
    ind = map.index(step)
    map[ind] = char
    
game_over = False
player_1 = True

while game_over == False:
    print_map()
    if player_1 == True:
        char = 'X'
        step = int(input('Ход первого игрока: '))
    else:
        char = 'O'
        step = int(input('Ход второго игрока: '))
    
    step_map(step, char)
    win = result()
    
    if win != '':
        game_over = True
    else:
        game_over = False
    
    player_1 = not(player_1)
    
print_map()
print('Победил', win)

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

text = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'

count = 1
st = ''
for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        count += 1
    else:
        st = st + str(count) + text[i]
        count = 1
if count > 1 or (text[len(text)-2] != text[-1]):
    st = st + str(count) + text[-1]
print(st)

text = '12W1B12W3B24W1B14W'

num = ''
st = ''
for i in range(len(text)):
    if not text[i].isalpha():
        num += text[i]
    else:
        st = st + text[i] * int(num)
        num = ''
print(st)