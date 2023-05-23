"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime as dt, timedelta as td


def print_days():
    return [(dt.today() - td(days=1)).strftime('%d.%m.%Y'), (dt.today()).strftime('%d.%m.%Y'),
            (dt.today() - td(days=30)).strftime('%d.%m.%Y')]


def str_2_datetime(date_string):
    return dt.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')


if __name__ == "__main__":
    print(*print_days(), sep='\n')
    print(str_2_datetime("01/01/20 12:10:03.234567"))
