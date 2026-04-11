import sqlite3

def connect_db():
    conn = sqlite3.connect('budget_tracker.db')
    return conn

