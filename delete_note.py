def remove_notes_by_criteria(notes, criteria_type, criteria_value):
    updated_notes = []
    removed_count = 0

    for note in notes:
        if note[criteria_type] != criteria_value:
            updated_notes.append(note)
        else:
            removed_count += 1

    if removed_count > 0:
        print(f"Успешно удалено {removed_count} заметок.")
    else:
        print("Заметок с таким именем пользователя или заголовком не найдено.")

    return updated_notes

def display_notes(notes):

    if not notes:
        print("\nНет заметок для отображения.")
        return

    print("\nТекущие заметки:")
    for index, note in enumerate(notes):
        print(f"{index + 1}. Имя: {note['username']}\n   Заголовок: {note['title']}\n   Описание: {note['description']}\n")

def main():

    notes = [
        {'username': 'Максим', 'title': 'Машина', 'description': 'Помыть машину'},
        {'username': 'Елена', 'title': 'Учеба', 'description': 'Сделать домашнюю работу'},
        {'username': 'Виктория', 'title': 'Танцы', 'description': 'Выступить на соревнованиях'}
    ]

    while True:
        display_notes(notes)
        print("\n1. Удалить заметки по имени пользователя или заголовку")
        print("2. Завершить программу")
        choice = input("\nВведите ваш выбор: ")
        if choice == '1':
            criteria = input("Введите имя пользователя или заголовок для удаления заметки: ")
            notes = remove_notes_by_criteria(notes, 'username', criteria) or \
                    remove_notes_by_criteria(notes, 'title', criteria)
        elif choice == '2':
            print("\nПрограмма завершена.")
            break
        else:
            print("\nНеправильный ввод. Попробуйте еще раз.")
if __name__ == "__main__":
    main()