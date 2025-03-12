h = int(input('Entre com a altura desejada da pirâmide: '))
for i in range(h):
    for j in range(i):
        print('* ',end="")
    print('')
for i in range(h,0,-1):
    for j in range(i):
        print('* ',end="")
    print('')    
