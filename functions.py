from data_create import *


def add_note():
    notes = read_file()
    note = create_note()
    notes.append(note)
    overwrite_file(notes)


def edit_note():
    selected_id = input("Введите номер заметки: ")
    while not selected_id.isdigit():
        print("Некорректный ввод")
        selected_id = input("Введите номер заметки: ")
    selected_id = int(selected_id)
    notes = read_file()
    for el in notes:
        if selected_id == int(el['Id']):
            el['Title'] = input('Введите заголовок заметки: ')
            el['Note_body'] = input('Введите тело заметки: ')
            el['Creation_date'] = datetime.now().date()
            overwrite_file(notes)
            return
    print('Такой заметки нет')


def delete_note():
    selected_id = input("Введите номер заметки: ")
    while not selected_id.isdigit():
        print("Некорректный ввод")
        selected_id = input("Введите номер заметки: ")
    selected_id = int(selected_id)
    notes = read_file()
    for el in notes:
        if selected_id == int(el['Id']):
            notes.remove(el)
            overwrite_file(notes)
            return
    print('Такой заметки нет')


def filter_notes_by_date():
    selected_date = input("Введите дату в формате ГГГГ-ММ-ДД: ")
    notes = read_file()
    flag = False
    for el in notes:
        if selected_date == el['Creation_date']:
            el['Creation_date'] = selected_date
            print(el)
            flag = True
    if not flag:
        print('Такой даты нет')


def show_all_notes():
    notes = read_file()
    for el in notes:
        print(el)