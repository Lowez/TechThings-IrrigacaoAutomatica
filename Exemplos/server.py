import socket

server_ip = '192.168.1.240'
server_port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind((server_ip, server_port))

    server_socket.listen(1)
    print("Servidor pronto para receber conexão")

    while True:
        client_socket, client_address = server_socket.accept()
        print("Conexão estabelecida com:", client_address)

        umidade = client_socket.recv(1024).decode()
        print("Porcentagem de umidade: ", umidade)

        client_socket.send(umidade.encode())

        client_socket.close()
        print("Conexão encerrada com: ", client_address)

finally:

    server_socket.close()