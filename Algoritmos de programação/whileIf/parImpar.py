n = int(input('Entre com um  número: '))
nPar = 0
nImpar = 0
for i in range(1,n,+1):
    if n % 2 == 0:
        nPar = nPar + 1
    else:
        nImpar = nImpar + 1
print(f'\t\nNúmeros par: {nPar}\t\nNúmeros Impares: {nImpar}')