# from datetime import datetime
#
# # current_datetime = datetime.now()
#
# datetime.datetime.combine(date_object, time_object)


# print(current_datetime.year)
# print(current_datetime.month)
# print(current_datetime.day)
# print(current_datetime.hour)
# print(current_datetime.minute)
# print(current_datetime.second)
# print(current_datetime.microsecond)
# print(current_datetime.tzinfo)

# print(current_datetime.date())
# print(current_datetime.time())
#
# import datetime

# # Створення об'єктів date і time
# date_part = datetime.date(2023, 12, 14)
# time_part = datetime.time(12, 30, 15)
#
# # Комбінування дати і часу в один об'єкт datetime
# combined_datetime = datetime.datetime.combine(date_part, time_part)
# print(combined_datetime)

# # Створення об'єкта datetime з конкретною датою і часом
# specific_datetime = datetime.datetime(2020, 1, 7, 14, 30, 15)
#
# print(specific_datetime)  # Виведе "2020-01-07 14:30:15"


# from datetime import datetime
# # Створення об'єкта datetime
# now = datetime.now()
#
# # Отримання номера дня тижня
# day_of_week = 1 + now.weekday()
#
# # Поверне число від 0 (понеділок) до 6 (неділя)
# print(f"Сьогодні: {day_of_week}")



# from datetime import timedelta
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# print(delta)




# from datetime import datetime, timedelta
#
# now = datetime.now()
# future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
# print(future_date)





# from datetime import datetime
#
# # Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
# napoleon_burns_moscow = datetime(year=1812, month=9, day=14)
#
# # Поточна дата
# current_date = datetime.now()
#
# # Розрахунок кількості днів
# days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
# print(days_since)


# from datetime import datetime
#
# # Поточна дата та час
# now = datetime.now()
#
# # Конвертація у формат ISO 8601
# iso_format = now.isoformat()
# print(type(iso_format), iso_format)

#
#
# from datetime import datetime
#
# # Створення об'єкта datetime
# now = datetime.now()
#
# # Використання isoweekday() для отримання дня тижня
# day_of_week = now.isoweekday()
#
# print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7, що відповідає дню тижня



#
# from datetime import datetime
#
# # Створення об'єкта datetime
# now = datetime.now()
#
# # Отримання ISO календаря
# iso_calendar = now.isocalendar()
#
# print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")
#
# print(iso_calendar)


# import datetime
# from datetime import datetime, timezone
#
# local_now = datetime.now()
# utc_now = datetime.now(timezone.utc)
#
# print(local_now)
# print(utc_now)  # Виведе поточний час в UTC

# main.py
# from tack_6 import say_hello as greeting
# def main():
#     print("You imported hello.py")
#     greeting('user')
#
# if __name__ == '__main__':
#     main()

import sys

def main():
    if len(sys.argv) > 1:
        print(sys.argv[1])

if __name__ == "__main__":
    main()

