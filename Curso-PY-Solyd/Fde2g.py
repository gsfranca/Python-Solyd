a = float(input("Valor de A: "))
b = float(input("Valor de B: "))
c = float(input("Valor de C: "))

delta1 = (b*b)
delta2 = -4*(a*c)
delta = delta1 + delta2

raizdelta = delta**0.5

xmenos1 = -(b) - raizdelta
xmenos2 = 2*a
xmenos = xmenos1 / xmenos2
xmais1  = -(b) + raizdelta
xmais2 = 2*a
xmais = xmais1 / xmais2


print("Delta é:", delta)
print("Raiz de Delta é:", raizdelta)
print("O valor de X+ é: ", xmais)
print("O valor de X- é: ", xmenos)
