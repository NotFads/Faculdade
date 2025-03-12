programaAtivo = 1
while programaAtivo == 1:
    nota = float(input('Entre com a nota do aluno: '))
    if nota >= 0 and nota <=10:
        programaAtivo = 0
    else:
        print('Nota inválida! Entre com uma nota de 0 a 10.')
        programaAtivo = 1