"""
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
"""
from csv import DictReader, DictWriter
from os.path import exists


class LenNameError(BaseException):
    def __init__(self, message):
        self.message = message


class LenNumberError(BaseException):
    def __init__(self, message):
        self.message = message


def get_info():
    is_valid_name = False
    while not is_valid_name:
        try:
            first_name = input("Введите имя:")
            if len(str(first_name)) > 1:
                is_valid_name = True
            else:
                raise LenNameError('невалидное имя')
        except LenNameError as err:
            print(err)
            continue
    last_name = 'Ivanov'
    is_valid_number = False
    while not is_valid_number:
        try:
            phone_number = int(input("Введите номер телефона:"))
            if len(str(phone_number)) != 11:
                raise LenNumberError('Невалидная длина')
            else:
                is_valid_number = True
        except ValueError:
            print("Невалидный номер")
            continue
        except LenNumberError as err:
            print(err)
            continue
    return [first_name, last_name, phone_number]


def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name):
    res = read_file(file_name)
    user_data = get_info()
    for el in res:
        if el['телефон'] == str(user_data[2]):
            print("Такой пользователь уже существует")
            return
    obj = {'имя': user_data[0], 'фамилия': user_data[1], 'телефон': user_data[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)


def copy_data(file_name):
    user_num = int(input("введите номер записи:"))
    data1 = read_file(file_name)
    user_data = data1[user_num - 1]
    res = read_file(file_name1)
    res.append(user_data)
    with open(file_name1, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)


file_name = 'phone.csv'
file_name1 = 'phone1.csv'


def main():
    while True:
        command = input("введите команду:")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print("файл не создан, создайтй его!")
                continue
            print(*read_file(file_name))
        elif command == 'c':
            if not exists(file_name1):
                create_file(file_name1)
            copy_data(file_name)


main()
