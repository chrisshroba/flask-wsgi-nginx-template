import sqlite3
from flask import Flask
# from flask import request
from flask import g

app = Flask(__name__)

DATABASE_PATH = 'data.db'


def connect_db():
    """
    Create and return a connection to the database here
    :return: db
    """
    g.db = sqlite3.connect(DATABASE_PATH)
    g.cursor = g.db.cursor()


@app.before_request
def before_request():
    connect_db()


@app.teardown_request
def teardown_request(_):
    """
    :param _: any exception that has occurred during execution
    """
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route('/')
def root():
    return "Hello worldddd!"
