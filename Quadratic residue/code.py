ints = [14, 6, 11]
ans = []

for i in range(29):
    for j in ints:
        if j == (i**2) % 29:
            print(i)
            print(j)
