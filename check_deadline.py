from datetime import datetime

def validate_date(input_date):

    try:
        date = datetime.strptime(input_date, '%d-%m-%Y')
        return date.date()
    except ValueError:
        return None

def check_deadline():

    current_date = datetime.now().date()
    while True:
        issue_date_input = input("Введите дату дедлайна в формате 'день-месяц-год': ")
        issue_date = validate_date(issue_date_input)
        if issue_date:
            break
        else:
            print("Неверный формат даты. Попробуйте еще раз.")
    if issue_date < current_date:
        print(f"Дедлайн истёк {current_date - issue_date} дней назад.")
    elif issue_date > current_date:
        print(f"До дедлайна осталось {issue_date - current_date} дней.")
    else:
        print("Сегодня последний день для выполнения задания!")
check_deadline()
