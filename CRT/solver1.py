import math

t = ''

exec('c='+open("output.txt").read())
tmp=[0] * len(c)

for i in range(len(c)):
    cc = c[i]
    for j in range(len(c)):
        if((cc-j) ** .5).is_integer():
            #print(str(cc) + "+" + str(j))
            tmp[j] = cc-j

print(tmp)

for i in range(len(tmp)):
    tmp[i] = math.sqrt(tmp[i]) - i

for i in range(len(tmp)):
    print(chr(int(tmp[i])))