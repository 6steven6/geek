import random

SIZE = 100
MIN_ITEM = -99
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'Массив: {array}')

min_index = 0

for i in array:
    if array[min_index] > i:
        min_index = array.index(i)

if array[min_index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'Минимальный отрицательный элемент: {array[min_index]}.',
            f'Находится в массиве на позиции {min_index}')