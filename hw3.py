# Создайте программу для игры в ""Крестики-нолики"".

import os

def Checking(list):
    if list[0] == list[1] == list[2] or list[2] == list[4] == list[6] or list[0] == list[4] == list[8] or list[2] == list[5] == list[8] or list[3] == list[4] == list[5] or list[6] == list[7] == list[8] or list[0] == list[3] == list[6] or list[1] == list[4] == list[7]:
        return True
    else:
        return False

def ShowTheDesk(str1, str2, str3):
    print(str1)
    print(str2)
    print(str3)

def LetsPlay(list, str1, str2, str3, hod, gamer, i, j, count):
    X = 'X'
    O = '0'
    win = False
    mimo = []
    os.system('cls' if os.name == 'nt' else 'clear')  # чистим поле вилкой
    ShowTheDesk(str1, str2, str3)
    hod = int(input(f'Ходит {gamer[j]} ({i}): '))
    if hod in range(1, 10):
        if hod in range(1, 4):
            str1[hod-1] = i
        elif hod in range(4, 7):
            str2[hod-4] = i
        else:
            str3[hod-7] = i
    else:
        print('Вы за пределами поля, ходите ещё раз!')
        LetsPlay(list, str1, str2, str3, hod, gamer, O, int(j), count)
    list[hod-1] = int(j)
    count += 1
    if count > 4:
        win = Checking(list)
    if win == False:
        j = not j
        if j == 0:
            i = X
        else:
            i = O
        LetsPlay(list, str1, str2, str3, hod, gamer, i, int(j), count)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')  # чистим поле вилкой
        ShowTheDesk(str1, str2, str3)
        print(f'Выиграл {gamer[int(j)]} ({i})')


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
str1 = [1, 2, 3]
str2 = [4, 5, 6]
str3 = [7, 8, 9]

gamer1 = (input(f'Первый игрок: '))
gamer2 = (input(f'Второй игрок: '))
gamers = [gamer1, gamer2]

LetsPlay(list, str1, str2, str3, 0, gamers, 'X', 0, 0)
