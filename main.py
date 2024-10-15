import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

a = int(input("1.Создать таблицу"
              "\n2.Добавить данные"
              "\n3.Удалить данные"
              "\n4.Запрос на поиск"
              "\nВыберите действие: "))
if a == 1: # создание таблицы

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    age INTEGER NOT NULL)
    ''')

    connection.commit()
    print("Таблица создана!")

'''elif a == 2:  # Добавление данных в таблицу
    username = input("Введите имя: ")
    age = int(input("Введите возраст: "))

    cursor.execute("INSERT INTO Users (username, age) VALUES (?, ?)", (username, age))

    connection.commit()
    print("Добавлено!")

elif a == 3:  # Обновление данных по id
    username = int(input("Введите имя пользователя для редактирования данных: "))
    new_username = input(f"Введите новое имя для {username}: ")
    new_age = int(input(f"Введите новый возраст для {username}: "))

    cursor.execute("UPDATE Users SET age = ?, username = ? WHERE username = ?", (new_age, new_username, username))

    #cursor.execute("INSERT INTO Users (username, age) VALUES (?, ?)", (username, age))

    connection.commit()'''

connection.close()
