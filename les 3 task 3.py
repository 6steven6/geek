import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max = array[0]
min = array[0]

for i in array:
    if i > max:
        max = i
    elif i < min:
        min = i
min_index = array.index(min)
max_index = array.index(max)
array[min_index], array[max_index] = array[max_index], array[min_index]
print(f'Массив после изменения элементов с инедксом {min_index} и {max_index}: {array}')