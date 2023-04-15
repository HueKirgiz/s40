# Задача 1
print('1. Сравнение чисел')
a1=int(input('Введи a1: '))
b1=int(input('Введи b1: '))
x11 = (a1+b1)/2
y11 = a1*b1
if (a1<b1):
    print(f'Меньшее число = {a1}')
    print(f'Большее число = {b1}')
    a1 = x11
    b1 = y11
    print(f'a1 = {a1}, b1 = {b1}')
else:
    print(f'Меньшее число = {b1}')
    print(f'Большее число = {a1}')
    b1 = x11
    a1 = y11
    print(f'a1 = {a1}, b1 = {b1}')
# Задача 2
print('2. Расстояние до начала координат')
x1, y1 = input('Введите координаты 1-й точки: ').split()
int(x1)
int(y1)
x2, y2 = input('Введите координаты 2-й точки: ').split()
int(x2)
int(y2)
x3, y3 = input('Введите координаты 3-й точки: ').split()
int(x3)
int(y3)
if (x1, y1!=0):
    l1 = ((x1**2)+(y1**2))**0.5
else:
    if x1 == 0:
        l1 = abs(y1)
    else:
        l1 = abs(x1)

if (x2, y2!=0):
    l2 = int((x2**2)+(y2**2))**0.5
else:
    if x2 == 0:
        l2 = abs(y2)
    else:
        l2 = abs(x2)
if (x3, y3!=0):
    l3 = (x3**2)+(y3**2))**0.5
else:
    if x2 == 0:
        l3 = abs(y3)
    else:
        l3 = abs(x3)
min1 = min(l1, l2, l3)
l1, l2, l3 = 1, 2 ,3
print(f'{min1}-я точка - ближняя')



