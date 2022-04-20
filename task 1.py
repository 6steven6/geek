# https://drive.google.com/file/d/1Rn4NmI8_SVwZ06q8l11rB70_al0hbc0n/view?usp=sharing

a = int(input('Введите число от 100 до 999: '))
first_int = a // 100
last_two_int = a % 100
second_int = last_two_int // 10
third_int = last_two_int % 10
res = first_int + second_int + third_int
print(f'{res}')
