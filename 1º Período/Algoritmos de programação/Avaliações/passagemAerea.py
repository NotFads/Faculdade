programaAtivo = 1
voos = dict()
passageiros = dict()

while programaAtivo == 1:
    menu = int(input(f'-------Menu-------\n1.Cadastrar Voo.\n2. Consultar um Voo.\n3. Informar o Voo com Menor Escala.\n4. Listar Passageiros de um Voo.\n5. Venda de Passagem.\n6. Cancelamento de Passagem.\n0. Encerrar programa.'))
    #Cadastro de Voo
    disp = []
    comp = []
    if menu == 1:
        nVoo = int(input('Entre com o número do voo: '))
        cidadeO = input('Entre com a cidade de origem: ')
        cidadeD = input('Entre com a cidade de destino: ')
        nEscala = int(input('Entre com o número de escalas: '))
        preco = float(input('Entre com o preço da passagem: '))
        lugares = int(input('Entre com o número de lugares: '))
        disp.append(lugares)
        voos[nVoo] = [cidadeO,cidadeD,nEscala,preco,lugares]
    elif menu == 2:
        consulta = int(input(f'Tipos de Consulta\n1. Código do voo.\n2. Cidade Origem.\n3. Cidade Destino.'))
        if consulta == 1:
            codigo = int(input('Entre o código que você deseja buscar: '))
            for codigo in voos.keys():
                print(voos)
        elif consulta == 2:
            cidadeOB = input('Entre a cidade de origem que você deseja buscar: ')
            for origem in voos.values():
                if voos[0] == cidadeOB:
                    print(voos)

        elif consulta == 3:
            cidadeDB = input('Entre com a cidade de destino que você deseja buscar: ')
            for destino in voos.values():
                encontrado = 0
                if voos[1] == cidadeDB:
                    print(voos)
                    encontrado = 1
                if encontrado == 0:
                    print('Voo não encontrado.')
