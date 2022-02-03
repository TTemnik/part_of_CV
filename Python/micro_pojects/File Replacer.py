###
###

import os, sys, shutil

path = fr"E:\Downloads\Пусть Самурая\03.SQL\PostgreSQL\[OTUS] PostgreSQL (2020)"


def del_webinar_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            current_path = os.path.realpath(root)
            os.chdir(current_path)
            if ".mp4" in file and len(str(file)) < 10:
                print(file)
                os.remove(file)


def file_renamer(path):
    os.chdir(path)
    for root, dirs, files in os.walk(path):
        for file in files:
            current_path = os.path.realpath(root)
            os.chdir(current_path)
            if int(os.path.getsize(file)) > 1000000 and ".rar" not in file:
                new_name = f"(empty) {file}"
                try:
                    with open(f"{new_name}.txt", "w", encoding="utf-8") as txt_file:
                        txt_file.write("")
                    os.remove(file)

                except Exception:
                    print(Exception)
                print(new_name)

def main():
    file_renamer(path)
    # del_webinar_files(path)


if __name__ == '__main__':
    main()
