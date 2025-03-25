import random
nAdv = 0
nSec = 1
programaAtivo = 1
while programaAtivo:   
    nSec = random.randint(1000,9999)
    nSec1 = nSec // 1000
    nSec2 = (nSec // 100) % 10
    nSec3 = (nSec // 10) % 10
    nSec4 = nSec % 10
    for i in range(1,11) and nAdv != nSec:
        dica = 1
        nAdv = int(input('Adivinhe um número aleatório de 1000 a 9999: '))
        nAdv1 = nAdv // 1000
        nAdv2 = ((nAdv // 100) % 10)
        nAdv3 = ((nAdv // 10) % 10)
        nAdv4 = nAdv % 10
        if nSec1 == nAdv1:
            print(nSec1, end=" ")
        else:
            if i < 5:
                print('_', end=" ")
            else:
                if dica == 1:
                    if nSec1 % 2 == 0:
                        print('Par',end=" ")
                    else:
                        print('Impar', end=" ")
                    dica = 0
                else:
                    print('_',end=" ")                    
        if nSec2 == nAdv2:
            print(nSec2,end=" ")
        else:
            if i < 5:
                print('_', end=" ")
            else:
                if dica == 1:
                    if nSec2 % 2 == 0:
                        print('Par',end=" ")
                    else:
                        print('Impar', end=" ")
                    dica = 0
                else:
                    print('_',end=" ")                
        if nSec3 == nAdv3:
            print(nSec3,end=" ")
        else:
            if i < 5:
                print('_', end=" ")
            else:
                if dica == 1:
                    if nSec3 % 2 == 0:
                        print('Par',end=" ")
                    else:
                        print('Impar', end=" ")
                    dica = 0
                else:
                    print('_',end=" ")
        if nSec4 == nAdv4:
            print(nSec4, end=" ")
        else:
            if i < 5:
                print('_', end=" ")
            else:
                if dica == 1:
                    if nSec4 % 2 == 0:
                        print('Par',end=" ")
                    else:
                        print('Impar', end=" ")
                    dica = 0
                else:
                    print('_',end=" ")
    else:
        print('Você errou o número!')
else:
    print('Você acertou o número!')
            