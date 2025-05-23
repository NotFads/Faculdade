programaAtivo = 1
voos = dict()
passageiros = dict()
disponiveis = []
compra = []

while programaAtivo == 1:
    menu = int(input(f'-------Menu-------\n1.Cadastrar Voo.\n2. Consultar um Voo.\n3. Informar o Voo com Menor Escala.\n4. Listar Passageiros de um Voo.\n5. Venda de Passagem.\n6. Cancelamento de Passagem.\n0. Encerrar programa.'))
    menorE = 999
    if menu == 1:
        nVoo = int(input('Entre com o número do voo: '))
        cidadeO = input('Entre com a cidade de origem: ')
        cidadeD = input('Entre com a cidade de destino: ')
        nEscala = int(input('Entre com o número de escalas: '))
        preco = float(input('Entre com o preço da passagem: '))
        lugares = int(input('Entre com o número de lugares: '))
        voos[nVoo] = [cidadeO,cidadeD,nEscala,preco,lugares]
        if lugares > 0:
            disponiveis.append(voos[nVoo])
    elif menu == 2:
        consulta = int(input(f'Tipos de Consulta\n1. Código do voo.\n2. Cidade Origem.\n3. Cidade Destino.'))
        if consulta == 1:
            codigo = int(input('Entre o código que você deseja buscar: '))
            if codigo in voos.keys():
                print(voos[codigo])
            else:
                print('Voo não encontrado.')
        elif consulta == 2:
            cidadeOB = input('Entre a cidade de origem que você deseja buscar: ')
            encontrado = 0
            for voo in voos.values():
                if voo[0].lower() == cidadeOB.lower():
                    print(voo)
                    encontrado = 1
            if encontrado == 0:
                print('Voo não encontrado.')
        elif consulta == 3:
            cidadeDB = input('Entre com a cidade de destino que você deseja buscar: ')
            encontrado = 0
            for voo in voos.values():
                if voo[1].lower() == cidadeDB.lower():
                    print(voo)
                    encontrado = 1
            if encontrado == 0:
                print('Voo não encontrado.')
    elif menu == 3:
        #Achar um jeito de printar só uma vez
        cidadeOB = input('Entre a cidade de origem que você deseja: ')
        cidadeDB = input('Entre a cidade de destino que você deseja: ')
        for voo in voos.values():
            if voo[0].lower() == cidadeOB.lower() and voo[1].lower() == cidadeDB.lower():
                if voo[2] < menorE:
                    menorE = voo[2]
                    print(voo)
    #elif menu == 4:
    elif menu == 5:
        for i in range(len(disponiveis)):
            print(f'Voo {i} : {disponiveis[i]}')
        disponiveisB = int(input('Entre o voo que você está interessado: '))
        cpf = input('Entre com o seu CPF: ')
        nome = input('Entre com o seu nome: ')
        tel = int(input('Entre com o seu número de telefone: '))
        passagem = int(input('Entre com o número de passagens que você deseja comprar: '))
        for codigo, dados in voos.items():
            if dados == disponiveis[disponiveisB]:
                voos[codigo][4] -= passagem
        passageiros[cpf] = [nome,tel]
        compra.append(passageiros[cpf])
        print(passageiros)
    elif menu == 6:
        cpfB = input('Entre com o CPF do comprador: ')
        for codigo, dados in voos.items():
            if dados == compra[cpfB]:
                del passageiros[cpfB]
    elif menu == 0:
        break


