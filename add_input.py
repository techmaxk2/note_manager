username = input("Имя пользователя: ")
title = input("Заголовок заметки: ")
content = input("Описание заметки: ")
status = input("Статус заметки: ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год: ") #"день-месяц-год", например "10-11-2024"
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год : ") #"день-месяц-год", например "10-12-2024"
print("Вы ввели следующие данные: ")
print("Имя пользователя:" , username)
print("Заголовок заметки:" , title)
print("Описание заметки:" , content)
print("Статус заметки:" , status)
print("Дата создания заметки:" , created_date)
print("Дата истечения заметки:" , issue_date)