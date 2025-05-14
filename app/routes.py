from flask import render_template

from app import app  # Unused import


@app.route("/")
def index():
    return render_template("index.html", message="Hello World")


def unused_function():
    print("This is never used")  # Unused function
