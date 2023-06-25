from dateutil.parser import parse
import tkinter as tk
from tkinter import *
import pymysql.cursors
from tkinter.messagebox import  showinfo, showerror
from crontab import CronTab
from datetime import datetime
import PySimpleGUI as sg
# Создание окна приложения
root = tk.Tk()
root.title('File Compare')
root.geometry('1000x600')
root.resizable(False, False)
def connect_to_database():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Pa$$w0rd",
        db="Apache_logs"
    )
    
    return conn
    

    

def get_logs():
    # Connect to the database
    conn = connect_to_database()
    if conn:
       showinfo(title = "Успешное подключение",message = "Подключение к базе данных выполнено успешно!")
    else:
        showerror(title = "Неудачное подключение",message = "Подключение к базе данных выполнено неуспешно!")

         
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM access_logs")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    # Create a label for each row of data
    for i in range(len(data)):
        row = data[i]
        show_logs.insert(tk.END, row)
        show_logs.insert(tk.END, "\n")

    # Run the window loop
    

def clear_logs():
    show_logs.delete('1.0', tk.END)

show_button = tk.Button(root, text="Подлкючить бд и вывести данные", command=get_logs)

def filtered_by_ip_address():
        show_logs.delete('1.0', tk.END)
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute("SELECT ip_address from access_logs")
        logs = []
        data = cursor.fetchall()
     
        for i in range(len(data)):
            logs = data[i]
            show_logs.insert(tk.END, logs)
            show_logs.insert(tk.END, "\n")
        cursor.close()
        conn.close() 

def filtered_by_date():
        show_logs.delete('1.0', tk.END)
        conn = connect_to_database()
        cursor = conn.cursor()
        cursor.execute("SELECT datee from access_logs")
        logs = []
        data = cursor.fetchall()
     
        for i in range(len(data)):
            logs = data[i]
            show_logs.insert(tk.END, logs)
            show_logs.insert(tk.END, "\n")
        cursor.close()
        conn.close() 



# Создание виджетов для вывода данных из базы данных
ip_filter_button = tk.Button(root, text="Фильтр по IP", command=filtered_by_ip_address)
date_filter_button = tk.Button(root, text="Фильтр по дате", command=filtered_by_date)
button_clear_labels = tk.Button(root, text="Очистить все", command= clear_logs)

# Размещение виджетов на окне приложения

show_button.pack()
ip_filter_button.pack()
date_filter_button.pack()


label_start_date = tk.Label(root, text="Начальная дата (DD/MM/YYYY): ")
label_start_date.pack()
entry_start_date = tk.Entry(root)
entry_start_date.pack()

label_end_date = tk.Label(root, text="Конечная дата (DD/MM/YYYY): ")
label_end_date.pack()
entry_end_date = tk.Entry(root)
entry_end_date.pack()
show_logs = tk.Text(root)

def get_logs_filtered_by_date_range():
    show_logs.delete('1.0', tk.END)
    start_date = entry_start_date.get()
    end_date = entry_end_date.get()

    try:
        conn = connect_to_database()
        cursor = conn.cursor()
        sql = "SELECT * FROM access_logs WHERE datee BETWEEN %s AND %s"
        cursor.execute(sql, (start_date, end_date))
        logs = []
        for row in cursor.fetchall():
            logs.append(row)
        for log in logs:
            show_logs.insert(tk.END, log)
            show_logs.insert(tk.END, "\n")
        cursor.close()
        conn.close() 
        
    except Exception as e:
        show_logs.insert(tk.END, "Error: " + str(e))

import subprocess

def create_task():
    task_name = sg.popup_get_text('Введите название задачи')
    time_str = sg.popup_get_text('Введите время (HH:MM)')
    command = "C:\\python\\apache_project\\app.py"
    try:
        # Создание задания в планировщике Windows
        args = f'schtasks /Create /SC DAILY /TN {task_name} /TR "python {command}" /ST {time_str}'
        subprocess.run(args, check=True)

        return True
    except subprocess.CalledProcessError as e:
        print(f"Error creating task: {e}")
        return False


            
show_button = tk.Button(root, text="Фильтр по промежутку даты", command=lambda:get_logs_filtered_by_date_range())
show_button.pack()
dd_button = tk.Button(root, text='Создать задачу', command=create_task)
dd_button.pack()
show_logs.pack()
button_clear_labels.pack()


root.mainloop()