from os.path import exists
from datetime import datetime
from csv import DictReader, DictWriter


def create_file():
    with open('notebook.csv', "w", encoding="utf-8") as data:
        f_writer = DictWriter(data, fieldnames=['Id', 'Title', 'Note_body', 'Creation_date'], delimiter=';')
        f_writer.writeheader()


def read_file():
    with open('notebook.csv', 'r', encoding='utf-8') as csvfile:
        reader = DictReader(csvfile, delimiter=';')
        notes = list(reader)
    return notes


def overwrite_file(notes):
    with open('notebook.csv', "w", newline='', encoding="utf-8") as data:
        f_writer = DictWriter(data, fieldnames=['Id', 'Title', 'Note_body', 'Creation_date'], delimiter=';')
        f_writer.writeheader()
        f_writer.writerows(notes)


def create_note():
    notes = read_file()
    max_id = 1
    for el in notes:
        if max_id <= int(el['Id']):
            max_id = int(el['Id']) + 1
    title = input('Введите заголовок заметки: ')
    note_body = input('Введите тело заметки: ')
    creation_date = datetime.now().date()
    note = {'Id': max_id, 'Title': title, 'Note_body': note_body, 'Creation_date': creation_date}
    return note

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


def user_interface():
    if not exists('notebook.csv'):
        create_file()
    cmd = None
    while cmd != '6':
        print('\nМеню:\n'
              '1. Добавить заметку\n'
              '2. Редактировать заметку по номеру\n'
              '3. Удалить заметку\n'
              '4. Фильтрация заметок по дате\n'
              '5. Показать все заметки на экране\n'
              '6. Выход')
        cmd = input('Введите номер операции: ')
        while cmd not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод')
            cmd = input('Введите номер операции: ')
        match cmd:
            case '1':
                add_note()
            case '2':
                edit_note()
            case '3':
                delete_note()
            case '4':
                filter_notes_by_date()
            case '5':
                show_all_notes()
            case '6':
                print('До свидания))')


user_interface()
