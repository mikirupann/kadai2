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
    sql = f"INSERT INTO users (name, age) VALUES ('{name}', {age})"
    cur.execute(sql)
    conn.commit()
    conn.close


def main():
    # init_db()
    name = 'Bob'
    age = 15
    register_user(name, age)


if __name__ == '__main__':
    main()
