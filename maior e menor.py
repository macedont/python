n = float(input("Informe um numero: "))
n1 = float(input("Informe um numero: "))
n2 = float(input("Informe um numero: "))

if n > n1 and n > n2:
    maior = n
elif n1 > n2 and n1 > n:
     maior = n1
else:
    maior = n2

if n < n1 and n < n2:
    menor = n
elif n1 < n2 and n1 < n:
    menor = n1
else:
    menor = n2

print(maior)
print(menor)
