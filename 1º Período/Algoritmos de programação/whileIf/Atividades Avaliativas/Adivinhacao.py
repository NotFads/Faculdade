import random
programaAtivo = 1
while programaAtivo == 1:   
    #nSec = random.randint(1000,9999)
    nSec = 1234
    nSec1 = nSec // 1000
    nSec2 = (nSec // 100) % 10
    nSec3 = (nSec // 10) % 10
    nSec4 = nSec % 10
    i = 10
    acert = 0
    tent = 0
    print(f'\t=> Bem vindo(a) ao Jogo da Adivinhação! <=\n\nVocê possui 10 tentativas para adivinhar uma senha aleatória de 4 digitos (entre 1000 e 9999). \nA partir da 5ª tentativa o jogo irá te dar dicas sobre os números não descobertos.')
    input(f'\t\t\t<<< Pressione Enter >>>')
    while i > 0:
        dica = 1
        tDica = random.randint(1,2)
        nAdv = int(input('Digite a sua tentativa de senha: '))
        while nAdv < 1000 or nAdv > 9999:
            print(f'\t\tATENÇÃO!!!\n\t\t\tSenha inválida!\n\t\t\tDigite um Valor Entre 1000 e 9999.')
            nAdv = int(input('Digite a sua tentativa de senha: '))
        nAdv1 = nAdv // 1000
        nAdv2 = ((nAdv // 100) % 10)
        nAdv3 = ((nAdv // 10) % 10)
        nAdv4 = nAdv % 10
        print('Sua senha é:', end=" ")
        if nSec1 == nAdv1:
            print(nSec1, end=" ")
            acert += 1
        elif i <= 6 and dica == 1:
            if tDica == 1:
                if nSec1 % 2 == 0:
                    print("Par", end=" ")
                else:
                    print("Ímpar", end=" ")
            else:
                if nSec1 >= 5:
                    print(">=5", end=" ")
                else:
                    print("<5",end=" ")
            dica = 0        
        else:
            print('_', end=" ")    
        if nSec2 == nAdv2:
            print(nSec2,end=" ")
            acert += 1
        elif i <= 6 and dica == 1:
            if tDica == 1:
                if nSec2 % 2 == 0:
                    print('Par',end=" ")
                else:
                    print('Impar', end=" ")
            else:
                if nSec2 >= 5:
                    print(">=5",end=" ")
                else:
                    print("<5",end=" ")
            dica = 0
        else:
            print('_', end=" ")              
        if nSec3 == nAdv3:
            print(nSec3,end=" ")
            acert += 1
        elif i <= 6 and dica == 1:
            if tDica == 1:
                if nSec3 % 2 == 0:
                    print('Par',end=" ")
                else:
                    print('Impar', end=" ")
            else:
                if nSec3 >= 5:
                    print(">=5",end=" ")
                else:
                    print("<5",end=" ")
            dica = 0
        else:
            print('_', end=" ")
        if nSec4 == nAdv4:
            print(nSec4, end=" ")
            acert += 1

        elif i <= 6 and dica == 1:
            if tDica == 1:
                if nSec4 % 2 == 0:
                    print('Par',end=" ")
                else:
                    print('Impar', end=" ")
            else:
                if nSec4 >= 5:
                    print(">=5",end=" ")
                else:
                    print("<5",end=" ")
            dica = 0
        else:
            print('_', end=" ")
        tent = i
        if nSec == nAdv:
            i = -1
        else:
            i -= 1
            if acert == 0:
                print('\nVocê não acertou nenhum dígito...')
            else:
                print(f'\nVocê acertou {acert} dígito(s)...')
            print(f'Restam {i} tentativas...')
            input(f'\t\t\t<<< Pressione Enter >>>')
        acert = 0
    else:
        if i == 0:
            print(f'Número de Tentativas Excedidas!!!\n\nVOCÊ PERDEU!\nA SENHA ERA: {nSec}')
            input(f'\n\t\t\t<<< Pressione Enter >>>')
        else:
            print(f'\n\tP A R A B É N S ! ! !\n\n\t\tVocê adivinhou a senha: {nSec}\n\tem {tent} tentativas...')
            input(f'\n\t\t\t<<< Pressione Enter >>>')
        programaAtivo = int(input('Jogar De Novo? 1=SIM E 0=NÃO\n'))
        