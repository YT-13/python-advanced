import os


def count_word(file_path):
    with open(file_path, "r", encoding="latin-1") as file:
        file_content = file.read()

    input_word = input("Введіть слово >>> ")
    count = file_content.split().count(input_word)

    print(f"Слово {input_word} входить в файл {count} разів.")


# Отримати шлях до файлу на робочому столі під Linux
our_file = os.path.join(os.path.expanduser("~"), "Desktop", "rockyou.txt")

count_word(our_file)
