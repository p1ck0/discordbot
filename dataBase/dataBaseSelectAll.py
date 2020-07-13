import sqlite3


def dataBaseSelectAll(ServerID):
    message = list()
    conn = sqlite3.connect(f"database/{ServerID}.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Server")
    for i in cursor.fetchall():
        message.append(i[1])
    return message
