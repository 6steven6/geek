import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Массив: {array}')

max_index = 0
for i in array:
    if array.count(max_index) < array.count(i):
        max_index = array.index(i)

print(f'Число {array[max_index]} встречается {array.count(max_index)} раза')