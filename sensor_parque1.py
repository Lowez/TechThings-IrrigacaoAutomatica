import socket, json, pickle

# Envia as informações sobre umidade dos solos e ocorrência futura de chuva nos parques

server_ip = '127.0.0.1'
server_port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((server_ip, server_port))

    data = {
        "porcentagem": 50,
        "chuvaProxima": True
    }
    json_string = json.dumps(data)

    # message = "Porcentagem de umidade do solo: " + input("Porcentagem de umidade do solo: ")
    # message += " "
    # message += " Chuva próxima: " + input("Chuva próxima: ")
    # message += " Parque: 1"
    json_bytes= json_string.encode()
    client_socket.sendall(json_bytes)

    modified_message = client_socket.recv(1024).decode("utf-8")
    print("Relatório: ", modified_message)

except ConnectionRefusedError:
    print("Não foi possível conectar ao servidor")

finally:

    client_socket.close()