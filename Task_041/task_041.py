# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
#
# Пример:
# 2+2 => 4
# 1+2*3 => 7
# 1-2*3 => -5
#
# Добавьте возможность использования скобок, меняющих приоритет операций.
#
# Пример:
# 1+2*3 => 7
# (1+2)*3 => 9
#
# передаваемое для расчета выражение считаем синтаксически верным
# проверку не производим

import os

# список операций по убыванию приоритета (важно!)
OPERATIONS = ('*', '/', '+', '-')

# парсинг строки в список
def parse_str(strk: str, list_op: tuple) -> list:
    result = []
    brackets_cnt = 0
    start_pos = 0
    i = 0
    while i < len(strk):
        if strk[i] == '(':  # нашли скобку -> ищем парную закрывающую
            brackets_cnt += 1
            j = i + 1
            while brackets_cnt > 0:
                if strk[j] == ')':
                    brackets_cnt -= 1
                elif strk[j] == '(':
                    brackets_cnt += 1
                j += 1
            i = j

        if strk[i] in list_op:  # нашли оператор
            result.append(strk[start_pos:i])
            result.append(strk[i])
            start_pos = i+1
        i += 1

    result.append(strk[start_pos::])    # последний аргумент
    return result

# вычисление выражения
# evals - список аргументов и операций
# oper - набор выполлняемых операций по убыванию приоритета


def calc_val(evals: list, oper: list):
    # один аргумент - расчет окончен
    if len(evals) == 1:
        return float(evals[0])

    # операция от начала списка (идут по убыванию приоритета)
    index_op = evals.index(oper[0])

    # искомой операции нет
    if index_op < 0:
        oper.remove(oper[0])
        return calc_val(evals, oper)

    # проводим вычисление
    # проверяем скобку на аргументах операции
    param = []
    for c in [evals[index_op-1], evals[index_op+1]]:
        if c[0] == '(':
            param.append(calc_val(parse_str(c[1:-1], OPERATIONS), list(OPERATIONS)))
        else:
            param.append(float(c))
    
    # вычисление
    evals[index_op] = calc(param, oper[0])
    
#
#    if evals[index_op-1][0] == '(':
#        arg_1 = calc_val(parse_str(evals[index_op-1][1:-1], OPERATIONS), list(OPERATIONS))
#    else:
#        arg_1 = float(evals[index_op-1])
#
#    if evals[index_op+1][0] == '(':
#        arg_2 = calc_val(parse_str(evals[index_op+1][1:-1], OPERATIONS), list(OPERATIONS))
#    else:
#        arg_2 = float(evals[index_op+1])
#


# блок операций
def calc(par: list, op: str) -> float:
    res = 0.
    match op:
        case '*':
            res = par[0]*par[1]
        case '/':
            res = par[0]/par[1]
        case '+':
            res = par[0]+par[1]
        case '-':
            res = par[0]-par[1]
    return res



## MAIN ##
line_str = '2+(4-7)*3'

i = 1
j = 4
#tt = line_str[i:j]

# print(int(tt))

print(parse_str(line_str, OPERATIONS))
