N = int(input('Entre com um número inteiro: '))
S = 0

a, b = 2, 3  

for i in range(2, N + 2):  
    print(a, end=" ")
    a, b = b, a + b

