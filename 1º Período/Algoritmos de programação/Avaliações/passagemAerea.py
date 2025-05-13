programaAtivo = 1
voos = dict()
passageiros = dict()
disp = []
comp = []

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
            disp.append(voos[nVoo])
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
        for i in range(len(disp)):
            print(disp[i])
        dispB = int(input('Entre o voo que você está interessado: '))
        cpf = input('Entre com o seu CPF: ')
        nome = input('Entre com o seu nome: ')
        tel = int(input('Entre com o seu número de telefone: '))
        passagem = int(input('Entre com o número de passagens que você deseja comprar: '))
        passageiros[cpf] = [nome,tel]
        print(passageiros)
        for voo in voos:
            if voo == disp[dispB]:
                voo[4] -= passagem
                disp[dispB][4] -= passagem
                

