#  1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Введите чило от одного до семи')
day = int(input())
if day <= 0:
    print('Введите корректное число')
elif day <= 5:
    print(f'{day} -> нет')
elif day == 6 or day == 7:
    print(f'{day} -> да')
else: print('Введите корректное число')

# 2. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print('Введите x')
x = int(input())
print('Введите y')
y = int(input())

if x > 0 and y > 0:
    print(f'{x}; {y} -> 1')
elif x < 0 and y > 0:
    print(f'{x}; {y} -> 2')
elif x < 0 and y < 0:
    print(f'{x}; {y} -> 3')
elif x > 0 and y < 0:
    print(f'{x}; {y} -> 4')
else:
    print('точка на координатной прямой')

# 3. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

print('Введите номер четверти (от 1 до 4)')
number = int(input())
if number == 1:
    print('x > 0; y > 0')
elif number == 2:
    print(' x < 0; y > 0')
elif number == 3:
    print('x < 0; y < 0')
elif number == 4:
    print('X > 0; y < 0')
else:
    print('Введите корректное значение')

# 4. Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.

print('Enter coordinates point А:')
x_A = float(input('X: '))
y_A = float(input('Y: '))
print("Enter coordinates point B:")
x_B = float(input('X: '))
y_B = float(input('Y: '))

from math import sqrt
print('Distance between A and B: ',round(sqrt((x_A - x_B)**2 + (y_A - y_B)**2), 2))


# 5. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


statement = inputNumbers(3)

if checkPredicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
