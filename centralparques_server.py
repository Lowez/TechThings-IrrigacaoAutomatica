while True:

    sensorId = input("Digite o ID do sensor: ")

    if sensorId == "1":
        import sensor_parque1
        sensor_parque1.main()
    elif sensorId == "2":
        import sensor_parque2
        sensor_parque2.main()
    elif sensorId == "3":
        import sensor_parque3
        sensor_parque3.main()
    elif sensorId == "4":
        import sensor_parque4
        sensor_parque4.main()
    else:
        print("Nenhum sensor detectado")