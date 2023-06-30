import socket

server_ip = '192.168.1.106'
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((server_ip, server_port))

    message = input("Digite um string: ")
    client_socket.send(message.encode())

    modified_message = client_socket.recv(1024).decode()
    print("String modificada: ", modified_message)

except ConnectionRefusedError:
    print("Não foi possível conectar ao servidor")

finally:

    client_socket.close()