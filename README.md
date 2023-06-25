<h1>Парсер Apache логов</h1>
Apache-parser позволяет вам анализировать и взаимодейстовать с логами на базе MySQL и Flask. Данное мини-приложение разработано в рамках учебной практики.

<h2>Возможности</h2>
<ul style="list-style-type: square;">
  
  <li>Программа считывает данные из журнала доступа Apache и разбирает его на нужные данные, такую как IP-адрес, дату и время, HTTP-метод, ресурс, протокол, код состояния и размер.</li>
  <li>Перенаправляет и сохраняет извлеченную информацию в базу данных MySQL.</li>
  <li>Предоставляет возможность извлечения нужных записей в программу без полного доступа к базе данных.</li>
  <li>Использование веб-сервера Flask для обработки данных журнала и отчетов.</li>
  <li>Возможность фильтра данных по IP, дате, нужному промежутку дат.</li>

</ul>

<h2>Установка</h2>
 
1. Склонируйте репозиторий проекта:

   ```
   git clone https://github.com/sofiksofa/Apache_logs_app.git
   ```
2. Установите необходимые библиотеки:
      ```
      pip install -r requirements.txt
   ```
3. Поменяйте в файлах config.ini, app.py, parsing.py данные базы данных и путь к файлу логов.

<h2>Старт</h2>   
1. Укажите в консоли путь до файла app.py:
  ```
      cd Папка/Папка/Папка/app.py
   ```

2. Запуск приложения :
      ```
      python app.py
   ```
<h3>Применение</h3>

Первый этап необязателен.
1. Запустите файл flask_site.py и скопируйте вышедшую ссылку на веб-сайт. Перейдя на него в файл access.logs автоматически добавляются записи о ваших действиях.  

2. Запустите приложение для парсинга в базу данных:
       ```
      python parsing.py
   ```
3. Подключение к MySQL и вывод данных в приложение осуществляется одной кнопкой.
   После того как вы нажмете на нее, выйдет сообщение о положительном или отрицательном подключении, в зависимости от правильности подключения:
   ![image](https://github.com/sofiksofa/Apache_logs_app/assets/137713536/02c99e12-7e18-4eee-bb52-6e4d127f8dea)

   ![image](https://github.com/sofiksofa/Apache_logs_app/assets/137713536/b0e77a98-d27b-4682-830b-c43858df93d0)
   Далее вы увидите данные в текстовом блоке:
   ![image](https://github.com/sofiksofa/Apache_logs_app/assets/137713536/585703a2-c742-4019-a6b8-69af9a22f5ea)
   
4. Кнопка "Фильтр по IP" подключается к базе данных и извлекает из таблицы данные сгруппированные по IP:
   ![image](https://github.com/sofiksofa/Apache_logs_app/assets/137713536/d4caad32-d908-44ca-89d3-a4102fa9f382)

   ![image](https://github.com/sofiksofa/Apache_logs_app/assets/137713536/355ca097-5910-49f7-8250-aa134eed0f8b)
   
5. Кнопка "Фильтр по дате" подключается к базе данных и извлекает из таблицы данные сгруппированные по дате:
   ![image](https://github.com/sofiksofa/Apache_logs_app/assets/137713536/0b5a145c-35cb-4432-b3e1-b4ae73b39e50)

   ![image](https://github.com/sofiksofa/Apache_logs_app/assets/137713536/3e12a639-a7ec-4a08-a6e4-03ab74a9e215)
   
6. Кнопка "Фильтр по дате" также извлекает из таблицы базы данных информацию, но только ту которая входит во вписанный вручную диапазон:
   ![image](https://github.com/sofiksofa/Apache_logs_app/assets/137713536/a2dc72ac-a474-4fd8-b439-2f147368625e)
   
   ![image](https://github.com/sofiksofa/Apache_logs_app/assets/137713536/ac8a3eea-92de-4481-a700-37a5e676dc47)

<h3>Создание задачи</h3>
В app.py прописан скрипт, которыйзапускает скрипт обновления сведений базы данных в указанное время.

Кнопка "Создать задачу" выводит окно с заполнением названия задачи и времени. Подключаясь к планировщику задач, создается событие:
   ![image](https://github.com/sofiksofa/Apache_logs_app/assets/137713536/a876835a-11cb-4726-bd38-b16f4182321b)

   


