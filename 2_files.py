"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""


def count_string_len(text):
    return len(text)


def count_words_in_text(text):
    return len(text.split())


def replace_dots_with_exclamation_marks(text):
    return text.replace('.', '!')


def main():
    with open('referat.txt', encoding='UTF-8') as read_file:
        read_txt = read_file.read()

    print(f'Длина строки: {count_string_len(read_txt)}')
    print(f'Количество слов в тексте: {count_words_in_text(read_txt)}')
    read_txt = replace_dots_with_exclamation_marks(read_txt)

    with open('referat2.txt', 'w', encoding='UTF-8') as write_file:
        write_file.write(read_txt)


if __name__ == "__main__":
    main()
