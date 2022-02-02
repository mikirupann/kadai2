import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def init_db():
    dsn = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    with open('schema.sql', encoding="utf-8") as f:
        sql = f.read()
        cur.execute(sql)
    conn.commit()
    conn.close


def register_user(name, age):
    dsn = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    sql = f"INSERT INTO users (name, age) VALUES (%(name)s, %(age)s)"
    cur.execute(sql, {'name': name, 'age': age})
    conn.commit()
    conn.close


def all_users():
    dsn = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    sql = "SELECT * FROM users;"
    cur.execute(sql)
    users = cur.fetchall()
    conn.commit()
    conn.close
    return users


def ken_saku():
    dsn = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    sql = "SELECT * FROM users WHERE age;"
    cur.execute(sql)
    users = cur.fetchall()
    conn.commit()
    conn.close
    print(users)

def main():
    init_db()
    users = all_users()
    while True:
        command = input('Your command > ')
        if command == 'S':
            for users in all_users():
                print(f"Name: {users[0]} Age: {users[1]}")
        elif command == 'A':
            name = input('New user name > ')
            age = input('New user age > ')
            print(f"Add new user: {name}")
            try:
                register_user(name, age)
            except psycopg2.errors.UniqueViolation:
                print(f"Duplicated user name Bob")
            else:
                pass
            finally:
                continue
        elif command == 'Q':
            print(f"Bye!")
            break
        elif command == 'F':
            name = input('User name > ')
            print()
        else:
            print(f"x: command not found")


if __name__ == '__main__':
    main()
