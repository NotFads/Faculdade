n = []
for i in range(1500,2701):
    if i >= 1500 and i <=2700:
        if i % 7 == 0 and i % 5 == 0:
            n.append(str(i))
print(','.join(n))