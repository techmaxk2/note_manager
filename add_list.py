username = input("Имя пользователя: ")
content = input("Описание заметки: ")
status = input("Статус заметки: ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год: ") #"день-месяц-год", например "10-11-2024"
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год : ") #"день-месяц-год", например "10-12-2024"

titles = []
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    titles.append(title)

print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовки заметки:", titles)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", issue_date)
