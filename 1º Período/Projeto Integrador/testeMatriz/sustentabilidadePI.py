programaAtivo = True
i = 0
matriz = [['', 0, 0, 0, 0, 0]]
while programaAtivo:
    opc = int(input(f'\n----------------Menu----------------\n\t[ 1 ] Fornecer Registro de Consumo.\n\t[ 2 ] Apagar Registro de Consumo.\n\t[ 3 ] Ver Registro de Consumo.\n\t[ 0 ] Sair.\n------------------------------------\n'))
    match opc:
        case 1:
            print(f'\nResponda o questionário a seguir: ')
            matriz[i][0] = input(f'\tQual é a data? ')
            matriz[i][1] = float(input(f'\tQuantos litros de água você consumiu hoje? (Aprox. em litros) '))
            matriz[i][2] = float(input(f'\tQuantos kWh de energia elétrica você consumiu hoje? '))
            matriz[i][3] = float(input(f'\tQuantos kg de resíduos não recicláveis você gerou hoje? '))
            matriz[i][4] = float(input(f'\tQual a porcentagem de resíduos reciclados no total (em %)? '))
            if matriz[i][4] < 0 or matriz[i][5] > 100:
                print('Entre com um valor de 0 a 100 (em %)!')
            matriz[i][5] = int(input(f'\tQual o meio de transporte você usou hoje? \n\t\t1. Transporte público (ônibus, metrô, trem)\n\t\t2. Bicicleta\n\t\t3. Caminhada\n\t\t4. Carro (combustível fóssil)\n\t\t5. Carro Elétrico\n\t\t6. Carona Compartilhada\n'))
            if matriz[i][5] < 1 or matriz[i][5] > 6:
                print('Entre com uma opção de 1 a 6! ')
            i += 1
        case 2:
            pass
        case 3:
            pesq = int(input('Digite o usuário que você deseja pesquisar: '))
            if pesq < 0 or pesq > i:
                print('Digite um usuário válido!')
            else:
                for j in range(5):
                    print(matriz[pesq][j],end=" ")
        case 0:                
            print('Fechando programa...')
            programaAtivo = False