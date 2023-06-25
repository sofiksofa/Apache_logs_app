import logging
from flask import Flask, jsonify
import re

site = Flask(__name__)

@site.route('/', methods=['GET'])
def index():
    logging.basicConfig(
        filename="C:\\python\\apache_project\\access.log",  # имя файла для записи логов
        format='%(asctime)s %(levelname)s %(message)s',
        level=logging.DEBUG
    )
    try:
        result = 1 / 0
    except Exception as e:
        # записываем лог ошибки
        logging.error('Ошибка: %s', e)

    return 'Hello, World!'

if __name__ == '__main__':
   site.run()