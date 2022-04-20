# https://drive.google.com/file/d/1hjppnhd7xtkIE7O1cwXoFW5pLph_cZzi/view?usp=sharing
a = int(input("Введите длинуо отрезка a: "))
b = int(input("Введите длинуо отрезка b: "))
c = int(input("Введите длинуо отрезка c: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольник не существует")
elif a == b == c:
    print("Треугольник равнсторонний")
elif a != b != c:
    print("Треугольник разносторонний")
else:
    print("Треугольник равнобедренный")
