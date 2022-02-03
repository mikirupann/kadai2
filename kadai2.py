import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


# テーブルをつくる
def init_db():
    dsn = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    with open('sql/schema.sql', encoding="utf-8") as f:
        sql = f.read()
        cur.execute(sql)
    conn.commit()
    conn.close


# カラム追加
def register_user(name, age):
    dsn = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    sql = f"INSERT INTO users (name, age) VALUES (%(name)s, %(age)s)"
    cur.execute(sql, {'name': name, 'age': age})
    conn.commit()
    conn.close


# テーブルにある一つのものを抽出
def one_user(name):
    dsn = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    sql = "SELECT * FROM users;"
    cur.execute(sql)
    user = cur.fetchone()
    conn.commit()
    conn.close
    return (user)


# テーブルにある全てのものを抽出
def all_users():
    dsn = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    sql = "SELECT * FROM users;"
    cur.execute(sql)
    users = cur.fetchall()
    conn.commit()
    conn.close
    return (users)


# 検索
def ken_saku(name):
    dsn = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    with open('sql/kensaku.sql', encoding="utf-8") as f:
        sql = f.read()
        cur.execute(sql, {'name': name})
    conn.commit()
    conn.close


# 削除
def de_lete(name):
    dsn = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    with open('sql/delete.sql', encoding="utf-8") as f:
        sql = f.read()
        cur.execute(sql, {'name': name})
    conn.commit()
    conn.close


# 編集
def kai(name, name_kai, age_kai):
    dsn = os.environ.get('DATABASE_URL')
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    with open('sql/kai.sql', encoding="utf-8") as f:
        sql = f.read()
        cur.execute(sql, {'name': name, 'name_kai': name_kai, 'age_kai': age_kai})
    conn.commit()
    conn.close


def main():
    with open('open.txt', encoding="utf-8") as f:
        sql = f.read()
        print(sql)
    init_db()
    # users = all_users()
    while True:
        command = input('Your command > ').upper()
        if command == 'S':
            all = all_users()
            for i in all:
                print(f"Name: {i[0]} Age: {i[1]}")
        elif command == 'A':
            name = input('New user name > ')
            age = input('New user age > ')
            print(f"Add new user: {name}")
            try:
                register_user(name, age)
            except psycopg2.errors.UniqueViolation:
                print(f"Duplicated user name {name}")
            else:
                pass
            finally:
                continue
        elif command == 'Q':
            print(f"Bye!")
            break
        elif command == 'F':
            name = input('User name > ')
            ken = ken_saku(name)
            if len(ken) == 0:
                print(f"Sorry, {name} is not found")
            else:
                print(f"Name: {ken[0][0]} Age: {ken[0][1]}")
        elif command == 'D':
            name = input('User name > ')
            de_lete(name)
            print(f"User {name} is deleted")
        elif command == 'E':
            name = input('User name > ')
            one_user(name)
            if not one_user(name):
                print(f"Sorry, {name} is not found")
            else:
                name_kai = input(f"New user name({name}) > ")
                age_kai = input(f"New user age({one_user(name)[1]}) > ")
                kai(name, name_kai, age_kai)
                print(f"Update user: {name_kai}")
        else:
            print(f"x: command not found")


if __name__ == '__main__':
    main()
