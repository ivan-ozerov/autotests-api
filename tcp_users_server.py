import socket


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    server_socket.listen(10)

    data = []

    while True:
        client_socket, client_address = server_socket.accept()

        print(f'Пользователь с адресом: {client_address} подключился к серверу')

        client_message = client_socket.recv(1024).decode()
        data.append(client_message)

        formatted_message = f'Пользователь с адресом: {client_address} отправил сообщение: {client_message}'
        print(formatted_message)

        response = f"{'\n'.join(data)}"

        client_socket.send(response.encode())

        client_socket.close()


if __name__ == '__main__':
    server()