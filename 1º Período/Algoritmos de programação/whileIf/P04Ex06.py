S = 0
for i in range(1,11,2):
    S += (i / i**2) - ((i + 1) / (i + 1) / i** 2)
print(f'{S : .3f}')