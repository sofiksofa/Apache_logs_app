import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import re
import logging
def parse_access_log(log_str, db):
    # Извлечение данных из строки лога
    # pattern = r'^(\d{1,3}\.\d{1,3}\.\d{0,3}\.\d{1,3}) (\S+) (\S+) \[(\d{2}\/\w{3}\/\d{4}):(\d{2}:\d{2}:\d{2})\] "(\S+)\s?(\S+)?\s?(\S+)?" (\d{3}) (\d+)\s?"?([^"]*)"?\s?"?([^"]*)?"?$'
    pattern = r'^(127\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(\d{2}/[A-Za-z]{3}/\d{4})\s?(\d{2}:\d{2}:\d{2})\] "(\S+)\s?(\S+)?\s?(\S+)?" (\d{3}) (\d+|-)$'
    match = re.match(pattern, log_str)
    if match is None:
         raise ValueError('Строка не соответствует регулярному выражению')
    # ip_address, identity, username, datee, timee,  request_method, request_uri, http_version, status_code, byte_count, referer, user_agent = match.groups()
    ip_address,  datee, timee,  request_method, request_uri, http_version, status_code, byte_count = match.groups()

    with db.cursor() as cur:
        cur.execute("""
                INSERT INTO access_logs (ip_address,  datee, timee,  request_method, request_uri, http_version, status_code, byte_count)
                VALUES (%s, %s,%s,%s,%s,%s,%s,%s);
            """, (ip_address,  datee, timee, request_method, request_uri, http_version, status_code, byte_count))

        db.commit()
        print("Данные успешно сохранены в базу данных!")
        return True
    
      
    

def read_access_log(file_path, db):
    with open(file_path, 'r') as file:
        db.connect()
        for line in file:
            parse_access_log(line, db)
        db.close()


try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pa$$w0rd",
        database="Apache_logs"
    )
    read_access_log("C:\\python\\apache_project\\access.log", db)
except Error as e:
    print(f"Ошибка: {e}")
finally:
    db.close()