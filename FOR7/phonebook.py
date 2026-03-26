import psycopg2
import csv

# ТВОИ НАСТРОЙКИ (проверь имя базы и пароль!)
DB_CONFIG = {
    "dbname": "phonebooks", # то имя, которое ты дал в pgAdmin
    "user": "postgres",       # стандартный юзер
    "password": "13PostgreSQL631", # пароль, который вводил при установке Postgres
    "host": "localhost",
    "port": "5432"
}

def add_contact(name, phone):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print(f"Контакт {name} добавлен!")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Ошибка: {e}")

# Простой запуск для теста
if __name__ == "__main__":
    print("--- Проверка связи с базой ---")
    name = input("Введите имя для теста: ")
    phone = input("Введите телефон: ")
    add_contact(name, phone)