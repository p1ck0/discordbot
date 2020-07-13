import sqlite3

def createServer(ServerID):
    conn = sqlite3.connect(f"dataBase/{ServerID}.db")
    cursor = conn.cursor()

    # Создание таблицы
    cursor.execute("""CREATE TABLE Server
                    (chat text, message text)
                """)
    cursor.execute("""CREATE TABLE Settings
                    (chat text, message text)
                """)
    conn.commit()
