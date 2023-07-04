import socket, pickle

# Servidor responsável por ativar irrigadores de cada parque

# Para comunicação entre diferentes computadores basta colocar o IPV4 do computador servidor
# tanto no server.py quanto no client.py
server_ip = '127.0.0.1'
server_port = 12345

class SensorReport:
    def __init__(self, umidadedePercentage, previsaoChuva):
        self.umidadePercentage = umidadedePercentage
        self.previsaoChuva = previsaoChuva

def irrigacaoValidation(reportData):
    #Logica para definir irrigação ou não
    return "False"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Abre o socket o servidor central
    server_socket.bind((server_ip, server_port))

    # Abre um listen para a quantidade de sensores ativos de cada parque
    server_socket.listen(4)
    print("Servidor pronto para receber conexão")

    # while True:
    client_socket, client_address = server_socket.accept()
    print("Conexão estabelecida com:", client_address)

    report = client_socket.recv(4096)
    reportData = pickle.loads(report)

    print(
        "\n" +
        "------ Sensor Parque " + reportData.sensorId + " ------\n" +
        "\\\\\\\\\\\\\\\\\\ REPORT \\\\\\\\\\\\\\\\\\\n\n" +
        "# Porcentagem de chuva: " + reportData.umidadePercentage + "%\n" + 
        "# Previsão de chuva: " + reportData.previsaoChuva + "\n\n" +
        "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n" +
        "\n"
    )

    ativarIrrigacao = irrigacaoValidation(reportData)
    client_socket.send(ativarIrrigacao.encode())

    client_socket.close()
    print("Conexão encerrada com: ", client_address)

finally:

    server_socket.close()