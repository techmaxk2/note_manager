note = {'title': "Имя", 'text': "Текст", 'status': "закрыта"}
statuses = {1: "выполнено", 2: "в процессе", 3: "отложено"}
note['status'] = statuses[1]

def main():

    while True:
        print(f"\nТекущий статус заметки: ", note['status'])

        print("\nВыберите новый статус заметки:")
        for i in statuses:
            print(f"{i}. {statuses[i]}")
        try:
            choice = int(input("\nВаш выбор: "))
            if 0 < choice <= len(statuses):
                note['status'] = statuses[choice]
                print(f"\nСтатус заметки успешно обновлен на: {note['status']}")
                break
            else:
                print("\nНекорректный ввод! Попробуйте снова.")
        except ValueError:
            print("\nНекорректный ввод! Пожалуйста, введите число.")
if __name__ == "__main__":
    main()
    print(note)
