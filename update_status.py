def get_current_status():
    """Запрашивает текущий статус заметки."""
    return input("Введите текущий статус заметки: ").strip().lower()


def display_statuses():
    """Отображает доступные статусы для выбора."""
    print("\nДоступны следующие статусы:\n")
    for index, status in enumerate(statuses):
        print(f"{index + 1}. {status.title()}")


def validate_choice(choice):
    """Проверяет, является ли введенный пользователем статус допустимым."""
    if choice.isdigit():  # Проверка на числовой ввод
        choice = int(choice)
        if 0 < choice <= len(statuses):
            return statuses[choice - 1].lower()
    elif choice.lower() in statuses:  # Проверка на текстовый ввод
        return choice.lower()
    return None


def update_status(current_status):
    """Обновляет статус заметки на основании ввода пользователя."""
    while True:
        display_statuses()
        user_input = input("\nПожалуйста, выберите новый статус (можно ввести текст или номер): ").strip().lower()
        new_status = validate_choice(user_input)
        if new_status is not None:
            current_status["status"] = new_status
            print(f"\nНовый статус заметки: {new_status.title()}\n")
            break
        else:
            print("\nНекорректный ввод! Попробуйте еще раз.\n")


def main():
    # Словарь для хранения текущего статуса заметки
    current_status = {"status": ""}

    # Получаем начальный статус
    current_status["status"] = get_current_status()

    # Основной цикл обновления статуса
    while True:
        print(f"Текущий статус заметки: {current_status['status'].title()}")
        update_status(current_status)

        # Вопрос о продолжении работы программы
        continue_program = input("Хотите обновить статус ещё раз? (да/нет): ").strip().lower()
        if continue_program != 'да':
            break


if __name__ == "__main__":
    # Возможные статусы заметок
    statuses = ["выполнено", "в процессе", "отложено"]
    main()
