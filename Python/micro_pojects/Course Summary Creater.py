import os, shutil


def pars_summary(text):
    temp_text = text.split(sep='\n    ')
    return temp_text


def main(path, text, template_file_name):
    os.chdir(path)
    print(os.path.abspath(os.curdir))

    summary = pars_summary(text)
    num = 1

    if len(os.listdir(os.curdir)) <= 1:
        for name in summary:
            shutil.copy(template_file_name, f"[Ольга Павликова] Модуль {num} ({name}).docx")
            print(f"New file name is: {name}")
            num += 1
    else:
        print("There are more than 1 Template file in this Dir...")


if __name__ == '__main__':
    path = fr"C:\Users\artem\Dropbox\Samurai_Path\QA\[Ольга Павликова] PostgreSQL (2020)"
    template_file_name = "[Ольга Павликова] Модуль Х.docx"

    name_list = """Введение
    Основы
    Группировка данных
    Тест №1
    Соединения
    Расширенные команды
    Тест №2
    Создание БД и Таблиц
    Тест №3
    Бонусы"""

    main(path, name_list, template_file_name)
