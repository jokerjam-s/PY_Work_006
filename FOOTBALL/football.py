# Напишите программу, которая принимает на стандартный вход список игр 
# футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# 
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# 
# Формат ввода следующий:
#
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
#
# Вывод программы необходимо оформить следующим образом:
# Команда: Всегоигр Побед Ничьих Поражений Всего очков
#
# Конкретный пример ввода-вывода приведён ниже.
#
# Порядок вывода команд произвольный.
#
# Sample Input:
#
# 3
# Спартак 9; Зенит; 10
# Локомотив 12; Зенит 3
# Спартак 8; Локомотив 15
#
# Sample Output:
#
# Спартак: 2 0 0 2 0
# Зенит: 2 1 0 1 3
# Локомотив: 2 2 0 0 6

import os

# чтение данных

## MAIN ##
os.system('cls')

team_names = []
team_win = []
team_luse = []
team_games = []
team_draw = []
team_score = []

fl = open('data.txt')
cnt_rec = int(fl.readline())

for i in range(cnt_rec):
    line = fl.readline()
    info = line.split(';')
    
    info[1::2] = list(map(lambda x: int(x), info[1::2]))
    
    pos = []
    for i in (0,2):
        if info[i] not in team_names:
            team_names.append(info[i])
            team_luse.append(0)
            team_score.append(0)
            team_win.append(0)
            team_games.append(0)
            team_draw.append(0)

        pos.append(team_names.index(info[i]))

    team_games[pos[0]] += 1
    team_games[pos[1]] += 1
    
    if info[1] > info[3]:
        team_win[pos[0]] += 1
        team_score[pos[0]] += 3
        team_luse[pos[1]] += 1
    elif info[1] < info[3]:
        team_win[pos[1]] += 1
        team_score[pos[1]] += 3
        team_luse[pos[0]] += 1
    else:
        team_draw[pos[0]] += 1
        team_draw[pos[1]] += 1
        team_score[pos[0]] += 1
        team_score[pos[1]] += 1

fl.close()

team_win = list(map(lambda l : str(l), team_win))
team_luse = list(map(lambda l : str(l), team_luse))
team_games = list(map(lambda l : str(l), team_games))
team_draw = list(map(lambda l : str(l), team_draw))
team_score = list(map(lambda l : str(l), team_score))

full_info = list(zip(team_names, team_games, team_win, team_draw, team_luse, team_score))

print('football')
print('--------')

for x in full_info:
    print(' '.join(x))

