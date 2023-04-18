#
from random import *

print('Мини-игра')
X = randint(-10, 10)
X = X // 1
Y = randint(-10, 10)
Y = Y // 1
print(X, Y)
com = (X >= 0) or True and (X == 3) or (Y * Y != 4)
if com == True:
    print('Вы проиграли!')
else:
    print('Вы выиграли!')

# Практическая работа
# 1
print('Практическая работа')
print('Задание 1')
A1 = randint(-20, 20)
B1 = randint(-20, 20)
print(f'Числа:{A1}; {B1};')
if A1 > B1:
    print(f'Число {A1} больше')
else:
    print(f'Число {B1} больше')

# 2
print()
print('Задание 2')
A2 = randint(-20, 20)
B2 = randint(-20, 20)
C2 = randint(-20, 20)
x2 = ([A2, B2, C2])
print(f'Числа:{A2}; {B2}; {C2};')
print(f'Число {max(x2, key=lambda i: int(i))} больше')

# 3
print()
print('Задание 3')
X3 = randint(-10, 10)
if X != 0:
    Y3 = (X3 + 1) / (2 * X)
    print(f'Значение функции равно: {Y3}')
else:
    print('Решений нет')

# 4
print()
print('Задание 4')
X4 = 38000  # рублей за 38 часов
A4 = X4 / 38  # рублей за час работы
B4 = A4 * 1.5  # Cверх
hour = int(input('Введите кол-во часов, проработанных работником:'))
if hour <= 38:
    summ1 = A4 * hour
    print(f'За {hour}ч. работник заработал {summ1}р.')
else:
    summ2 = (X4 + (hour - 38) * B4)
    print(f'За {hour}ч. работник заработал {summ2}р.')
# 5
print()
print('Задание 5')
X5 = randint(-10, 10)
if X5 > 3:
    Y5 = X ** 2 + 5
    print(f'Значение функции равно: {Y5}')
else:
    Y5 = X5 - 8
    print(f'Значение функции равно: {Y5}')
# 6
print()
print('Задание 6')
X6 = randint(-10, 10)
if X6 > 0:
    Y6 = X6 - 12
    print(f'Значение функции равно: {Y6}')
elif X6 < 0:
    Y6 = X6 ** 2
    print(f'Значение функции равно: {Y6}')
else:
    Y6 = 5
    print(f'Значение функции равно: {Y6}')
# 7
print()
print('Задание 7')
A7 = randint(-10, 10)
B7 = randint(-10, 10)
C7 = randint(-10, 10)
print(f'Числа:{A7}; {B7}; {C7};')
S7 = 0
if A7 > 0:
    S7 = S7 + A7
if B7 > 0:
    S7 = S7 + B7
if C7 > 0:
    S7 = S7 + C7
print(f'Сумма положительных чисел равна: {S7}')
# 8
print()
print('Задание 8')
A8 = int(input('Введи первое число:'))
B8 = int(input("Введи второе число:"))
C8 = int(input("Введи третье число:"))
S8 = 0
if A8 == 0:
    S8 = S8 + 1
if B8 == 0:
    S8 = S8 + 1
if C8 == 0:
    S8 = S8 + 1

print(f'Количество чисел равных нулю: {S8}')
# 9
print()
print('Задание 9')
rad9 = int(input('Введите радиус круга:'))
stkv9 = int(input('Введите сторону квадрата:'))
gip9 = ((stkv9 ** 2) * 2) ** 0.5
if gip9 > rad9:
    print('Квадрат не входит в круг')
else:
    print('Квадрат входит в круг')
