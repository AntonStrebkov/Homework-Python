# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

lst = [1, 2, 3, 4, 5]
sum = 0
for i in range(1, len(lst)):
    if (i % 2 == 1):
        sum += lst[i]
print (sum)

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

def pairs_mult(numbers):
    results = []
    while len(numbers) > 1:
        results.append(numbers[0]*numbers[-1])
        del numbers[0] 
        del numbers[-1] 
    if len(numbers) ==1: results.append(numbers[0]**2) 
    return results

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.

lst = [1.1, 1.2, 3.1, 5, 10.01]
min = 1
max = 0
for i in lst:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)
print(max - min)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num = int(input('Введите число: '))
res = ''
while (num != 0):
    res = str(num % 2) + res
    num //= 2
print(int(res))

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))

def get_fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n-1):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

fibo_nums = get_fibonacci(n)
print(get_fibonacci(n))
print(fibo_nums.index(0))
