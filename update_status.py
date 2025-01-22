def get_current_status():
    return input("Введите текущий статус заметки: ").strip().lower()
def display_statuses():
    print("\nДоступны следующие статусы:\n")
    for index, status in enumerate(statuses):
        print(f"{index + 1}. {status.title()}")
def validate_choice(choice):
    if choice.isdigit():
        choice = int(choice)
        if 0 < choice <= len(statuses):
            return statuses[choice - 1].lower()
    elif choice.lower() in statuses:
        return choice.lower()
    return None
def update_status(current_status):
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
    current_status = {"status": ""}
    current_status["status"] = get_current_status()
    while True:
        print(f"Текущий статус заметки: {current_status['status'].title()}")
        update_status(current_status)

if __name__ == "__main__":
    statuses = ["выполнено", "в процессе", "отложено"]
    main()
