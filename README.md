# TechThings-IrrigacaoAutomatica

## Como rodar?

### Na mesma máquina
- Inicialmente, configure devidamente o ip do servidor que deseja enviar informações dentro de todos os arquivos de `sensor_parque`;
- Após isso, rode o arquivo irrigacaoControll_server.py com o comando `py irrigacaoControll_server.py`, para inicializar o servidor;
- Execute o comando `py centralParques_server.py` em outro terminal para inicializar o gerenciador de sensores. Informe devidamente o id do sensor que irá enviar informações para o servidor;
- Assim que um id existente for informado, informe a porcentagem de umidade do solo e se existe previsão de chuva para o próximo dia;
- O servidor deve reconhecer os dados e retornar uma resposta se irá ser feita a irrigação do parque, junto com um relatório dos dados enviados.

### Com máquinas diferentes
- Inicialmente, configure devidamente o ip do servidor que deseja enviar informações dentro de todos os arquivos de `sensor_parque`;
- Após isso, rode o arquivo irrigacaoControll_server.py com o comando `py irrigacaoControll_server.py`, para inicializar o servidor;
- Execute individualmente os comandos `py sensor_parqueID.py` onde *ID* é o id do parque do arquivo referido;
- Assim que um id existente for informado, informe a porcentagem de umidade do solo e se existe previsão de chuva para o próximo dia;
- O servidor deve reconhecer os dados e retornar uma resposta se irá ser feita a irrigação do parque, junto com um relatório dos dados enviados.