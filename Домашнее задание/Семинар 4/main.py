# 1. Вычислить число c заданной точностью d

# from math import pi


# d = int(input())
# print(round(pi, d))

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input("Число N: "))
# lst = []
# i = 2
# while i <= n:
#     if n % i == 0:
#         lst.append(i)
#         n //= i
#     else:
#         i += 1
# print(lst)

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# list = [int(i) for i in input("Введите числа через пробел:").split()]
# print(list)

# new_list = []
# [new_list.append(i) for i in list if i not in new_list]
# print(new_list)

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
#  и записать в файл многочлен степени k.

from random import randint


k = int(input("Введите степень: "))
list = []
res = ''
for i in range(k + 1):
    list.append(randint(0, 101))
# print(list)
# # for i in range(len(list)):
# #     if i == len(list) - 1:
# #         res += str(list[i])
# #     else:
# #         res += str(list[i]) + 'x^' + str(len(list) - i - 1) + '+'
# # print(res)
# # with open('file.txt', 'w') as data:
# #     data.write(res)

# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
list = []
res = ''
for i in range(k + 1):
    list.append(randint(0, 101))
list2 = []
res = ''
for i in range(k + 1):
    list2.append(randint(0, 101))
list3 = [x+y for x, y in zip(list, list2)]
print(list)
print(list2)
print(list3)
for i in range(len(list)):
    if i == len(list3) - 1:
        res += str(list3[i]) + '=0'
    else:         
        res += str(list3[i]) + 'x^' + str(len(list3) - i - 1) + '+'
print(res)
with open('file.txt', 'w') as data:
    data.write(res)
