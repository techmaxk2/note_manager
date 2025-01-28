titles = []

while True:
    title = input("Введите заголовок (оставьте пустым или введите 'стоп' для завершения): ")
    stop_list = ["стоп", ""]
    if title in stop_list:
        break
    elif title in titles:
        print("Такой заголовок уже был введен ранее.")
    else:
        titles.append(title)
        print("Заголовок успешно добавлен.")
if len(titles) > 0:
    print("\nСписок заголовков заметок:")
    for i, title in enumerate(titles):
        print(f"{i + 1}. {title}")
else:
    print("Вы не ввели ни одного заголовка.")




