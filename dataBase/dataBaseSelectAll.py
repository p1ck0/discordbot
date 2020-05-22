import sqlite3


def dataBaseSelectAll(path):
    conn = sqlite3.connect(path)
    cursor = conn.cursor()
    sql = "SELECT * FROM Message"
    cursor.execute(sql)
    return cursor.fetchall()
