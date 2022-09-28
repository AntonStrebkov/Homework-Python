# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# number = input('введите число')
# sum = 0
# for i in number:
#     if i != '.':
#       sum += int(i)
# print(sum)


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# num = int(input('Введите число: '))
# composition = 1
# for i in range(1, num + 1):
#     composition *= i
#     print(composition, end=' ')


# 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# n = 4
# sum = 0
# for i in range(1, n + 1):
#     sum += (1 + 1/i)**i
# print(round(sum, 4))


# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N] (например, [-3, -2, 1, 0, 1, 2, 3]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# list_numbers = [-3, -2, -1, 0, 1, 2, 3]
# first_position = 1
# second_position = 7
# for i in range(len(list_numbers)):
#     myltiplication = list_numbers[first_position - 1] * list_numbers[second_position - 1]
# print(myltiplication)


# 5. Реализуйте алгоритм перемешивания списка (метод random.shuffle использовать нельзя, но другие методы из библиотеки random - можно).

# import random

# def mixed_list(origin_list):
#     list = origin_list[:]
#     list_length = len(list)
#     for i in range(list_length):
#         ran_index = random.randint(0, list_length - 1)
#         temp = list[i]
#         list[i] = list[ran_index]
#         list[ran_index] = temp
#     return list

# list = [1, 2, 3, 4, 5]
# mix_list = mixed_list(list)
# print(f'Исходный список: {list}')
# print(f'Перемешанный список: {mix_list}')
