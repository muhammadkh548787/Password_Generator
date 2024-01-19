import datetime

def calculate_days_until_birthday(birthday):
    today = datetime.date.today()
    next_birthday = datetime.date(today.year, birthday.month, birthday.day)

    if next_birthday < today:
        next_birthday = datetime.date(today.year + 1, birthday.month, birthday.day)

    days_until_birthday = (next_birthday - today).days
    return days_until_birthday

def main():
    birthday = input("Введите дату своего дня рождения в формате ДД.ММ.ГГГГ: ")
    birthday = datetime.datetime.strptime(birthday, "%d.%m.%Y").date()

    days_until_birthday = calculate_days_until_birthday(birthday)
    print(f"До вашего следующего дня рождения осталось {days_until_birthday} дней.")

if __name__ == "__main__":
    main()