"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""


def main():
    with open('referat.txt', encoding='UTF-8') as read_file:
        read_txt = read_file.read()

    print(f'Длина строки: {len(read_txt)}')
    print(f'Количество слов в тексте: {len(read_txt.split())}')
    read_txt = read_txt.replace('.', '!')
    
    with open('referat2.txt', 'w', encoding='UTF-8') as write_file:
        write_file.write(read_txt)


if __name__ == "__main__":
    main()
