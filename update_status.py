statuses = ["выполнено", "в процессе", "отложено"]
def main():
    current_status = statuses[2]
    while True:
        print(f"\nТекущий статус заметки: {current_status}")

        print("\nВыберите новый статус заметки:")
        for i, status in enumerate(statuses):
            print(f"{i + 1}. {status}")
        try:
            choice = int(input("\nВаш выбор: "))
            if 0 < choice <= len(statuses):
                new_status = statuses[choice - 1]
                current_status = new_status
                print(f"\nСтатус заметки успешно обновлен на: {new_status}")
                break
            else:
                print("\nНекорректный ввод! Попробуйте снова.")
        except ValueError:
            print("\nНекорректный ввод! Пожалуйста, введите число.")
if __name__ == "__main__":
    main()
