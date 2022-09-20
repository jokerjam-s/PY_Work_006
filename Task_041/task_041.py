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
# проверку не производим. Расчет

import os

# список операций по убыванию приоритета (важно!)
# - олобрабатывать раньше +. ()
OPERATIONS = ('*', '/', '-', '+')

# парсинг строки в список
def parse_str(strk: str, list_op: tuple) -> list:
    result = []
    brackets_cnt = 0
    start_pos = 0
    i = 0
    while i < len(strk):
        if strk[i] == '(':  # нашли скобку -> ищем пару
            brackets_cnt += 1
            j = i + 1
            while brackets_cnt > 0:
                if strk[j] == ')':
                    brackets_cnt -= 1
                elif strk[j] == '(':
                    brackets_cnt += 1
                j += 1
            i = j-1
        elif strk[i] in list_op:  # нашли оператор
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
    try:
        index_op = evals.index(oper[0])
    except:
        index_op = -1

    # искомой операции нет
    if index_op < 0:
        oper.remove(oper[0])
        return calc_val(evals, oper)

    # проводим вычисление
    # проверяем скобку на аргументах операции
    param = []
    for c in (evals[index_op-1], evals[index_op+1]):
        if c[0] == '(':
            str_par = calc_val(parse_str(c[1:-1], OPERATIONS), list(OPERATIONS))
            param.append(float(str_par))
        else:
            param.append(float(c))
    
    # вычисление
    evals[index_op] = calc(param, oper[0])
    # удалить элементы справа& слева
    evals.pop(index_op+1)
    evals.pop(index_op-1)

    return calc_val(evals, oper)


# блок операций
def calc(par: list, op: str) -> str:
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
    return str(res)


## MAIN ##
os.system('cls')

tasks = ((
    '2+(4-7)*3', 
    '4*(3-1)/(9-7)', 
    '8+2*4+(6+(2-3)*2)', 
    '12-8+3*2' 
    ))

for t in tasks:
    lst = parse_str(t, OPERATIONS)
    print(lst)
    print(f'{t} = {calc_val(lst, list(OPERATIONS))}')
