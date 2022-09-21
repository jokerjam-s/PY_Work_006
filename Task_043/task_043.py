# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
#
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
#
#
import os

# формирование списка уникальных элементов из посл.
def unic_list(data: list) -> list: 
    dct = {x : data.count(x) for x in data}
    return [k for k in dct.keys() if dct[k]==1]

## MAIN ## 
os.system('cls')

tests = ((
    [1, 2, 3, 5, 1, 5, 3, 10],
    [1, 8, 7, 5, 4, 5, 3, 10],
    [1, 1, 3, 5, 4, 3, 3, 10]
))

print('Задача 43')
print('---------')
for t in tests:
    print(f'{t} -> {unic_list(t)}')
