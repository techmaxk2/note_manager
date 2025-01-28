import datetime
class NoteManager:
    def __init__(self):
        self.notes = []
    def add_note(self):
        username = input("Введите имя пользователя: ")
        title = input("Введите заголовок заметки: ")
        description = input("Введите описание заметки: ")
        status = input("Введите статус заметки (новая, в процессе, выполнено): ").lower()
        while True:
            creation_date_str = input("Введите дату создания (день-месяц-год): ")
            try:
                creation_date = datetime.datetime.strptime(creation_date_str, "%d-%m-%Y").date()
                break
            except ValueError:
                print("Неверный формат даты. Пожалуйста, введите дату в формате день-месяц-год (например, 01-12-2023).")
        while True:
            deadline_str = input("Введите дедлайн (день-месяц-год): ")
            try:
                deadline = datetime.datetime.strptime(deadline_str, "%d-%m-%Y").date()
                break
            except ValueError:
                print("Неверный формат даты. Пожалуйста, введите дату в формате день-месяц-год (например, 31-12-2023).")
        note = {
            'Имя пользователя': username,
            'Заголовок заметки': title,
            'Описание заметки': description,
            'Статус заметки': status,
            'Дата создания': creation_date,
            'Дедлайн': deadline
        }
        self.notes.append(note)
        print("\nЗаметка успешно добавлена!\n")
    def show_notes(self):

        if not self.notes:
            print("\nУ вас пока нет заметок.\n")
            return
        print("\nСписок ваших заметок:\n")
        for index, note in enumerate(self.notes):
            print(f"Заметка #{index + 1}:")
            for key, value in note.items():
                if isinstance(value, datetime.date):
                    value = value.strftime("%d-%m-%Y")
                print(f"{key.capitalize()}: {value}")
            print()
    def run(self):

        print("Добро пожаловать в 'Менеджер заметок'! Вы можете добавить новую заметку.")
        while True:
            choice = input("\nХотите добавить ещё одну заметку? (да/нет): ").lower()
            if choice == 'да':
                self.add_note()
            elif choice == 'нет':
                break
            else:
                print("Пожалуйста, введите 'да' или 'нет'.")
        self.show_notes()
if __name__ == "__main__":
    manager = NoteManager()
    manager.run()
