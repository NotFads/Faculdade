cid = int(input('Entre com o número de cidadãos: '))
sSal = 0
sFil = 0
mSal = -999999
cont = 0
for i in range(0, cid):
    sal = float(input(f'Entre o salário da {i + 1}ª pessoa: '))
    fil = int(input(f'Entre a quantidade de filho da {i + 1}ª pessoa: '))
    sSal += sal
    sFil += fil
    if sal > mSal:
        mSal = sal
    if sal < 100:
        cont += 1
print(f'\n\ta. {sSal / cid}\n\tb. {sFil / cid}\n\tc. {mSal}\n\td. {(cont / cid) * 100}%')
