#https://drive.google.com/file/d/1QNn35_vD9RTefSbpkNUhPLp9dpQ0rS_S/view?usp=sharing
year = int(input("Введите год: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Високосный")
else:
    print("Не високосный")
