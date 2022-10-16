import csv
from view import add_text

def open_txt():
    with open('Семинары\Домашнее задание\Семинар 7\phonebook.txt', 'r', encoding = 'utf-8') as data:
        print(*data)

def open_csv():
    with open('Семинары\Домашнее задание\Семинар 7\phonebook.csv', encoding = 'utf-8') as data:
        file_reader = csv.reader(data, delimiter = ",")
        count = 0
        for row in file_reader:
            if count == 0:
                print(f'{row[0]}|{row[1]}|{row[2]}')
            else:
                print(f'{row[0]} {row[1]} - {row[2]}')
            count += 1

add = add_text()
def add_txt():
    with open('Семинары\Домашнее задание\Семинар 7\phonebook.txt', 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {add[0]}\n\nИмя: {add[1]}\n\nНомер телефона: {add[2]}\n\nОписание: {add[3]}\n\n\n')

add_txt()