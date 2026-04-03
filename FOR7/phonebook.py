import psycopg2
import csv

DB_CONFIG={
    "dbname": "phonebooks", 
    "user": "postgres",       
    "password": "13PostgreSQL631", 
    "host": "localhost",
    "port": "5432"
}

def icsv(file_path):
    try:
        conn=psycopg2.connect(**DB_CONFIG)
        cur=conn.cursor()
        with open("contacts.csv", mode='r', encoding='utf-8') as f:
            reader=csv.reader(f)
            for row in reader:
                name=row[0]
                phone=row[1]
                cur.execute(
                    "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                    (name, phone)
                )
                
        conn.commit()
        print(f"csv is finished")

    except Exception as e:
        print(f"Error: {e}")
        if 'conn' in locals():
            conn.rollback() 
    finally:
        if 'cur' in locals(): cur.close()
        if 'conn' in locals(): conn.close()

conn=psycopg2.connect(**DB_CONFIG)
cur=conn.cursor()
cur.execute("SELECT * FROM contacts")
r=cur.fetchall()
conn.commit()
for row in r:
    print(row)
cur.close()
conn.close()

def add_contact(name, phone):
    try:
        conn=psycopg2.connect(**DB_CONFIG)
        cur=conn.cursor()
        cur.execute("INSERT INTO contacts (name, phone) VALUES (%s, %s)", (name, phone))
        conn.commit()
        print(f"Контакт {name} добавлен!")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

def change(phone, name,  id):
    try:
        conn=psycopg2.connect(**DB_CONFIG)
        cur=conn.cursor()
        cur.execute("UPDATE contacts SET phone = %s, name = %s WHERE id = %s", (phone, name,  id))
        conn.commit()
        print(f"Контакт {name} обновлен!")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")
    
def delete(id):
    try:
        conn=psycopg2.connect(**DB_CONFIG)
        cur=conn.cursor()
        cur.execute("DELETE FROM contacts WHERE id = %s", (id,))
        conn.commit()
        print(f"Deleting complete")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error: {e}")

def find(srch_p):
    try:
        conn=psycopg2.connect(**DB_CONFIG)
        cur=conn.cursor()
        cur.execute("SELECT * FROM contacts WHERE phone ILIKE %s", (srch_p,))
        res=cur.fetchall()
        conn.commit()
        for row in res:
            print(row)
    except Exception as e:
        print(f"Error: {e}")
a=""
while a!="stop":

    a=input()

    if(a=="add"):
        try:
            print("--- Проверка связи с базой ---")
            name=input("Введите имя для теста: ")
            phone=input("Введите телефон: ")
            add_contact(name, phone)
        except Exception as e:
            print(e)

    if(a=="delete"):
        try:
            print("give id: ")
            id=int(input())
            delete(id)
        except Exception as e:
            print(e)
            
    if (a=="change"):
        try:
            print ("write down phone, name, id")
            phone=input("phone ")
            name=input("name ")
            id=int(input("id "))
            change(phone, name, id)
        except Exception as e:
            print(e)
    
    if (a=="table"):
        conn=psycopg2.connect(**DB_CONFIG)
        cur=conn.cursor()
        cur.execute("SELECT * FROM contacts")
        r=cur.fetchall()
        conn.commit()
        for row in r:
            print(row)
        cur.close()
        conn.close()
    
    if (a=="csv"):
        icsv("contacts.csv")

    if (a=="find"):
        srch_p=input("enter number with % in start or end")
        print(find(srch_p))
