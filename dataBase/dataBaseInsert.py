import sqlite3

def Insert(Chat, Message, ServerID):
    conn = sqlite3.connect(f"dataBase/{ServerID}.db")
    cursor = conn.cursor()
    Server = [(str(Chat), str(Message))]
    cursor.executemany(f"INSERT INTO Server VALUES (?,?)", Server)
    conn.commit()