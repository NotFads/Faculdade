programaAtivo = True
matriz = ['', 0, 0, 0, 0, 0]
while programaAtivo:
    opc = int(input(f'\n----------------Menu----------------\n\t[ 1 ] Fornecer Registro de Consumo.\n\t[ 2 ] Apagar Registro de Consumo.\n\t[ 3 ] Ver Registro de Consumo.\n\t[ 0 ] Sair.\n------------------------------------\n'))
    match opc:
        case 1:
            print(f'\nResponda o questionário a seguir: ')
            data = input(f'\tQual é a data? ')
            agua = float(input(f'\tQuantos litros de água você consumiu hoje? (Aprox. em litros) '))
            eEle = float(input(f'\tQuantos kWh de energia elétrica você consumiu hoje? '))
            nRec = float(input(f'\tQuantos kg de resíduos não recicláveis você gerou hoje? '))
            pRec = float(input(f'\tQual a porcentagem de resíduos reciclados no total (em %)? '))
            if pRec < 0 or pRec > 100:
                print('Entre com um valor de 0 a 100 (em %)!')
            tran = int(input(f'\tQual o meio de transporte você usou hoje? \n\t\t1. Transporte público (ônibus, metrô, trem)\n\t\t2. Bicicleta\n\t\t3. Caminhada\n\t\t4. Carro (combustível fóssil)\n\t\t5. Carro Elétrico\n\t\t6. Carona Compartilhada\n'))
            if tran < 1 or tran > 6:
                print('Entre com uma opção de 1 a 6! ')
        case 2:
            pass
        case 3:
            pass
        case 0:                
            print('Fechando programa...')
            programaAtivo = False