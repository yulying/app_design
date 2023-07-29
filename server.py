import os
import sqlite3
import socket


# Connects user to server after getting "Pending connection" request

db_conn = sqlite3.connect("app_info.db")
cur = db_conn.cursor()


def server():
    # create an INET, STREAMing socket
    print("Creating socket...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to a public host, and a well-known port
    print("Binding socket...")
    server_socket.bind(("localhost", 8000))
    print("Done.")
    # become a server socket
    server_socket.listen()
    print("Waiting for connection...")

    # accept connections from outside
    (client_socket, address) = server_socket.accept()
    print(f"Accepted Connection at {address}")

    while True:
        data = client_socket.recv(8096)

        if not data:
            break

        print(data.decode())

        try:
            eval(data.decode())

            db_conn.commit()

            getAllUsers()
            getAllUserPreferences()

            client_socket.send("Database updated.".encode())
        except Exception as e:
            print(e)
            client_socket.send(str(e).encode())

    client_socket.close()


# <html><body><h1>Hello, world!</h1></body></html>"""
# client_socket.send(msg)
# client_socket.close()
# now do something with the clientsocket
# in this case, we'll pretend this is a threaded server


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


def test():
    test = 1


def main():
    deleteUser("1000001")
    db_conn.commit()

    getAllUsers()
    getAllUserPreferences()


server()

cur.close()
db_conn.close()
