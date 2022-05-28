import sympy as sym

f = open('output_479698cde19aaa05d9e9dfca460f5443.txt', 'r')
datalist = f.readlines()
p = int(datalist[0].replace('p = ', ''))
datalist[2] = datalist[2].replace('ints = [', '')
datalist[2] = datalist[2].replace(']', '')
datalist[2] = datalist[2].split(', ')
for i in range(len(datalist[2])):
    datalist[2][i] = int(datalist[2][i])
#print(p)
#print(datalist[2])

tmp = 0

for i in datalist[2]:
    if pow(i, (p-1)//2, p) == 1:
        tmp = i
print(pow(tmp, (p+1)//4, p))

f.close()
