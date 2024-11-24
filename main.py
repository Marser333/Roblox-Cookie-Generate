import random
import string
import os

def clear_console():
    # Очистка консоли в зависимости от операционной системы
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_warning():
    warning = "_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_"
    length_needed = random.randint(800, 1200) - len(warning)
    random_chars = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length_needed))
    return warning + random_chars

def print_pattern():
    pattern = """\
╔══╗╔════╗
║╔╗║╚═╗╔═╝
║╚╝╚╗─║║
║╔═╗║─║║
║╚═╝║─║║
╚═══╝─╚╝
╔═══╦═══╦╗─╔╦═══╦═══╦══╦════╦══╦═══╗
║╔══╣╔══╣╚═╝║╔══╣╔═╗║╔╗╠═╗╔═╣╔╗║╔═╗║
║║╔═╣╚══╣╔╗─║╚══╣╚═╝║╚╝║─║║─║║║║╚═╝║
║║╚╗║╔══╣║╚╗║╔══╣╔╗╔╣╔╗║─║║─║║║║╔╗╔╝
║╚═╝║╚══╣║─║║╚══╣║║║║║║║─║║─║╚╝║║║║
╚═══╩═══╩╝─╚╩═══╩╝╚╝╚╝╚╝─╚╝─╚══╩╝╚╝
"""
    print(pattern)

def main():
    # Выбор языка
    language = input("Выберите язык / Choose language (1 - Русский, 2 - English): ")
    
    if language == "1":
        messages = {
            "cookies_prompt": "Сколько куков нужно?",
            "requesting_cookies": "Запрашиваем {0} куков...",
            "success": "Успешно записано в файл: {0}",
            "error": "Введите корректное число.",
            "not_logged_in": "Вы не вошли в систему."
        }
    elif language == "2":
        messages = {
            "cookies_prompt": "How many cookies do you need?",
            "requesting_cookies": "We are requesting {0} cookies...",
            "success": "Successfully saved to file: {0}",
            "error": "Please enter a valid number.",
            "not_logged_in": "You are not logged in."
        }
    else:
        print("Неверный выбор языка. / Invalid language selection.")
        return

    logged_in = True

    while True:  # Бесконечный цикл
        clear_console()  # Очищаем консоль при каждом новом запуске

        if not logged_in:
            print(messages["not_logged_in"])  # Сообщение, когда не авторизованы

        print_pattern()  # Выводим текст

        try:
            cookies = int(input(messages["cookies_prompt"] + "\n"))
            print(messages["requesting_cookies"].format(cookies))

            unique_warnings = set()

            # Генерация уникальных предупреждений
            while len(unique_warnings) < cookies:
                new_warning = generate_warning()
                unique_warnings.add(new_warning)

            # Генерация случайного числа для имени файла
            random_suffix = random.randint(1000, 9999)
            filename = f'cookie_{cookies}_{random_suffix}.txt'

            # Запись уникальных предупреждений в файл с рандомным числом в имени
            with open(filename, 'w') as file:
                file.write('\n'.join(unique_warnings))

            print(messages["success"].format(filename))

        except ValueError:
            print(messages["error"])

if __name__ == "__main__":
    main()