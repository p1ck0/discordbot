import sqlite3

conn = sqlite3.connect("dataBase.db")
cursor = conn.cursor()

with open("../msg.txt", "r", encoding="UTF-8") as file:
    file = file.read().split("\n")
for i in range(len(file)):
    if file[i] != "":
        Message = [('', '', file[i])]
        cursor.executemany("INSERT INTO Message VALUES (?,?,?)", Message)

    message_list = set()
    #
    # old_msgs = open('msg.txt', 'r', encoding='UTF=8')
    # for msg in old_msgs:
    #     message_list.add(msg)


conn.commit()
