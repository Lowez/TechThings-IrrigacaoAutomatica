import socket, pickle

class SensorReport:
    def __init__(self):
        self.sensorId = "3"
        self.umidadePercentage = input("Porcentagem de umidade detectada: ")
        self.previsaoChuva = input("Previsão de chuva para próximo dia: ")

def main():
    import socket, pickle

    # Envia as informações sobre umidade dos solos e ocorrência futura de chuva nos parques

    server_ip = '127.0.0.1'
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_ip, server_port))

        # Cria o objeto de report do sensor
        report = SensorReport()

        # Codifica para o envio do objeto para o servidor
        reportString = pickle.dumps(report)
        client_socket.send(reportString)

        # Imprime os dados enviados
        print(
            "\n" +
            "------ Sensor Parque " + report.sensorId + " ------\n" +
            "\\\\\\\\\\\\\\\\\\ REPORT \\\\\\\\\\\\\\\\\\\n\n" +
            "# Porcentagem de chuva: " + report.umidadePercentage + "%\n" + 
            "# Previsão de chuva: " + report.previsaoChuva + "\n\n" +
            "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n" +
            "\n"
        )

        # Recebe o retorno do servidor para irrigar ou não o parque
        report = client_socket.recv(4096).decode()

        if (report == "True"):
            print("\nIrrigando Parque...\n")
        else:
            print("\nNão será feita irrigação\n")

    except ConnectionRefusedError:
        print("Não foi possível conectar ao servidor")

    finally:

        client_socket.close()

    return

if __name__ == "__main__":
    main()