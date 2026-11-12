import sqlite3
from pathlib import Path

db_path = Path(__file__).with_name("shop.db")

connection = sqlite3.connect(db_path)

connection.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price INTEGER NOT NULL
    )
""")

connection.executemany("""
    INSERT INTO products (name, price)
    VALUES (?, ?)
""", [
    ("Кофе", 250),
    ("Чай", 150),
    ("Круассан", 200),
    ("Какао", 220)
])

connection.commit()
connection.close()