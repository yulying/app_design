import os
import sqlite3
import socket


# Connects user to server after getting "Pending connection" request
db_conn = sqlite3.connect("app_design/app_info.db")
cur = db_conn.cursor()


# User ID is UNIQUE
def addNewUser(user_id, username, password, email):
    cur.execute(
        "INSERT INTO users (user_id, username, password, email) VALUES (?,?,?,?)",
        (user_id, username, password, email),
    )
    cur.execute(
        "INSERT INTO preferences(user_id, song, album, artist) VALUES (?,?,?,?)",
        (user_id, None, None, None),
    )


def deleteUser(user_id):
    cur.execute("DELETE FROM users WHERE user_id=(?)", (user_id,))


def editUser(username, password, email):
    cur.execute(
        "UPDATE users SET password=%s, email=%s WHERE username=%s",
        (password, email, username),
    )


def editUserPreferences(username, song, album, artist):
    cur.execute(
        "UPDATE users SET song=%s, album=%s, artist=%s WHERE username=%s",
        (song, album, artist, username),
    )


def getAllUsers():
    cur.execute("SELECT * FROM USERS")

    for row in cur:
        print(row)


def getAllUserPreferences():
    cur.execute("SELECT * FROM PREFERENCES")

    for row in cur:
        print(row)


def main():
    deleteUser("1000001")
    db_conn.commit()

    getAllUsers()
    getAllUserPreferences()


main()

cur.close()
db_conn.close()
