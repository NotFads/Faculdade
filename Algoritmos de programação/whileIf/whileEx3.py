i = 0
somaN = 0
while i < 5:
    n = float(input('Entre com um número: '))
    somaN = somaN + n
    i = i + 1
media = somaN / 5
print(f'{media : .1f}')