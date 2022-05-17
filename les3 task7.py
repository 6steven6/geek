import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Массив: {array}')

min_index_1 = 0
min_index_2 = 1

for i in array:
    if array[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = array.index(i)
    elif array[min_index_2] > i:
        min_index_2 = array.index(i)

print(f'Два наименьших элемента: {array[min_index_1]} и {array[min_index_2]}')


    