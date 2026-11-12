import sqlite3
from pathlib import Path

from flask import Flask, render_template, request, redirect


app = Flask(__name__)

db_path = Path(__file__).with_name("shop.db")


@app.route("/")
def home():
    search = request.args.get("q", "")

    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row

    if search:
        # Намеренно уязвимый запрос для лабораторной
        query = (
            "SELECT id, name, price FROM products WHERE name = '"
            + search
            + "'"
        )

        print("SQL-запрос:", query)
        products = connection.execute(query).fetchall()
    else:
        products = connection.execute(
            "SELECT id, name, price FROM products"
        ).fetchall()

    reviews = connection.execute(
        "SELECT id, author, text FROM reviews ORDER BY id DESC"
    ).fetchall()

    connection.close()

    return render_template(
        "index.html",
        products=products,
        reviews=reviews
    )


@app.route("/reviews", methods=["POST"])
def add_review():
    author = request.form.get("author", "").strip()
    text = request.form.get("text", "").strip()

    if author and text:
        connection = sqlite3.connect(db_path)

        connection.execute(
            "INSERT INTO reviews (author, text) VALUES (?, ?)",
            (author, text)
        )

        connection.commit()
        connection.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)