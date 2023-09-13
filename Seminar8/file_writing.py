"""Создать телефонный справочник с
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
не должна быть линей

Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию,
и Вы должны реализовать функционал для изменения и удаления данных и поиска по фамилии.
"""

from csv import DictReader, DictWriter
from os.path import exists


def get_info():
    info = []
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    info.append(last_name)
    info.append(first_name)
    flag = False
    while not flag:
        try:
            phone_number = int(input("Введите номер телефона: "))
            if len(str(phone_number)) != 11:
                print("wrong number")
            else:
                flag = True
        except ValueError:
            print("not valid number")
    info.append(phone_number)
    return info


def create_file():
    with open("phone.csv", "w", encoding="utf-8", newline="") as data:
        # data.write('Фамилия;Имя;Номер\n')
        f_n_writer = DictWriter(data, fieldnames=["Фамилия", "Имя", "Номер"])
        f_n_writer.writeheader()


def write_file(lst):
    # with open('phone.txt', 'a', encoding='utf-8') as data:
    #     data.write(f'{lst[0]};{lst[1]};{lst[2]}\n')
    with open("phone.csv", "a", encoding="utf-8", newline="") as f_n:
        f_n_writer = DictWriter(f_n, fieldnames=["Фамилия", "Имя", "Номер"])
        obj = {"Фамилия": lst[0], "Имя": lst[1], "Номер": lst[2]}
        f_n_writer.writerow(obj)


def read_file(file_name):
    # with open(file_name, encoding='utf-8') as data:
    #     phone_book = data.readlines()
    with open(file_name, encoding="utf-8") as f_n:
        f_n_reader = DictReader(f_n)
        phone_book = list(f_n_reader)
    return phone_book


def record_info():
    lst = get_info()
    write_file(lst)


def search_name(file_name):
    name = input("Введите имя: ")
    phone_book = read_file(file_name)
    records_name = [record for record in phone_book if name.lower() in record["Имя"].lower()]
    if not records_name:
        print("Имя не найдено в справочнике")
    else:
        for record in records_name:
            print(record)


def search_surname(file_name):
    surname = input("Введите фамилию: ")
    phone_book = read_file(file_name)
    records_surname = [record for record in phone_book if surname.lower() in record["Фамилия"].lower()]
    if not records_surname:
        print("Фамилия не найдена в справочнике")
    else:
        for record in records_surname:
            print(record)


def edit_record(file_name):
    last_name = input("Введите фамилию для изменения: ").lower()
    first_name = input("Введите имя для изменения: ").lower()
    phone_book = read_file(file_name)
    record_edit = []
    for record in phone_book:
        if record["Фамилия"].lower() == last_name and record["Имя"].lower() == first_name:
            record_edit.append(record)

    if not record_edit:
        print("Запись не найдена в справочнике")
    else:
        new_information = get_info()
        for record in record_edit:
            record["Фамилия"] = new_information[0]
            record["Имя"] = new_information[1]
            record["Номер"] = new_information[2]

        with open(file_name, "w", encoding="utf-8", newline="") as f_n:
            f_n_writer = DictWriter(f_n, fieldnames=["Фамилия", "Имя", "Номер"])
            f_n_writer.writeheader()
            f_n_writer.writerows(phone_book)

        print("Запись изменена")


def delete_record(file_name):
    last_name = input("Введите фамилию для удаления: ")
    first_name = input("Введите имя для удаления: ")
    phone_book = read_file(file_name)
    record_delete = []
    for record in phone_book:
        if record["Фамилия"].lower() == last_name.lower() and record["Имя"].lower() == first_name.lower():
            record_delete.append(record)

    new_phone_book = [record for record in phone_book if record not in record_delete]

    with open(file_name, "w", encoding="utf-8", newline="") as f_n:
        f_n_writer = DictWriter(f_n, fieldnames=["Фамилия", "Имя", "Номер"])
        f_n_writer.writeheader()
        f_n_writer.writerows(new_phone_book)
    print("Запись удалена")


def main():
    while True:
        command = input("Введите команду: ")
        if command == "q":
            break
        elif command == "r":
            if not exists("phone.csv"):
                print("Файл не создан")
                break
            print(*read_file("phone.csv"))
        elif command == "w":
            if not exists("phone.csv"):
                create_file()
                record_info()
            else:
                record_info()
        elif command == "sn":
            search_name("phone.csv")
        elif command == "ss":
            search_surname("phone.csv")
        elif command == "d":
            delete_record("phone.csv")
        elif command == "e":
            edit_record("phone.csv")
        else:
            print("Вы ввели неверную команду")


main()
