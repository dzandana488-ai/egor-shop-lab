import sqlite3
from pathlib import Path

db_path = Path(__file__).with_name("shop.db")

connection = sqlite3.connect(db_path)

connection.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY,
        author TEXT NOT NULL,
        text TEXT NOT NULL
    )
""")

connection.commit()
connection.close()

print("Таблица отзывов готова")