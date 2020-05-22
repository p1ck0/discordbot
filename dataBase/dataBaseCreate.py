import sqlite3

conn = sqlite3.connect("dataBase.db")
cursor = conn.cursor()

# Создание таблицы
cursor.execute("""CREATE TABLE Message
                  (server text, chat text, message text)
               """)
conn.commit()

with open("../msg.txt", "r", encoding="UTF-8") as file:
    file = file.read().split("\n")
for i in range(len(file)):
    if file[i] != "":
        Message = [('', '', file[i])]
        cursor.executemany("INSERT INTO Message VALUES (?,?,?)", Message)

conn.commit()






# print("Here's a listing of all the records in the table:")
# for row in cursor.execute("SELECT rowid, * FROM albums ORDER BY artist"):
#     print(row)
#
# print("Results from a LIKE query:")
# sql = "SELECT * FROM albums WHERE title LIKE 'The%'"
# cursor.execute(sql)
#
# print(cursor.fetchall())
