"""
ПО для рекурсивного обхода папки и подпапок для поиска и переименования файлов,
название кот. сод. искомый текст.


Дальнейшее содержимое комментария - лишь черновик для автора.

В идеале:
1) Открывается .exe файлом
2) Есть GUI.
3) Выбрать в проводнике / ввести путь к папке (в кот. будет произведён рекурсивный обход).
4) Выбрать в выпадающем меню / вписать искомый текст.
5) Выбрать / вписать текст замены.
6) Кнопка ОК.
7) Уведомление об успешном завершении работы.


Шаги:

- Выбор папки
- Выбор иском. текста
- Выбор нового текста

1) Рекурсивный обход
2) Переименование



Вывод в консоли:
Тек. папка:
"blablabla"

Список подпапок:
[1, 2, 3, 4, 5]

Список файлов:
[1, 2, 3]



Механизм работы:
0) Доступный функционал:
    - Удалить ненужные файлы с опр. именем (напр. рекламные ссылки на сайт)
    - Переименовать файлы, имеющие опр. подпись в имени

1) Выбираешь папку, в кот будешь искать все папки и файлы с лишним текстом (подписью по типу [My_School]) в названии.
2) Выбираешь подпись, кот будешь искать
3) Выбираешь переименовать/удалить.
    3.1) Выбираешь замену для этой подписи
4) Нажимаешь "START"
5) Получаешь сообщение об успешном выполнении / об ошибке.


1) Выбор папки:
- Выбрать через стандартное окно проводника.
- Вставить путь до корневой папки

2) Список подписей состоит из:
- Выпадающий список, в кот можно:
    - выбрать любое значние из списка*
    * пример списка: ['SHERWOOD', 'SHWD', 'SKLAD']
    - выбрать все значнеия из списка
    - добавить свой вариант в список
    - выбрать свой вариант

3) Список замен для подписи состоит из:
- Выпадающий список, в от можно:
    - выбрать любое значние из списка*
    * пример списка: [' ', '']
    - добавить свой вариант в список
    - выбрать свой вариант

4) Сообщение по типу:
    - "Process had been succeeded!"
    - "Error in the process!"


В идеале:
1) Открывается .exe файлом
2) GUI
3) Выбрать в проводнике / ввести путь к папке (в кот. будет рекурсивный обход).
4) Выбрать в выпадающем меню / вписать искомый текст.
5) Выбрать / вписать текст замены.
6) Кнопка ОК
7) Уведомление об успешном завершении работы.

"""

import os
import shutil
import zipfile


def count_tree_lvls(path):
    max_leaf_len = 0
    max_path = None
    for root, dirs, files in os.walk(path):
        if len(root) > max_leaf_len:
            max_leaf_len = len(root)
            max_path = root
    all_slash_count = max_path.count('\\')
    root_slash_count = path.count('\\')
    walk_count = all_slash_count - root_slash_count + 1
    return walk_count


def recurse_walk_rename(path, labels_list):
    os.chdir(path)

    for root, dirs, files in os.walk(path):
        for dir in dirs:
            for label in labels_list:
                if label in dir:
                    current_path = os.path.realpath(root)
                    os.chdir(current_path)
                    label_ends = dir.index(']') + 2
                    os.rename(dir, dir[label_ends::])

        for file in files:
            for label in labels_list:
                if label in file:
                    current_path = os.path.realpath(root)
                    os.chdir(current_path)
                    label_ends = file.index(']') + 2
                    os.rename(file, file[label_ends::])


def tree_walking(path, labels_list):
    tree_count = count_tree_lvls(path)
    while tree_count > 0:
        recurse_walk_rename(path, labels_list)
        tree_count -= 1


def delete_useless_files(path, trash_names):  # Works correctly
    os.chdir(path)
    trash_count = 0

    for root, dirs, files in os.walk(os.curdir):
        for file in files:
            if any(trash in file for trash in trash_names):
                trash_count += 1
                path = os.path.realpath(fr"{root}\{file}")
                os.remove(path)
    print(f"Done, all trash was removed! \n trash_count= {trash_count} \n")


def rename_start_root(path, labels_list):
    os.chdir(path)
    if any(label in path for label in labels_list):
        print("TRASH NAME IN ROOT DIR!")
        print(os.path.realpath(os.curdir))
        os.chdir('..')
        print(os.path.realpath(os.curdir))

        scan = dict(os.scandir(os.curdir))
        print(scan)
        # for dir in [dict(os.listdir)]:
        #     print(dir)
        # os.rename()


def unpack_zip(zip_path, direction_path, name):
    os.chdir(zip_path)
    new_path = fr"{direction_path}\{name[:-3:]}"
    File = zipfile.ZipFile(name, 'r')
    File.extractall(path=new_path)


def clean_root_dir(path):
    os.chdir(path)
    if len([os.listdir]) == 0:
        print("Empty Training Dir")
    else:
        for root, dirs, files in os.walk(os.curdir):
            for dir in dirs:
                shutil.rmtree(dir)


def reset_tree(Training_Path, zip_path, zip_name):
    # Cleaning
    clean_root_dir(Training_Path)
    # Unpacking ZipFile
    unpack_zip(zip_path=zip_path, direction_path=Training_Path, name=zip_name)


def main():
    trash_names = ['Качай курсы беслпатно!', 'Обязательно к прочтению', "Прочти_перед_изучением!",
                   'Прочти перед изучением', 'zerkalo', 'ZERKALO', "Платное_теперь_бесплатно!"]
    labels_list = ["[GoQAOnline]", "[sharewood.band]", "[sharewood.biz]", "[MEGASLIV.BIZ]", "[SWD]", "[SW.BAND]"]
    path = fr"E:\Downloads\Пусть Самурая\QA\Backlog\03.SQL\PostgreSQL\[Илья Фофанов] Практический курс для новичков по SQL и PostgreSQL (2019)"
    # Tree walking and renaming
    tree_walking(path, labels_list)

    # Trash deleting
    delete_useless_files(path, trash_names)

    # Rename starter root dir
    # rename_start_root(path, labels_list)


if __name__ == '__main__':
    main()
