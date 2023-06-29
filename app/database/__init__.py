from flask import g     # g is a global object that Flask provides to share data between functions
import sqlite3

DATABASE_URl = "main.db"

def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE_URl)
    return db

