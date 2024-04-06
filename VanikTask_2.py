# -*- coding: utf-8 -*-
# Угадай число
import random

def check_ask():
    if n < m:
        print("Мое число больше")
        return True
    elif n > m:
        print("Мое число меньше")
        return True
    else:
        print("Вы угадали! Поздравляю!")
        return False

m = random.randint(1, 100)

while True:
    n = int(input("Введите свое число от 1 до 100: "))
    if check_ask() == False:
        break

# Сумма заданного диапазона
first_number = int(input("Введите первое целое число диапазона: "))
last_number = int(input("Введите последнее целое число диапазона: "))
list_ = [x for x in range(first_number, last_number + 1)]
print(list_)
print(sum(list_))

# Определение возможности построения треугольника по трем сторонам


def check_first():
    treugolnik.append(ab)
    treugolnik.append(bc)
    treugolnik.append(ca)
    treugolnik.sort()
    if (treugolnik[0] + treugolnik[1]) > treugolnik[2]:
        print("Треугольник построить можно")
        if treugolnik[0] == treugolnik[1] and (treugolnik[0] + treugolnik[1]) > treugolnik[2]:
            print("Тругольник равносторонний")
    elif ((treugolnik[0] ** 2 + treugolnik[1] ** 2) ** 0.5) == treugolnik[2]:
        print("Треугольник прямоугольный")
    else:
        print("Невозможно построить треугольник")

ab = float(input("Введите первую длины: "))
bc = float(input("Введите вторую длину: "))
ca = float(input("введите третью сторону: "))
treugolnik = []

check_first()

# Счастливый билетик

def bilet():
    for i in range(6):
       paper.append(int(input(f"Введите {i + 1} число номера билета: ")))
    if sum(paper[:3]) == sum(paper[3:6]):
        print(sum(paper[:3]))
        print(sum(paper[3:6]))
        print("Билетик счастливый")
    else:
        print(sum(paper[:3]))
        print(sum(paper[3:6]))
        print("Это обычный билет")

paper=[]
bilet()

# Своя функция len

stroka = input("Введите свою строку: ")
len_ = 0
for i in stroka:
    len_ += 1
print(len_)
