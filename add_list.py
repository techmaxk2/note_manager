username = input("Имя пользователя: ")
content = input("Описание заметки: ")
status = input("Статус заметки: ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год: ") #"день-месяц-год", например "10-11-2024"
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год : ") #"день-месяц-год", например "10-12-2024"

# titles = []
# for i in range(3):
#     title = input(f"Введите заголовок заметки {i + 1}: ")
#     titles.append(title)


title1 = input("Введите первый заголовок: ")
title2 = input("Введите второй заголовок: ")
title3 = input("Введите третий заголовок: ")
notes_titles = []
notes_titles.append(title1)
notes_titles.append(title2)
notes_titles.append(title3)




print("Вы ввели следующие данные:")
print("Имя пользователя:", username)
print("Список заголовков ваших заметок: " , notes_titles)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:" , created_date[0:5])
print("Дата истечения заметки:" , created_date[0:5])
