# Задача No49. Общее обсуждение
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

import json
import os


def find_contact(contacts: list) -> None:
    what = input("Введите параметр по которому нужно найти контакт: \n")

    found = list(filter(lambda el: what in el['first_name'] or what in el['second_name'] or what in el['contacts'],
                        contacts))
    if found:
        show_on_screen(found)
    else:
        print('Такого контакта нет :с')


def file_path(file_name='contact_list'):
    return os.path.join(os.path.dirname(__file__), f'{file_name}.txt')


def load_from_file() -> list:
    path = file_path()

    with open(path, 'r', encoding='UTF-8') as file:
        data = json.load(file)

    return data


def save_to_file(contact: list) -> None:
    path = file_path()

    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(contact, file, ensure_ascii=False)


def show_on_screen(contacts: list) -> None:
    decode_keys = dict(
        first_name='Имя: ',
        second_name='Фамилия: ',
        contacts='Номер телефона: '
    )
    pretty_text = str()
    for num, elem in enumerate(contacts, 1):
        pretty_text += f'Контакт №{num}:\n'
        pretty_text += '\n'.join(f'{decode_keys[k]} {v}' for k, v in elem.items())
        pretty_text += '\n________\n'
    print(pretty_text)


def create_contact_dict():
    pass


def new_contact(contacts: list) -> None:
    contacts.append(
        dict(
            first_name=input('Введите имя контакта: \n>>> '),
            second_name=input('Введите фамилию контакта: \n>>> '),
            contacts=input('Введите номер телефона: \n>>> ')
        )
    )


def delite_contact(contacts: list) -> None:
    name = input('Введите имя контакта, который нужно удалить?\n>>> ')
    family = input('Введите фамилию контакта, который нужно удалить?\n>>> ')
    found = list(filter(lambda el: name in el['first_name'] and family in el['second_name'], contacts))
    if len(found) <= 0:
        print('Такого контакта нет :с')
    elif len(found) > 0:
        ind = contacts.index(found[0])
        print(ind)
        contacts.pop(ind)


def change_contact(contacts: list):
    name = input('Введите имя контакта, который нужно изменить?\n>>> ')
    family = input('Введите фамилию контакта, который нужно изменить?\n>>> ')
    found = list(filter(lambda el: name in el['first_name'] and family in el['second_name'], contacts))
    print(found)
    ind = 0
    res = 0
    for i in contacts:
        if i == found[0]:
            res = ind
        ind += 1
    contacts[res] = dict(
        first_name=input('Введите новое имя контакта: \n>>> '),
        second_name=input('Введите новую фамилию контакта: \n>>> '),
        contacts=input('Введите новый номер телефона: \n>>> ')
    )
    return contacts

def menu(data: list):
    command = -1
    commands = [
        'Выйти из меню', # Выключить программу
        'Показать все контакты',
        'Найти контакт',
        'Создать контакт',
        'Удалить контакт',
        'Изменить контакт'
    ]
    while command != 0:
        print('=====МЕНЮ=====')
        print('\n'.join(f'{n}. {v}' for n, v in enumerate(commands)))
        command = int(input(f'\nУкажите номер команды: \n'))
        if command == 1:
            show_on_screen(data)
        elif command == 2:
            find_contact(data)
        elif command == 3:
            new_contact(data)
        elif command == 4:
            delite_contact(data)
        elif command == 5:
            change_contact(data)
        else:
            print(f'Такой команды не существует!\n')


def main() -> None:
    data = load_from_file()
    menu(data)

    save_to_file(data)


if __name__ == '__main__':
    main()
