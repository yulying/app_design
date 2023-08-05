import socket


def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 8000))

    while True:
        request = input(str("Request: "))

        if request == "":
            break
        client_socket.send(request.encode())
        success_msg = client_socket.recv(8096).decode()
        print(success_msg)

    client_socket.close()


# Called when a new thread is created
client()
