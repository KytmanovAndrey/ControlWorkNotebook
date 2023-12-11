from functions import *
from os.path import exists


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