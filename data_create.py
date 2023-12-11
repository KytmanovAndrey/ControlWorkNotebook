from csv import DictReader, DictWriter
from datetime import datetime


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