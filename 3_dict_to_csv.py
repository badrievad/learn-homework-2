"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


def main():
    data_list = [
        {'name': 'John', 'age': 26, 'job': 'economist'},
        {'name': 'Debra', 'age': 35, 'job': 'accountant'},
        {'name': 'Ben', 'age': 14, 'job': 'unemployed'},
        {'name': 'Bob', 'age': 42, 'job': 'programmer'},
        {'name': 'Silvia', 'age': 21, 'job': 'designer'}
    ]

    with open('data.csv', 'w', newline='') as file:
        titles = ['name', 'age', 'job']
        writer = csv.DictWriter(file, titles, delimiter=';')
        writer.writeheader()
        for user in data_list:
            writer.writerow(user)

if __name__ == "__main__":
    main()
