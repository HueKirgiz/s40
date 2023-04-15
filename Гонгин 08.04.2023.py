#
from random import *
X = randint(-10,10)
X = X//1
Y = randint (-10,10)
Y = Y//1
print(X,Y)
com = (X>=0) or True and (X == 3) or (Y*Y!=4)
if com==True:
    print('Вы проиграли!')
else:
    print('Вы выиграли!')
# Практическая работа
# 1
print('Задание 1')
A1 = randint(-20,20)
B1 = randint(-20,20)
print(f'Первое число:{A1},второе число: {B1}')
if (A1>B1):
    print(f'Число {A1}')
else:
    print(B1)
# 2
A2 = randint(-20,20)
B2 = randint(-20,20)
C2 = randint(-20,20)
print(A2,B2,C2)
if (A2>B2>C2):
    print(A2)
else:
    if (A2<B2<C2):
        print(C2)
    else:
        print(B2)
# 3
X3 = randint(-10,10)
if (X!=0):
    Y31 = (X3 + 1) / (2 * X)
    print(Y31)
else:
    print('Решений нет')
# 4
X4 = 38000 #рублей за 38 часов
A4 = X4/38 #рублей за час работы
B4 = A4*1.5 #Cверх
hour = 40
print (hour)
if (hour<=38):
    summ1 = A4*hour
    print(summ1)
else:
    summ2 = (A4*38 + (hour - 38)*(B4))
    print(summ2)
# 5
X5 = randint(-10,10)
if (X5>3):
    Y51 = X**2+5
    print(Y51)
else:
    Y52 = X5-8
    print(Y52)
# 6
X6 = randint(-10,10)
if (X6>0):
    Y61 = X6-12
    print(Y61)
else:
    if (X6<0):
        Y62 = X6**2
        print(Y62)
    else:
        Y63 = 5
        print(Y63)
# 7
A7 = randint(-10,10)
B7 = randint(-10,10)
C7 = randint(-10,10)
S7 = 0
if A7>0: S7 = S7+A7
if B7>0: S7 = S7+B7
if C7>0: S7 = S7+C7
print(f'Сумма положительных чисел равна: {S7}')
# 8
print('Задание 8')
A8 = int(input('Введи первое число:'))
B8 = int(input("Введи второе число:"))
C8 = int(input("Введи третье число:"))
S8 = 0
if (A8==0): S8 = S8+1
if (B8==0): S8 = S8+1
if (C8==0): S8 = S8+1

print(f'Количество чисел равных нулю: {S8}')
# 9



