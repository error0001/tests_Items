import re
# re.match()
# re.search()
# re.findall()
# re.split()
# re.sub()
# re.compile()
import requests
import json


# Читаем из файла с помощью конструкции with
def read_file(filename):
    with open(filename) as some_file:
        return some_file.read()


# Записываем в файл с помощью конструкции with
def write_to_file(filename, content, mode='w'):
    with open(filename, mode=mode) as some_file:
        some_file.write(content)


# Test 1, with re
# При помощи requests скачиваем содержимое страниц
# reddit.com/r/python (любой тред 5 комментов) и вывести
# пару комметнов и его текстов в консоль
# http://docs.python-requests.org/en/master/user/quickstart/

if __name__ == '__main__':
    try:
        print("start app")
        some_texts = requests.get('https://habr.com/ru/',
                                  stream=True)

        print("HEADERS:\n", some_texts.headers)
        print("STATUS_CODE:\n", some_texts.status_code)
        # контент не можем взять, потому что лимит на скорость надо закинуть
        #print("CONTENT:\n", some_texts.content)
        #write_to_file("habr_html.txt", str(some_texts.content))
        post_list = re.findall(r'ul', str(some_texts.content))
        print('RE match:\n', post_list)
    finally:
        print("end app")
