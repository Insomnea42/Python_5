# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

def CandyGame2Players(candys, gamer, i):
    taken = int(input(f'Ход игрока {gamer[i]}: '))
    if taken <= 28:
        candys -= taken
    else:
        print(f'Нужно взять до 28 конфет!')
        CandyGame2Players(candys, gamer, i)
    if candys <= 0:
        print(f'Game over! Победил игрок {gamer[i]}')
    else:
        i = not i  # будет либо 0, либо 1 и меняется в зависимости от значения
        print(f'На столе осталось {candys} конфет')
        CandyGame2Players(candys, gamer, int(i))


def CandyGameBot(candys, gamer, i):
    bot_take = 1
    ost = candys
    if i == 0:
        if ost <=28:
            print(f'Game over! Победил игрок {gamer[i]}')
        else:
            taken = int(input(f'Ход игрока {gamer[i]}: '))
            if taken <= 28:
                candys -= taken
                print(f'На столе осталось {candys} конфет')
                CandyGameBot(candys, gamer, 1)
            else:
                print(f'Нужно взять до 28 конфет!')
                CandyGameBot(candys, gamer, 0)
    else:
        if ost <=28:
            print(f'Game over! Победил игрок {gamer[i]}')
        else:
            while ost > 30 and bot_take < 28:
                bot_take += 1
                ost -= 1
            candys -= bot_take            
        #else:
            print(f'Bot взял {bot_take} конфет')
            print(f'На столе осталось {candys} конфет')
            CandyGameBot(candys, gamer, 0)

gamers = []

style = input(f'Выберите режим игры: Два игрока, Против бота: ')
if style == 'Два игрока':
    gamer1 = (input(f'Первый игрок: '))
    gamer2 = (input(f'Второй игрок: '))
    all_candy = int(input(f'Положите на стол все конфеты: '))
    gamers = [gamer1, gamer2]
    CandyGame2Players(all_candy, gamers, 0)
else:
    gamer1 = (input(f'Первый игрок: '))
    all_candy = int(input(f'Положите на стол все конфеты: '))
    gamers = [gamer1, 'Bot']
    CandyGameBot(all_candy, gamers, 0)
