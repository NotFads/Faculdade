n = int(input('Entre com um número inteiro: '))
F = 0
while n > 0:
    for i in range(1,n + 1,2):
        F *= i * (i + 1)
    print({F}, end=" ")
    n = int(input('Entre com um número inteiro: '))