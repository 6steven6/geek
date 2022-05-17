result_array = [0]*8
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            result_array[j-2] += 1
i = 0
while i < len(result_array):
    print(f'Колличество чисел кратных {i+2}: {result_array[i]}')
    i += 1