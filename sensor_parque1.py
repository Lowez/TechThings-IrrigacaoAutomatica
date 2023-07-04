import socket, json, pickle

# Envia as informações sobre umidade dos solos e ocorrência futura de chuva nos parques

server_ip = '127.0.0.1'
server_port = 12345

class SensorReport:
    def __init__(self):
        self.sensorId = "1"
        self.umidadePercentage = input("Porcentagem de umidade detectada: ")
        self.previsaoChuva = input("Previsão de chuva para próximo dia: ")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((server_ip, server_port))

    report = SensorReport()
    reportString = pickle.dumps(report)
    client_socket.send(reportString)

    report = client_socket.recv(4096).decode()
    # reportResult = pickle.loads(report)
    if (report):
        print("\nIrrigando Parque...\n")
    else:
        print("\nNão será feita irrigação\n")

except ConnectionRefusedError:
    print("Não foi possível conectar ao servidor")

finally:

    client_socket.close()