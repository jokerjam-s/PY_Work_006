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
# проверку не производим.

import os

# парсинг строки в список
def parse_str(strk: str) -> list:
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
        elif strk[i] in ('*', '/', '-', '+'):  # нашли оператор
            # отрицательные числа -Х, как 0-X
            result.append(strk[start_pos:i] if strk[start_pos:i] !='' else '0')
            result.append(strk[i])
            start_pos = i+1
        i += 1

    result.append(strk[start_pos::])    # последний аргумент
    return result

# вычисление выражения
# evals - список аргументов и операций
def calc_val(evals: list):
    # один аргумент - расчет окончен
    if len(evals) == 1:
        return float(evals[0])

    # вначале ищем и выполняем приоритетные операции 
    # перевернем список
    prior = list(reversed([i for i in range(len(evals)) if evals[i]=='*' or evals[i]=='/']))
    if len(prior) > 0:
        for i in prior:
            calculate(evals, i)

    # выполняем остальные шаг через 1 элемент т.к. 
    # список сформирован как аргумент, операция, аргумент, ... 
    while len(evals) > 1:
        calculate(evals, 1)

    return float(evals[0])


def calculate(listeval: list, op_no: int):
    par = []
    for c in (listeval[op_no-1], listeval[op_no+1]):
        if c[0] == '(':
            str_par = calc_val(parse_str(c[1:-1]))
            par.append(float(str_par))
        else:
            par.append(float(c))
    
    # вычисление c отловом ошибок (/ на 2 и т.д.)
    try:
        res = 0.
        match listeval[op_no]:
            case '*':
                res = par[0]*par[1]
            case '/':
                res = par[0]/par[1]
            case '+':
                res = par[0]+par[1]
            case '-':
                res = par[0]-par[1]
        
        listeval[op_no] = str(res)

        # удалить элементы справа & слева
        listeval.pop(op_no+1)
        listeval.pop(op_no-1)
    except Exception as e:
        print(e)


## MAIN ##
os.system('cls')

tasks = ((
    '2+2', 
    '1+2*3', 
    '1-2*3', 
    '-2+(4-7)*3', 
    '4*(3-1)/(9-7)*(-1)', 
    '8+2*4+(6+(2-3)*2)', 
    '12-8+3*2',
    '-3-1'
    ))

for t in tasks:
    lst = parse_str(t)
    print(f'{t} = {calc_val(lst)}')
