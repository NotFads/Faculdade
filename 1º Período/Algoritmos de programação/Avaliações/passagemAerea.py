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
            for voo in voos.keys():
                if codigo == voos.keys():
                    print(voos.values())
        elif consulta == 2:
            cidadeOB = input('Entre a cidade de origem que você deseja buscar: ')
            encontrado = 0
            for voo in voos.values():
                if voo[0] == cidadeOB:
                    print(voo)
                    encontrado = 1
                if encontrado == 0:
                    print('Voo não encontrado.')

        elif consulta == 3:
            cidadeDB = input('Entre com a cidade de destino que você deseja buscar: ')
            encontrado = 0
            for voo in voos.values():
                if voo[1] == cidadeDB:
                    print(voo)
                    encontrado = 1
                if encontrado == 0:
                    print('Voo não encontrado.')
    elif menu == 3:
        menorEscala = 999999
        codigo = -1
        for voo in voos.values():
            if voo[2] < menorEscala:
                menorEscala = voo[2]
                codigo = voos.keys()
        for voo in voos.values():
            if voos.keys() == codigo:
                print(voo)