from sympy import discrete_log as dl
from Crypto.Util.number import long_to_bytes as l2b

a = 288260533169915
p = 1007621497415251

exec('c='+open("outpuy2.txt").read())

tmp = ''

for i in range(len(c)):
    cc = c[i]
    try:
        r = dl(p, cc, a)
        tmp += '1'
    except:
        r = dl(p, -cc%p, a)
        tmp += '0'
print(l2b(int(tmp,2)))
