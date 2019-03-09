import re


# Читаем из файла с помощью конструкции with
def read_file(filename):
    with open(filename) as some_file:
        return some_file.read()


# Записываем в файл с помощью конструкции with
def write_to_file(filename, content, mode='w'):
    with open(filename, mode=mode) as some_file:
        some_file.write(content)


if __name__ == '__main__':
    try:
        print("start app")

    finally:
        print("end app")
