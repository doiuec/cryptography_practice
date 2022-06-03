import sympy.ntheory.modular

# x = 5 mod 7
# x = 2 mod 11

m=[5,11,17]
a=[2,3,5]

(x,y) = sympy.ntheory.modular.crt(m,a)

print(f"x={x}, y={y}, x%7={x%7}, x%11={x%11}")
