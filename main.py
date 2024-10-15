import sqlite3

while True:
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    a = int(input("1.Создать таблицу"
                  "\n2.Добавить данные"
                  "\n3.Обновить данные"
                  "\n4.Запрос на поиск"
                  "\n5.Выйти"
                  "\nВыберите действие: "))
    if a == 1: # создание таблицы
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        age INTEGER NOT NULL)
        ''')

        connection.commit()
        print("Таблица создана!")

    elif a == 2:  # Добавление данных в таблицу
        username = input("Введите имя: ")
        age = int(input("Введите возраст: "))

        cursor.execute("INSERT INTO Users (username, age) VALUES (?, ?)", (username, age))

        connection.commit()
        print("Добавлено!")

    elif a == 3:  # Обновление данных по имени
        username = input("Введите имя пользователя для редактирования данных: ")
        new_age = int(input(f"Введите новый возраст для {username}: "))

        cursor.execute("UPDATE Users SET age = ? WHERE username = ?", (new_age, username))

        connection.commit()

        if cursor.rowcount == 0:
            print(f"Пользователь с именем {username} не найден.")
        else:
            print(f"Возраст пользователя {username} обновлен на {new_age}.")

    elif a == 4:  # Запрос
        def get_record_id(table_name, field_name, field_value):
            query = f"SELECT id FROM {table_name} WHERE {field_name} = ?"
            cursor.execute(query, (field_value,))
            results = cursor.fetchall()

            # Если запись найдена, возвращаем её идентификатор, иначе None
            if results:
                return [row[0] for row in results]
            else:
                return None


        table_name = 'Users'
        field_name = 'username'
        field_value = 'Андрей'
        get_record_id(table_name, field_name, field_value)

    elif a == 5:
        connection.close()
        break  # Выход
        
    else: print("Попробуйте снова!")

    connection.close()
    print("")
