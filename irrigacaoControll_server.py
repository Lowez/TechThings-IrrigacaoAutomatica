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

def irrigar(reportData):
    #Logica para definir irrigação ou não

    # Só deve haver irrigação se a porcentagem de umidade for menor que 50% e não haver previsão de chuva
    # Caso a umidade seja menor que 50% porém maior ou igual que 10% e existir previsão de chuva, não deve haver irrigação
    if (int(reportData.umidadePercentage) >= 50):
        return "False"
    elif ((int(reportData.umidadePercentage) >= 10 and int(reportData.umidadePercentage) < 50) and reportData.previsaoChuva == "Sim"):
        return "False"
    
    return "True"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Abre o socket o servidor central
    server_socket.bind((server_ip, server_port))

    # Abre um listen para a quantidade de sensores ativos de cada parque
    server_socket.listen(4)
    print("Servidor pronto para receber conexão")

    while True:
        client_socket, client_address = server_socket.accept()
        print("Conexão estabelecida com:", client_address)

        # Recebe os dados do sensor e decodifica para um objeto SensorReport
        report = client_socket.recv(4096)
        reportData = pickle.loads(report)

        # Imprime os dados recebidos
        print(
            "\n" +
            "------ Sensor Parque " + reportData.sensorId + " ------\n" +
            "\\\\\\\\\\\\\\\\\\ REPORT \\\\\\\\\\\\\\\\\\\n\n" +
            "# Porcentagem de chuva: " + reportData.umidadePercentage + "%\n" + 
            "# Previsão de chuva: " + reportData.previsaoChuva + "\n\n" +
            "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n" +
            "\n"
        )
        
        # Valida os dados recebidos para saber se deve enviar sinal para irrigação do parque
        ativarIrrigacao = irrigar(reportData)
        client_socket.send(ativarIrrigacao.encode())

        client_socket.close()
        print("Conexão encerrada com: ", client_address)

finally:

    server_socket.close()