import os
import json
import logging
import threading
import time
import sqlite3

from flask import Flask, render_template, request


app = Flask(__name__)

## Using FLASK_ENV enviroment variable  setting the debug mode 
app.config['DEBUG'] = os.environ.get('FLASK_ENV') == 'development'

## Using TODO_DB environment variable setting the path to the SQLite database file 
app.config['TODO_DB'] = os.environ.get('TODO_DB', 'todo.db')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


## Creting todo table
def init_db():
    with sqlite3.connect(app.config['TODO_DB']) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS todo
                     (content text)''')
        conn.commit()


##Periodically saving the todo items 
def periodically_save_todo_items():
    while True:
        time.sleep(10)
        with sqlite3.connect(app.config['TODO_DB']) as conn:
            c = conn.cursor()
            c.execute('DELETE FROM todo')
            c.executemany('INSERT INTO todo VALUES (?)', [(item,) for item in get_todo_items()])
            conn.commit()


## fun to add todo items
def add_todo_item(item):
    with sqlite3.connect(app.config['TODO_DB']) as conn:
        c = conn.cursor()
        c.execute('INSERT INTO todo VALUES (?)', (item,))
        conn.commit()


##fun fetch the todo items 
def get_todo_items():
    with sqlite3.connect(app.config['TODO_DB']) as conn:
        c = conn.cursor()
        c.execute('SELECT content FROM todo')
        todo_items = [item[0] for item in c.fetchall()]
    return todo_items


## Initialize the todo table
init_db()

## Starting the thread that periodically saves the todo items to the database
saving_thread = threading.Thread(target=periodically_save_todo_items)
saving_thread.start()


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        content = request.form["content"]
        add_todo_item(content)

    todo_items = get_todo_items()

    return render_template("index.html", todo_items=todo_items)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
