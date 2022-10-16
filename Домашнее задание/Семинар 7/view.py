
def quest_user():
    print('В каком формате открыть файл?')
    choice = int(input('1 - txt\n2 - csv\n:'))
    return choice

def add_text():
    lst = []
    first_name = input('Введите имя: ')
    lst.append(first_name)
    last_name = input('введите фамилию: ')
    lst.append(last_name)
    phone_num = input('Введите телефон: ')
    lst.append(phone_num)
    info = input('Введите описание: ')
    lst.append(info)
    return

